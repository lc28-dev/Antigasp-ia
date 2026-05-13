import streamlit as st

# On utilise st.components.v1.html pour injecter le code HTML/CSS
import streamlit.components.v1 as components

# Ton code HTML doit être entouré de trois guillemets """ pour être une "string"
html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <style>
        /* Colle tout le CSS que je t'ai donné ici */
        :root { --primary: #2d5a27; --accent: #e67e22; --light: #f9f7f2; }
        body { font-family: 'Arial', sans-serif; background: var(--light); margin: 0; }
        .hero { 
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
            url('https://images.unsplash.com/photo-1490818387583-1baba5e638af?w=1200');
            background-size: cover; height: 400px; display: flex; 
            align-items: center; justify-content: center; color: white; text-align: center;
        }
        .card-container { display: flex; gap: 20px; padding: 40px; justify-content: center; }
        .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 300px; }
    </style>
</head>
<body>
    <section class="hero">
        <div>
            <h1>Cuisiner, c'est s'aimer.</h1>
            <p>L'anti-gaspi au service du goût.</p>
        </div>
    </section>

    <div class="card-container">
        <div class="card"><h3>🥑 Pour vous</h3><p>Mangez sain, vivez mieux.</p></div>
        <div class="card"><h3>🌍 Anti-Gaspi</h3><p>Rien ne se perd, tout se déguste.</p></div>
    </div>
</body>
</html>
"""

# Cette ligne affiche le rendu dans ton appli Streamlit
components.html(html_code, height=800, scrolling=True)
