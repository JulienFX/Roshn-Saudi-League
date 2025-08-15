import streamlit as st
import pandas as pd
import plotly.express as px
from data import match_info, stats_equipes, stats_joueurs, df_lineup

# --- ÉTAGE 2 : STATS ---
col4, col5 = st.columns([2,2])
with col4:
    st.subheader("📊 Stats équipes")
    st.dataframe(stats_equipes.set_index("Equipe"), height=110)
with col5:
    st.subheader("🏆 Top joueurs")

    # Affichage initial (par défaut 'Buts')
    stat_options = ["Buts", "Passes", "Dribbles"]
    default_stat = "Buts"
    top_joueurs = stats_joueurs.sort_values(by=default_stat, ascending=False).head(3)
    table_placeholder = st.empty()
    table_placeholder.table(top_joueurs[["Nom", "Equipe", default_stat]])

    # Boîte de sélection en dessous du tableau
    selected_stat = st.selectbox("", stat_options, index=stat_options.index(default_stat))

    # Mise à jour du tableau selon la sélection
    top_joueurs = stats_joueurs.sort_values(by=selected_stat, ascending=False).head(3)
    table_placeholder.table(top_joueurs[["Nom", "Equipe", selected_stat]])

st.markdown("---")