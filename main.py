import streamlit as st
import pandas as pd
import plotly.express as px
from data import match_info, stats_joueurs, df_lineup

# CSS - La partie qui permet de faire en sorte que l'affichage s'étale sur toute la largeur d'écran disponible
st.markdown(
    """
    <style>
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# retirer le blanc du haut 
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

# Création des onglets
tab1, tab2 = st.tabs(["Page d'accueil", "Page 2"])

with tab1:
    st.sidebar.success("Page d'accueil")

    # --- ÉTAGE 1 : BANDEAU MATCH ---
    col1, col2, col3 = st.columns([2,4,2])

    with col2:
        st.markdown(
            f"""
            <div style='text-align:center; display:flex; justify-content:center; align-items:center;'>
                <img src='https://upload.wikimedia.org/wikipedia/en/a/a7/Paris_Saint-Germain_F.C..svg' style='height:24px; vertical-align:middle;'>
                <h2 style='margin:0;'>{match_info['equipe1']} vs {match_info['equipe2']}</h2>
                <img src='https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg' style='height:24px; vertical-align:middle;'>
            </div>
            <p style='text-align:center'>
                📅 {match_info['date']} | 🏟️ {match_info['stade']} | ⚽ {match_info['cote']}
            </p>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # --- ÉTAGE 3 : TERRAIN + STATS JOUEUR ---
    col6, col7 = st.columns([4,2])
    with col6:
        st.subheader("🖼️ Lineup")

        fig = px.scatter(
            df_lineup,
            x='PosX', y='PosY',
            color='Equipe', text='Nom',
            hover_data=['Poste'],
            color_discrete_map={'PSG': 'blue', 'Barça': 'red'},
            height=500, width=700
        )

        # Ajustement des points/joueurs
        fig.update_traces(
            textposition='top center',
            marker=dict(size=22, line=dict(width=2, color='black')),
            textfont=dict(color='white', size=14)
        )
        fig.update_xaxes(
        range=[0, 100],
        showticklabels=False,
        showgrid=False,  # ❌ enlève les lignes verticales/horizontales
        zeroline=False   # ❌ enlève la ligne "0"
        )

        fig.update_yaxes(
            autorange="reversed",
            range=[0, 100],
            showticklabels=False,
            showgrid=False,  # ❌ enlève les lignes verticales/horizontales
            zeroline=False   # ❌ enlève la ligne "0"
        )

        # Axes & fond
        fig.update_yaxes(autorange="reversed", range=[0, 100], showticklabels=False)
        fig.update_xaxes(range=[0, 100], showticklabels=False)
        fig.update_layout(
            plot_bgcolor='#34C924',
            margin=dict(l=5, r=5, t=5, b=5),
        )

        # =====================
        # TRAÇÉS DU STADE (sans lignes horizontales inutiles)
        # =====================

        # Contour du terrain
        fig.add_shape(type="rect", x0=0, y0=0, x1=100, y1=100, line=dict(color="grey", width=3),layer="below")

        # Ligne médiane
        fig.add_shape(type="line", x0=50, y0=0, x1=50, y1=100, line=dict(color="grey", width=2),layer="below")

        # Rond central
        fig.add_shape(type="circle", x0=40, y0=40, x1=60, y1=60, line=dict(color="grey", width=2),layer="below")

        # Point central
        fig.add_shape(type="circle", x0=49.5, y0=49.5, x1=50.5, y1=50.5, fillcolor="grey", line=dict(color="white"),layer="below")

        # Surfaces de réparation gauche et droite
        fig.add_shape(type="rect", x0=0, y0=21, x1=18, y1=79, line=dict(color="grey", width=2),layer="below")
        fig.add_shape(type="rect", x0=82, y0=21, x1=100, y1=79, line=dict(color="grey", width=2),layer="below")

        # Petites surfaces gauche et droite
        fig.add_shape(type="rect", x0=0, y0=36, x1=6, y1=64, line=dict(color="grey", width=2),layer="below")
        fig.add_shape(type="rect", x0=94, y0=36, x1=100, y1=64, line=dict(color="grey", width=2),layer="below")

        # Points de penalty
        fig.add_shape(type="circle", x0=11-0.5, y0=50-0.5, x1=11+0.5, y1=50+0.5, fillcolor="grey", line=dict(color="grey"),layer="below")
        fig.add_shape(type="circle", x0=89-0.5, y0=50-0.5, x1=89+0.5, y1=50+0.5, fillcolor="grey", line=dict(color="grey"),layer="below")

        st.plotly_chart(fig, use_container_width=True)

    with col7:
        st.subheader("📋 Stats joueur")
        player_name = st.selectbox("Joueur :", df_lineup["Nom"].tolist(), key="player_select")
        player_data = stats_joueurs[stats_joueurs["Nom"] == player_name]
        if not player_data.empty:
            st.write(f"**Equipe :** {player_data.iloc[0]['Equipe']}")
            st.write(f"**Buts :** {player_data.iloc[0]['Buts']}")
            st.write(f"**Passes :** {player_data.iloc[0]['Passes']}")
            st.write(f"**Dribbles :** {player_data.iloc[0]['Dribbles']}")

with tab2:
    st.header("Page 2")
    st.write("Hello")