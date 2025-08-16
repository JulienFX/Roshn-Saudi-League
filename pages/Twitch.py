import socket
import streamlit as st
import threading
# -----------------------------
# CONFIGURATION
# OAuth = Protocole d'autorisation
# Client id crée depuis https://dev.twitch.tv/console/apps
# https://id.twitch.tv/oauth2/authorize?client_id=wks1t7o5x4iei3hd92k6b819wi1myv&redirect_uri=http://localhost:8501&response_type=token&scope=chat:read
# -----------------------------
# CLIENT_ID = "wks1t7o5x4iei3hd92k6b819wi1myv"
#ACCESS_TOKEN = "oauth:6w3aii5ev4gtpzxls1njwi916wvayl"

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'adr_blody'
token = 'oauth:6w3aii5ev4gtpzxls1njwi916wvayl'
channel = '#adilrami23'

sock = socket.socket()
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

# Initialisation session_state AVANT tout
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'sock' not in st.session_state:
    st.session_state.sock = None

# Fonction d'écoute en continu
def listen_to_chat(sock):
    while True:
        try:
            resp = sock.recv(2048).decode('utf-8')
            print('hey')
        except Exception:
            break

        for line in resp.split("\r\n"):
            if line == "":
                print("vide")
                continue
            if line.startswith("PING"):
                sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
                print(resp)
            elif "PRIVMSG" in line:
                print('PRIVMSG')
                username = line.split('!', 1)[0][1:]
                message = line.split('PRIVMSG', 1)[1].split(':', 1)[1]
                # Ajout du message
                print(f"{username}: {message}")

# Connexion au chat une seule fois
if st.session_state.sock is None:
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\r\n".encode('utf-8'))
    st.session_state.sock = sock

    # Lancer le thread
    threading.Thread(target=listen_to_chat, args=(sock,), daemon=True).start()

# Affichage
st.title(f"Twitch Chat {channel}")
for msg in st.session_state.messages[-20:]:
    st.write(msg)

# Rafraîchit la page toutes les secondes
# st.rerun()

# # Queue pour partager les messages avec Streamlit
# chat_queue = queue.Queue()

# # -----------------------------
# # FONCTION POUR LE BOT SOCKET
# def twitch_socket_bot():
#     sock = ssl.wrap_socket(socket.socket())  # socket SSL
#     sock.connect((SERVER, PORT))
#     sock.send(f"PASS {ACCESS_TOKEN}\r\n".encode('utf-8'))
#     sock.send(f"NICK {NICKNAME}\r\n".encode('utf-8'))
#     sock.send(f"JOIN {CHANNEL}\r\n".encode('utf-8'))

#     while True:
#         resp = sock.recv(2048).decode('utf-8')
#         if resp.startswith('PING'):
#             sock.send("PONG\n".encode('utf-8'))
#         elif len(resp) > 0:
#             try:
#                 username, channel, message = re.search(
#                     r':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', resp
#                 ).groups()
#                 chat_queue.put({
#                     'datetime': datetime.now(),
#                     'username': username,
#                     'message': message
#                 })
#             except Exception:
#                 pass

# # -----------------------------
# # LANCER LE BOT DANS UN THREAD
# if "bot_started" not in st.session_state:
#     threading.Thread(target=twitch_socket_bot, daemon=True).start()
#     st.session_state.bot_started = True

# # -----------------------------
# # STREAMLIT - affichage du chat
# st.title(f"💬 Chat Twitch - {CHANNEL}")
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# chat_placeholder = st.empty()

# # Mise à jour en continu
# while True:
#     while not chat_queue.empty():
#         st.session_state.messages.append(chat_queue.get())

#     chat_text = "\n".join([
#         f"[{m['datetime'].strftime('%H:%M:%S')}] {m['username']}: {m['message']}" 
#         for m in st.session_state.messages[-20:]
#     ])
#     chat_placeholder.text(chat_text)
    
#     time.sleep(1)