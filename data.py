import pandas as pd 
# ----- Données fictives -----

# Match info
match_info = {
    "equipe1": "PSG",
    "equipe2": "Barça",
    "date": "2025-08-20 21:00",
    "stade": "Parc des Princes",
    "cote": "PSG 2.3 - Barça 3.1"
}

# Stats équipes (buts marqués, encaissés, forme derniers 5 matchs en points)
stats_equipes = pd.DataFrame({
    "Equipe": ["PSG", "Barça"],
    "Buts_Marques": [25, 22],
    "Buts_Encaisses": [10, 15],
    "Forme_5_derniers": [4, 3]
})

# Stats joueurs (pour top buteurs, passeurs, dribbleurs)
stats_joueurs = pd.DataFrame([
    {"Nom": "Mbappé", "Equipe": "PSG", "Buts": 12, "Passes": 5, "Dribbles": 30},
    {"Nom": "Messi", "Equipe": "PSG", "Buts": 8, "Passes": 10, "Dribbles": 25},
    {"Nom": "Neymar", "Equipe": "PSG", "Buts": 7, "Passes": 8, "Dribbles": 40},
    {"Nom": "Lewandowski", "Equipe": "Barça", "Buts": 15, "Passes": 4, "Dribbles": 20},
    {"Nom": "Fati", "Equipe": "Barça", "Buts": 5, "Passes": 6, "Dribbles": 22},
    {"Nom": "Pedri", "Equipe": "Barça", "Buts": 3, "Passes": 9, "Dribbles": 18},
])

# Lineup joueurs PSG et Barça (positions pour scatter plot)
lineup = [
  {"Nom": "Navas", "Equipe": "PSG", "Poste": "Gardien", "PosX": 10, "PosY": 50},
  {"Nom": "Hakimi", "Equipe": "PSG", "Poste": "Défenseur Droit", "PosX": 20, "PosY": 80},
  {"Nom": "Kimpembe", "Equipe": "PSG", "Poste": "Défenseur Central Droit", "PosX": 25, "PosY": 65},
  {"Nom": "Marquinhos", "Equipe": "PSG", "Poste": "Défenseur Central Gauche", "PosX": 25, "PosY": 35},
  {"Nom": "Nuno Mendes", "Equipe": "PSG", "Poste": "Défenseur Gauche", "PosX": 20, "PosY": 20},
  {"Nom": "Verratti", "Equipe": "PSG", "Poste": "Milieu Central", "PosX": 40, "PosY": 50},
  {"Nom": "Paredes", "Equipe": "PSG", "Poste": "Milieu Défensif", "PosX": 35, "PosY": 65},
  {"Nom": "Gueye", "Equipe": "PSG", "Poste": "Milieu Offensif", "PosX": 35, "PosY": 35},
  {"Nom": "Messi", "Equipe": "PSG", "Poste": "Ailier Droit", "PosX": 45, "PosY": 80},
  {"Nom": "Mbappé", "Equipe": "PSG", "Poste": "Avant-centre", "PosX": 45, "PosY": 50},
  {"Nom": "Neymar", "Equipe": "PSG", "Poste": "Ailier Gauche", "PosX": 45, "PosY": 20},
  {"Nom": "Ter Stegen", "Equipe": "Barça", "Poste": "Gardien", "PosX": 90, "PosY": 50},
  {"Nom": "Dest", "Equipe": "Barça", "Poste": "Défenseur Droit", "PosX": 80, "PosY": 80},
  {"Nom": "Piqué", "Equipe": "Barça", "Poste": "Défenseur Central Droit", "PosX": 75, "PosY": 65},
  {"Nom": "Araujo", "Equipe": "Barça", "Poste": "Défenseur Central Gauche", "PosX": 75, "PosY": 35},
  {"Nom": "Alba", "Equipe": "Barça", "Poste": "Défenseur Gauche", "PosX": 80, "PosY": 20},
  {"Nom": "Busquets", "Equipe": "Barça", "Poste": "Milieu Défensif", "PosX": 60, "PosY": 50},
  {"Nom": "De Jong", "Equipe": "Barça", "Poste": "Milieu Central Droit", "PosX": 65, "PosY": 70},
  {"Nom": "Pedri", "Equipe": "Barça", "Poste": "Milieu Central Gauche", "PosX": 65, "PosY": 30},
  {"Nom": "Gavi", "Equipe": "Barça", "Poste": "Milieu Offensif", "PosX": 70, "PosY": 50},
  {"Nom": "Fati", "Equipe": "Barça", "Poste": "Ailier Gauche", "PosX": 85, "PosY": 30},
  {"Nom": "Lewandowski", "Equipe": "Barça", "Poste": "Avant-centre", "PosX": 85, "PosY": 65},
]

##data 
# Données fictives pour les entraîneurs et remplaçants
entraineurs = {
    "PSG": "Christophe Galtier",
    "Barça": "Xavi Hernandez"
}

remplacants = {
    "PSG": ["Ramos", "Donnarumma", "Soler", "Ekitike", "Sanches"],
    "Barça": ["Raphinha", "Torres", "Kessie", "Christensen", "Pena"]
}

df_lineup = pd.DataFrame(lineup) # chargement des données pour la composition avec les joueurs 
