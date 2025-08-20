import streamlit as st
import webbrowser

# Configuration de la page
st.set_page_config(
    page_title="Actu SPL",
    page_icon="📰",
    layout="wide"
)

# CSS pour le style
st.markdown(
    """
    <style>
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100% !important;
    }
    .stButton button {
        background-color: #1DA1F2;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 20px;
        font-weight: bold;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #1a91da;
    }
    .twitter-container {
        text-align: center;
        margin-top: 5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre de la page
st.title("📰 Actualités SPL")

# Description
st.markdown("""
Restez informé des dernières actualités de la Super League en suivant notre compte Twitter officiel.
Vous y trouverez les dernières nouvelles, analyses exclusives et mises à jour en direct.
""")

# Conteneur pour centrer le bouton
st.markdown('<div class="twitter-container">', unsafe_allow_html=True)

# Bouton pour rediriger vers Twitter
if st.button("📱 Suivre @actuSPL sur Twitter", key="twitter_redirect"):
    webbrowser.open_new_tab("https://twitter.com/actuSPL")

st.markdown('</div>', unsafe_allow_html=True)

# Espacement
st.markdown("<br><br>", unsafe_allow_html=True)

# Section supplémentaire avec informations
st.subheader("À propos de @actuSPL")
st.info("""
Notre compte Twitter **@actuSPL** vous offre:
- ⚽ Les dernières transferts et rumeurs
- 📊 Analyses statistiques des matchs
- 🔥 Highlights et moments forts
- 🎙️ Interviews exclusives
- 📅 Calendriers des matchs à venir
- 🏆 Classements en direct

Suivez-nous pour ne rien manquer de l'actualité frénétique de la Super League!
""")

# Pied de page
st.markdown("---")
st.caption("© 2024 SPL Actu - Toutes les actualités de la Super League")