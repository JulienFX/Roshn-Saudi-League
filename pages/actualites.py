import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Actu SPL",
    page_icon="📰",
)

# CSS pour centrer et gérer la taille
st.markdown(
    """
    <style>
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100% !important;
    }
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 3rem;
        gap: 50px;
    }
    .image-container img {
        width: 150px;  /* Ajuste la taille selon tes besoins */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titre de la page
st.title("📰 Actualités SPL")

# Description
st.markdown("""
Restez informé des dernières actualités de la Super League.
Vous y trouverez les dernières nouvelles, analyses exclusives et mises à jour en direct.
""")

# --- Images côte à côte, centrées, même taille ---
spacer_left, center, spacer_right = st.columns([1, 3, 1])  # centre le bloc
with center:
    col_img1, col_img2 = st.columns(2)
    with col_img1:
        st.image("actuSPL.png", caption="@actuSPL", width=400)
    with col_img2:
        st.image("znfoot.png", caption="@zacknanifoot", width=800)



# Suite du contenu
st.markdown("<br><br>", unsafe_allow_html=True)
st.subheader("À propos de @actuSPL et @ZackNaniFoot")
st.info("""
- ⚽ Les dernières transferts et rumeurs
- 📊 Analyses statistiques des matchs
- 🔥 Highlights et moments forts
- 🎙️ Interviews exclusives
- 📅 Calendriers des matchs à venir
- 🏆 Classements en direct
""")

st.markdown("---")
st.caption("© 2025 SPL Actu - Toutes les actualités de la Super League")
