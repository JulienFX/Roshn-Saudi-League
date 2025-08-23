import pandas as pd 
# ----- Données fictives -----

team1 = "AL-NASSR"
team2 = "AL-AHLI"

# Match info
match_info = {
    "equipe1": team1,
    "equipe2": team2,
    "date": "23-08-2025 14:00 🇫🇷",
    "stade": "Hong Kong Stadium",
    "cote": team1+" 2.1 - "+ team2 +" 2.9"
}

# Stats équipes (buts marqués, encaissés, forme derniers 5 matchs en points)
stats_equipes = pd.DataFrame({
    "Equipe": [team1, team2],
    "Buts_Marques": [2, 5],
    "Buts_Encaisses": [1, 1],
    "Forme_5_derniers": [4, 3]
})

# Stats joueurs (pour top buteurs, passeurs, dribbleurs)
stats_joueurs = pd.DataFrame([
    {"Nom": "Mbappé", "Equipe": team1, "Buts": 12, "Passes": 5, "Dribbles": 30},
    {"Nom": "Messi", "Equipe": team1, "Buts": 8, "Passes": 10, "Dribbles": 25},
    {"Nom": "Neymar", "Equipe": team1, "Buts": 7, "Passes": 8, "Dribbles": 40},
    {"Nom": "Lewandowski", "Equipe": team2, "Buts": 15, "Passes": 4, "Dribbles": 20},
    {"Nom": "Fati", "Equipe": team2, "Buts": 5, "Passes": 6, "Dribbles": 22},
    {"Nom": "Pedri", "Equipe": team2, "Buts": 3, "Passes": 9, "Dribbles": 18},
])

# Lineup joueurs PSG et Barça (positions pour scatter plot)
lineup = [
  {"Nom": "Bento", "Equipe": team1, "Poste": "Gardien", "PosX": 10, "PosY": 50},
  {"Nom": "Nawaf Bu Washl", "Equipe": team1, "Poste": "Défenseur Droit", "PosX": 20, "PosY": 80},
  {"Nom": "Simakan", "Equipe": team1, "Poste": "Défenseur Central Droit", "PosX": 20, "PosY": 60},
  {"Nom": "Martinez", "Equipe": team1, "Poste": "Défenseur Central Gauche", "PosX": 20, "PosY": 40},
  {"Nom": "Yahya", "Equipe": team1, "Poste": "Défenseur Gauche", "PosX": 20, "PosY": 20},
  {"Nom": "Coman", "Equipe": team1, "Poste": "Milieu Droit", "PosX": 30, "PosY": 80},
  {"Nom": "Al-Khaibari", "Equipe": team1, "Poste": "Milieu Central", "PosX": 30, "PosY": 60},
  {"Nom": "Brozovic", "Equipe": team1, "Poste": "Milieu Central", "PosX": 30, "PosY": 40},
  {"Nom": "Wesley", "Equipe": team1, "Poste": "Milieu Gauche", "PosX": 30, "PosY": 20},
  {"Nom": "Félix", "Equipe": team1, "Poste": "Avant-centre", "PosX": 37.5, "PosY": 50},
  {"Nom": "Ronaldo", "Equipe": team1, "Poste": "Ailier Gauche", "PosX": 45, "PosY": 50},
  {"Nom": "Mendy", "Equipe": team2, "Poste": "Gardien", "PosX": 90, "PosY": 50},
  {"Nom": "Matteo Dams", "Equipe": team2, "Poste": "Défenseur Droit", "PosX": 80, "PosY": 80},
  {"Nom": "Demiral", "Equipe": team2, "Poste": "Défenseur Central Droit", "PosX": 80, "PosY": 60},
  {"Nom": "Ibanez", "Equipe": team2, "Poste": "Défenseur Central Gauche", "PosX": 80, "PosY": 40},
  {"Nom": "Ali Majrashi", "Equipe": team2, "Poste": "Défenseur Gauche", "PosX": 80, "PosY": 20},
  {"Nom": "Mahrez", "Equipe": team2, "Poste": "Milieu Droit", "PosX": 70, "PosY": 20},
  {"Nom": "Kessie", "Equipe": team2, "Poste": "Milieu Central", "PosX": 70, "PosY": 40},
  {"Nom": "Millot", "Equipe": team2, "Poste": "Milieu Central", "PosX": 70, "PosY": 60},
  {"Nom": "Galeno", "Equipe": team2, "Poste": "Milieu Gauche", "PosX": 70, "PosY": 80},
  {"Nom": "Al-Buraikan", "Equipe": team2, "Poste": "Ailier Gauche", "PosX": 60, "PosY": 40},
  {"Nom": "Toney", "Equipe": team2, "Poste": "Avant-centre", "PosX": 60, "PosY": 60},
]

##data 
# Données fictives pour les entraîneurs et remplaçants
entraineurs = {
    team1: "Jorge Jesus",
    team2: "Matthias Jaissle"
}

remplacants = {
    team1: ["Al-Amri", "Al-Aqidi", "Al-Ghanam", "Al-Hassan", "Salem Al Najdi", "Al Nemer", "Aman", "Borges", "Al Elewai", "Gharib", "Haqawi", "Marran"],
    team2: ["Al Sanbi", "Abdullah Abdo", "Al Khaibari", "Rayan Hamed", "Balobaid", "Sulaiman", "Yousef", "Al Muwallad", "Aboulshamat", "Alijohani", "Al-Zubaidi", "Al-Rashidi"]
}

df_lineup = pd.DataFrame(lineup) # chargement des données pour la composition avec les joueurs 
