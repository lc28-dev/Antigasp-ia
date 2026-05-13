import streamlit as st
from groq import Groq

# 1. Configuration Pro
st.set_page_config(page_title="AntigaspIA | Haute Cuisine", page_icon="🍽️", layout="wide")

# 2. Design "Square & Premium" (Style SaaS Moderne)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&family=Playfair+Display:wght@700&display=swap');
    
    .stApp { background-color: #F8FAFC; font-family: 'Inter', sans-serif; }

    /* Header Compact et Carré */
    .hero-banner {
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        padding: 60px 20px;
        color: white;
        text-align: center;
        border-bottom: 4px solid #0F172A;
    }

    .brand-name { font-family: 'Playfair Display', serif; font-size: 3.5rem; letter-spacing: -1px; margin: 0; }
    .hero-tagline { font-size: 1rem; font-weight: 300; opacity: 0.8; text-transform: uppercase; letter-spacing: 2px; }

    /* Conteneur principal "Carré" */
    .main-workspace {
        max-width: 1100px;
        margin: -40px auto 40px auto;
        display: grid;
        grid-template-columns: 1fr 350px;
        gap: 20px;
        position: relative;
        z-index: 100;
    }

    /* Bloc de Saisie */
    .input-card {
        background: white;
        padding: 30px;
        border: 2px solid #0F172A;
        box-shadow: 10px 10px 0px #0F172A; /* Effet carré pro */
    }

    /* Bloc Latéral (Options) */
    .side-card {
        background: #0F172A;
        padding: 30px;
        color: white;
        border: 2px solid #0F172A;
        box-shadow: 10px 10px 0px #CBD5E1;
    }

    /* Bouton Noir Massif */
    .stButton>button {
        background-color: #0F172A;
        color: white;
        border-radius: 0px; /* Carré */
        height: 60px;
        font-weight: 800;
        text-transform: uppercase;
        border: none;
        width: 100%;
        transition: 0.2s;
    }
    .stButton>button:hover { background-color: #334155; transform: translate(-2px, -2px); box-shadow: 4px 4px 0px #94A3B8; }

    /* Custom Text Area */
    .stTextArea textarea { border-radius: 0px; border: 2px solid #E2E8F0; padding: 15px; }
    
    h3 { font-family: 'Playfair Display', serif; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="hero-banner">
        <p class="hero-tagline">Intelligence Artificielle Culinaire</p>
        <h1 class="brand-name">AntigaspIA</h1>
    </div>
    """, unsafe_allow_html=True)

# --- WORKSPACE ---
st.markdown("<div class='main-workspace'>", unsafe_allow_html=True)

# Colonne Gauche : L'ACTION
with st.container():
    st.markdown("<div class='input-card'>", unsafe_allow_html=True)
    st.markdown("<h3>Optimisation instantanée</h3>", unsafe_allow_html=True)
    
    ingredients = st.text_area("Inventaire de vos restes :", 
                               placeholder="Ex: 2 filets de bar, citron vert, reste de quinoa...", 
                               height=180, label_visibility="collapsed")
    
    if st.button("Lancer l'analyse culinaire"):
        if not ingredients:
            st.error("Veuillez renseigner votre inventaire.")
        else:
            try:
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])
                with st.spinner('Analyse en cours...'):
                    prompt = f"Expert culinaire. Recette pro avec : {ingredients}. Style : Fiche technique, précis."
                    completion = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
                    st.markdown("---")
                    st.markdown("### 📋 Fiche Recette AntigaspIA")
                    st.info(completion.choices[0].message.content)
            except:
                st.error("Erreur serveur.")
    st.markdown("</div>", unsafe_allow_html=True)

# Colonne Droite : OPTIONS & COMPTE (Plus pro)
with st.container():
    st.markdown("<div class='side-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:white; margin-bottom:20px;'>CONFIGURATION</h4>", unsafe_allow_html=True)
    
    st.selectbox("Régime", ["Standard", "Végétarien", "Sportif"], index=0)
    st.selectbox("Niveau", ["Amateur", "Chef"], index=1)
    
    st.markdown("<br><hr style='border-color:#334155'><br>", unsafe_allow_html=True)
    
    st.markdown("##### ESPACE MEMBRE")
    st.write("Sauvegardez vos fiches et préférences.")
    st.button("CRÉER UN COMPTE")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 0.8rem; margin-top: 100px;'>© 2024 AntigaspIA - Excellence, Précision, Durabilité.</p>", unsafe_allow_html=True)
