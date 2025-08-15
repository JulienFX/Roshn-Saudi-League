import re
import streamlit as st
from twitchio.ext import commands  # <-- important !
# -----------------------------
# CONFIGURATION
# -----------------------------
CLIENT_ID = "wks1t7o5x4iei3hd92k6b819wi1myv"
ACCESS_TOKEN = "h38wlia2j0uxzldlfe5gsyd3omgbyu"  # récupéré via l'URL OAuth 
CHANNEL = "Zacknani"        # le streamer dont tu veux lire le chat

# Création du bot
bot = commands.Bot(
    token=ACCESS_TOKEN,
    prefix="!",  # nécessaire mais pas utilisé ici
    initial_channels=[CHANNEL]
)

# Regex pour filtrer les questions
import re
question_pattern = re.compile(r'.{2,}\?{1,3}.*', re.UNICODE)

def is_question(message):
    return bool(question_pattern.fullmatch(message.strip()))

# Event quand un message est reçu
@bot.event
async def event_message(ctx):
    # Filtrer les messages du bot lui-même
    if ctx.author.name.lower() == CHANNEL.lower():
        return
    # Affiche les questions
    if is_question(ctx.content):
        print(f"{ctx.author.name}: {ctx.content}")  # tu peux remplacer print par Streamlit write

# Lancer le bot
bot.run()