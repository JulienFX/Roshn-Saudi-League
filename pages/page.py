import streamlit as st
import streamlit.components.v1 as components

# Ton code HTML/CSS/JS
html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Page HTML intégrée</title>
<style>
    body { font-family: Arial, sans-serif; background: #f4f4f4; text-align: center; padding: 2rem; }
    h1 { color: #333; }
    button {
        padding: 10px 20px;
        background: #4CAF50;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;
    }
    button:hover { background: #45a049; }
</style>
</head>
<body>
    <h1>Bonjour depuis du vrai HTML</h1>
    <p>Ce contenu est rendu en dehors du moteur Streamlit.</p>
    <button onclick="alert('Coucou depuis JS !')">Clique-moi</button>
</body>
</html>
"""

# Intégration dans Streamlit
components.html(html_code, height=400)
