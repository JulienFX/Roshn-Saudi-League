import socket
import threading
import time
import html
import queue
import streamlit as st
import streamlit.components.v1 as components
import datetime
import re

# -----------------------------
# CONFIGURATION
# OAuth = Protocole d'autorisation
# Client id crée depuis https://dev.twitch.tv/console/apps
# https://id.twitch.tv/oauth2/authorize?client_id=wks1t7o5x4iei3hd92k6b819wi1myv&redirect_uri=http://localhost:8501&response_type=token&scope=chat:read
# -----------------------------
# CLIENT_ID = "wks1t7o5x4iei3hd92k6b819wi1myv"
# ACCESS_TOKEN = "oauth:variable"

SERVER = 'irc.chat.twitch.tv'
PORT = 6667
NICKNAME = 'adr_blody'
TOKEN = 'oauth:fcxs5h0q1itzb5rdad7lcyfhoi5ta7'
CHANNEL = '#areliann'

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "sock" not in st.session_state:
    st.session_state.sock = None
if "listener_started" not in st.session_state:
    st.session_state.listener_started = False

# Une queue thread-safe pour transférer les messages
if "msg_queue" not in st.session_state:
    st.session_state.msg_queue = queue.Queue()


# Config écran 
# st.set_page_config(layout="wide")
# -----------------------------
# THREAD : écouter IRC
# -----------------------------
def listen_to_chat(sock: socket.socket, q: queue.Queue):
    buffer = ""
    while True:
        try:
            data = sock.recv(4096)
            if not data:
                break
            buffer += data.decode("utf-8", errors="ignore")
        except Exception:
            break

        lines = buffer.split("\r\n")
        buffer = lines.pop()

        for line in lines:
            if not line:
                continue

            if line.startswith("PING"):
                try:
                    sock.sendall(b"PONG :tmi.twitch.tv\r\n")
                except Exception:
                    return
                continue

            if " PRIVMSG " in line:
                try:
                    prefix, payload = line.split(" PRIVMSG ", 1)
                    username = prefix.split("!", 1)[0][1:]
                    message = payload.split(":", 1)[1]
                except Exception:
                    continue

                # 🔹 On pousse le message dans la queue
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                q.put(f"[{timestamp}] {username}: {message}")


# -----------------------------
# CONNEXION
# -----------------------------
def ensure_connection():
    if st.session_state.sock is None:
        s = socket.socket()
        s.connect((SERVER, PORT))
        s.sendall(f"PASS {TOKEN}\r\n".encode("utf-8"))
        s.sendall(f"NICK {NICKNAME}\r\n".encode("utf-8"))
        s.sendall(f"JOIN {CHANNEL}\r\n".encode("utf-8"))
        st.session_state.sock = s

    if not st.session_state.listener_started:
        t = threading.Thread(
            target=listen_to_chat,
            args=(st.session_state.sock, st.session_state.msg_queue),
            daemon=True,
        )
        t.start()
        st.session_state.listener_started = True

ensure_connection()

# -----------------------------
# MAIN THREAD : vider la queue dans session_state.messages
# -----------------------------
while not st.session_state.msg_queue.empty():
    msg = st.session_state.msg_queue.get_nowait()
    st.session_state.messages.append(msg)

# -----------------------------
# UI : Titre + Chat centrés (titre + box alignés)
# -----------------------------
WRAP_W = 1000  # <- ajuste ici (ex: 1000, 1100...)

line_re = re.compile(r'^\[(\d{2}:\d{2}:\d{2})\]\s+([^:]+):\s?(.*)$')

def render_messages_html(msgs):
    items_html = []
    for m in msgs:
        m = m.strip()
        mt = line_re.match(m)
        if mt:
            t, user, text = mt.groups()
            items_html.append(
                f"<div class='msg'>"
                f"<span class='time'>[{html.escape(t)}]</span> "
                f"<span class='user'>{html.escape(user)}</span>: "
                f"<span class='text'>{html.escape(text)}</span>"
                f"</div>"
            )
        else:
            items_html.append(f"<div class='msg'><span class='text'>{html.escape(m)}</span></div>")

    items = "\n".join(items_html)
    return f"""
    <div id="wrap">
      <h1 id="title">💬 Twitch Chat</h1>
      <div id="chatbox">{items}</div>
    </div>

    <script>
      const box = document.getElementById('chatbox');
      if (box) {{ box.scrollTop = box.scrollHeight; }}
    </script>

    <style>
      #wrap {{
        max-width: {WRAP_W}px;
        margin: 0 auto;
        overflow: visible;
      }}
      #title {{
        text-align: center;
        margin-bottom: 15px;
      }}
      #chatbox {{
        width: 100%;              /* prend 100% de #wrap */
        height: 70vh;
        overflow-y: auto;
        box-sizing: border-box;
        border-top: 1px solid blue;
        border-bottom: 1px solid blue;
        border-radius: 50px;
        padding: 30px 18px;
        background: white;
        font-family: system-ui, sans-serif;
        font-size: 1rem;
        color: black;
        text-align: left;
      }}
      .msg {{ margin: 8px 0; line-height: 1.45; word-wrap: break-word; }}
      .time {{ color: purple; font-weight: 700; margin-right: 6px; }}
      .user {{ color: #d40000; font-weight: 700; }}
      .text {{ color: black; }}
    </style>
    """

# 10 derniers messages
html_chunk = render_messages_html(st.session_state.messages[-10:])
components.html(html_chunk, height=600, width=WRAP_W, scrolling=False)

# -----------------------------
# Auto-refresh
# -----------------------------
try:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=1000, key="twitch_refresh")
except ImportError:
    time.sleep(1)
    st.rerun()