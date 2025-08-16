import socket
import threading
import time
import html
import queue
import streamlit as st
import streamlit.components.v1 as components
import datetime

# -----------------------------
# CONFIGURATION
# OAuth = Protocole d'autorisation
# Client id crée depuis https://dev.twitch.tv/console/apps
# https://id.twitch.tv/oauth2/authorize?client_id=wks1t7o5x4iei3hd92k6b819wi1myv&redirect_uri=http://localhost:8501&response_type=token&scope=chat:read
# -----------------------------
# CLIENT_ID = "wks1t7o5x4iei3hd92k6b819wi1myv"
#ACCESS_TOKEN = "oauth:6w3aii5ev4gtpzxls1njwi916wvayl"

SERVER = 'irc.chat.twitch.tv'
PORT = 6667
NICKNAME = 'adr_blody'
TOKEN = 'oauth:6w3aii5ev4gtpzxls1njwi916wvayl'
CHANNEL = '#Escolit0'

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
# UI : chatbox stylée
# -----------------------------
st.title(f"Twitch Chat {CHANNEL}")

def render_messages_html(msgs):
    items = "\n".join(
        f"<div class='msg'><span class='user'>{html.escape(m.split(':',1)[0])}</span>: "
        f"{html.escape(m.split(':',1)[1].lstrip() if ':' in m else m)}</div>"
        for m in msgs
    )
    return f"""
    <div id="chatbox">
        {items}
    </div>
    <script>
        const box = document.getElementById('chatbox');
        if (box) {{
            box.scrollTop = box.scrollHeight;
        }}
    </script>
    <style>
        #chatbox {{
            height: 60vh;
            overflow-y: auto;
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px;
            padding: 12px 14px;
            background: rgba(255,255,255,0.03);
            backdrop-filter: blur(4px);
            font-family: system-ui, sans-serif;
        }}
        .msg {{ margin: 6px 0; line-height: 1.35; word-wrap: break-word; }}
        .user {{ font-weight: 600; opacity: .9; }}
    </style>
    """

html_chunk = render_messages_html(st.session_state.messages[-200:])
components.html(html_chunk, height=420, scrolling=False)

# -----------------------------
# Auto-refresh
# -----------------------------
try:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=1000, key="twitch_refresh")
except ImportError:
    time.sleep(1)
    st.rerun()