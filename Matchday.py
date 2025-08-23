import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data import match_info, stats_joueurs, df_lineup, entraineurs, remplacants, team1, team2, stats_equipes

# CSS for full-width display and reduced padding
st.markdown(
    """
    <style>
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
        padding-bottom: 0rem;
        max-width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Additional custom styles for tab2
st.markdown("""
<style>
    .header-style {
        font-size: 30px;
        font-weight: bold;
        color: #2a9fd6;
        text-align: center;
        padding: 10px;
        margin-bottom: 20px;
        border-bottom: 2px solid #2a9fd6;
    }
    .metric-card {
        background: #1e2130;
        border-radius: 10px;
        padding: 15px;
        margin: 5px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .metric-title {
        font-size: 14px;
        color: #a1a1a1;
        margin-bottom: 5px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: white;
    }
    .team-name {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Création des onglets
tab1, tab2 = st.tabs(["Compositions", "Stats"])

with tab1:
    st.sidebar.success("Page d'accueil")

    # --- ÉTAGE 1 : BANDEAU MATCH ---
    col1, col2, col3 = st.columns([2,4,2])

    with col2:
        st.markdown(
            f"""
            <div style='text-align:center; display:flex; justify-content:center; align-items:center;'>
                <img src='https://upload.wikimedia.org/wikipedia/ar/a/ac/Al_Nassr_FC_Logo.svg' style='height:36px; vertical-align:middle;'>
                <h2 style='margin:0;'>{match_info['equipe1']} vs {match_info['equipe2']}</h2>
                <img src='https://upload.wikimedia.org/wikipedia/fr/7/70/Logo_Al-Ahli_FC_2025.svg' style='height:36px; vertical-align:middle;'>
            </div>
            <p style='text-align:center'>
                📅 {match_info['date']} | 🏟️ {match_info['stade']} | 🌡️ 31° 
            </p>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

# --- ÉTAGE 2 : LINEUP ---
    st.subheader("🖼️ Lineup")
    fig = px.scatter(
        df_lineup,
        x='PosX', y='PosY',
        color='Equipe', text='Nom',
        hover_data=['Poste'],
        color_discrete_map={team1: 'blue', team2: 'red'},
        height=500, width=700
    )

    # Ajustement des points/joueurs
    fig.update_traces(
        textposition='top center',
        marker=dict(size=22, line=dict(width=2, color='black')),
        textfont=dict(color='black', size=16)
    )
    fig.update_xaxes(
        range=[0, 100],
        showticklabels=False,
        showgrid=False,
        zeroline=False
    )

    fig.update_yaxes(
        autorange="reversed",
        range=[0, 100],
        showticklabels=False,
        showgrid=False,
        zeroline=False
    )

    # Axes & fond
    fig.update_layout(
        plot_bgcolor='#F7F7F7',
        margin=dict(l=5, r=5, t=5, b=5),
    )

    # Contour du terrain
    fig.add_shape(type="rect", x0=0, y0=0, x1=100, y1=100, line=dict(color="#E3E3E3", width=3), layer="below")

    # Ligne médiane
    fig.add_shape(type="line", x0=50, y0=0, x1=50, y1=100, line=dict(color="#E3E3E3", width=2), layer="below")

    # Rond central
    fig.add_shape(type="circle", x0=40, y0=40, x1=60, y1=60, line=dict(color="#E3E3E3", width=2), layer="below")

    # Point central
    fig.add_shape(type="circle", x0=49.5, y0=49.5, x1=50.5, y1=50.5, fillcolor="#E3E3E3", line=dict(color="#E3E3E3"), layer="below")

    # Surfaces de réparation gauche et droite
    fig.add_shape(type="rect", x0=0, y0=31, x1=10, y1=69, line=dict(color="#E3E3E3", width=2), layer="below")
    fig.add_shape(type="rect", x0=90, y0=31, x1=100, y1=69, line=dict(color="#E3E3E3", width=2), layer="below")

    # Petites surfaces gauche et droite
    fig.add_shape(type="rect", x0=0, y0=45, x1=2, y1=55, line=dict(color="#E3E3E3", width=2), layer="below")
    fig.add_shape(type="rect", x0=98, y0=45, x1=100, y1=55, line=dict(color="#E3E3E3", width=2), layer="below")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # --- ÉTAGE 3 : ENTRAÎNEURS + REMPLAÇANTS ---
    col_coach_sub1, col_coach_sub2 = st.columns(2)

    with col_coach_sub1:
        st.subheader("👔 Entraîneur")
        st.markdown(f"**{team1}**")
        st.write(entraineurs[team1])

        st.subheader("🔄 Remplaçants")
        st.markdown(f"**{team1}**")
        for remplacant in remplacants[team1]:
            st.write(f"- {remplacant}")

    with col_coach_sub2:
        st.subheader("👔 Entraîneur")
        st.markdown(f"**{team2}**")
        st.write(entraineurs[team2])

        st.subheader("🔄 Remplaçants")
        st.markdown(f"**{team2}**")
        for remplacant in remplacants[team2]:
            st.write(f"- {remplacant}")

with tab2:
    # --- En-tête avec animation ---
    st.markdown(f"""
    <div class="header-style">
        ⚽ PREVIEW DU MATCH ⚽<br>
    </div>
    """, unsafe_allow_html=True)

    # --- Section 1: Métriques clés ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">COTE DU MATCH</div>
            <div class="metric-value">{match_info['cote']}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        avg_goals = (stats_equipes.loc[0, "Buts_Marques"] + stats_equipes.loc[1, "Buts_Marques"]) / 2
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">MOYENNE DE BUTS PAR MATCH DES 2 équipes</div>
            <div class="metric-value">{avg_goals:.1f}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        last_meeting = team2+" 2-3 "+team1+" (13/02/2025)"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">DERNIÈRE RENCONTRE</div>
            <div class="metric-value">{last_meeting}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # # --- Section 2: Comparaison des équipes ---
    # st.subheader("📊 COMPARAISON DES ÉQUIPES")

    # # Graphique radar pour comparer les équipes
    # fig_radar = go.Figure()

    # for i, row in stats_equipes.iterrows():
    #     fig_radar.add_trace(go.Scatterpolar(
    #         r=[row['Buts_Marques'], row['Buts_Encaisses'], row['Forme_5_derniers']],
    #         theta=['Buts marqués', 'Buts encaissés', 'Forme récente'],
    #         fill='toself',
    #         name=row['Equipe']
    #     ))

    # fig_radar.update_layout(
    #     polar=dict(
    #         radialaxis=dict(
    #             visible=True,
    #             range=[0, 30]
    #         )),
    #     showlegend=True,
    #     template="plotly_dark",
    #     height=400
    # )

    # st.plotly_chart(fig_radar, use_container_width=True)

    # --- Section 3: Top joueurs avec visualisation interactive ---
    st.subheader("🌟 TOP JOUEURS")

    # Sélection de la statistique
    stat_options = ["Buts", "Passes D", "Dribbles"]
    selected_stat = st.selectbox("Choisissez une statistique:", stat_options, key="player_stat")

    # Tri des joueurs
    top_players = stats_joueurs.sort_values(by=selected_stat, ascending=False).head(5)

    # Graphique à barres animé
    fig_players = px.bar(top_players, 
                         x="Nom", 
                         y=selected_stat, 
                         color="Equipe",
                         color_discrete_map={team1: "#004170", team2: "#a50044"},
                         text=selected_stat,
                         title=f"Top 5 joueurs - {selected_stat}",
                         height=400)

    fig_players.update_traces(texttemplate='%{text}', textposition='outside')
    fig_players.update_layout(showlegend=False, 
                             yaxis_title=selected_stat,
                             xaxis_title="",
                             template="plotly_dark")

    st.plotly_chart(fig_players, use_container_width=True)

    # --- Section 5: Radar des Talents (Légende sur le côté) ---
    st.subheader("🕷️ PROFIL COMPARATIF DES STARS")

    # Couleurs pour chaque joueur (jusqu'à 5)
    player_colors = {
        0: "#004170",  # Bleu
        1: "#a50044",  # Rouge
        2: "#2e8b57",  # Vert
        3: "#ff8c00",  # Orange
        4: "#9370db"   # Violet
    }

    # Sélection des joueurs à comparer (jusqu'à 5)
    stars = st.multiselect(
        "Comparez plusieurs joueurs (max 5):", 
        stats_joueurs["Nom"].unique(),
        default=["Riyad Mahrez", "Cristiano Ronaldo"],
        max_selections=5
    )

    if len(stars) >= 1:
        # Préparation des données
        comparison_df = stats_joueurs[stats_joueurs["Nom"].isin(stars)].melt(
            id_vars=["Nom", "Equipe"],
            value_vars=["Buts", "Passes D", "Dribbles"],
            var_name="Statistique",
            value_name="Valeur"
        )
        
        # Création du radar chart
        fig_radar = go.Figure()
        
        for i, player in enumerate(stars):
            player_data = comparison_df[comparison_df["Nom"] == player]
            fig_radar.add_trace(go.Scatterpolar(
                r=player_data["Valeur"],
                theta=player_data["Statistique"],
                name=player,
                fill='toself',
                line_color=player_colors[i % 5],
                opacity=0.7
            ))
        
        # Configuration du layout avec légende à droite
        max_value = comparison_df["Valeur"].max() * 1.2  # Marge de 20%
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max_value],
                    gridcolor="rgba(255,255,255,0.3)"
                ),
                angularaxis=dict(
                    gridcolor="rgba(255,255,255,0.3)",
                    rotation=90
                )
            ),
            title="Comparaison des statistiques clés",
            template="plotly_dark",
            height=600,
            width=800,
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.1
            ),
            margin=dict(l=50, r=150, b=50, t=80)
        )
        
        # Ajout d'une note explicative
        st.caption("💡 Plus la surface colorée est grande, meilleur est le joueur sur l'ensemble des critères")
        
        st.plotly_chart(fig_radar, use_container_width=True)
        
        # Tableau récapitulatif sous le radar
        if len(stars) > 1:
            st.subheader("📊 Tableau Comparatif")
            pivot_df = comparison_df.pivot(index="Nom", columns="Statistique", values="Valeur")
            st.dataframe(
                pivot_df.style
                    .background_gradient(cmap="Blues", axis=0)
                    .format("{:.1f}"),
                use_container_width=True
            )
    else:
        st.warning("Sélectionnez au moins un joueur pour la comparaison")