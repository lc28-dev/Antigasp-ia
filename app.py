import streamlit as st
from groq import Groq

# 1. Configuration Pro
st.set_page_config(page_title="AntigaspIA | Haute Cuisine Circulaire", page_icon="🍽️", layout="wide")

# 2. Design "Luxe & Sobriété"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp { background-color: #ffffff; font-family: 'Inter', sans-serif; }

    /* Header avec Photo Réelle */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1556910103-1c02745aae4d?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        color: white;
        text-align: center;
        border-radius: 0 0 40px 40px;
    }

    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }

    /* Boite d'essai - L'élément central */
    .action-container {
        background: white;
        max-width: 850px;
        margin: -60px auto 40px auto;
        padding: 45px;
        border-radius: 24px;
        box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);
        position: relative;
        z-index: 99;
        border: 1px solid #f1f5f9;
    }

    /* Style du bouton "Action" */
    .stButton>button {
        background-color: #0f172a;
        color: white;
        border-radius: 8px;
        height: 65px;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #334155;
        transform: translateY(-2px);
    }

    /* Section Options / Inscription */
    .membership-section {
        background: #f8fafc;
        padding: 60px 20px;
        margin-top: 40px;
        border-radius: 30px;
        text-align: center;
    }

    .premium-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        margin: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="hero-section">
        <h1 class="main-title">AntigaspIA</h1>
        <p style="font-size: 1.3rem; font-weight: 300; opacity: 0.95; letter-spacing: 0.5px;">
            L'intelligence artificielle qui sublime vos ressources alimentaires.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- ZONE D'ESSAI (CE QUI SAUTE AUX YEUX) ---
with st.container():
    st.markdown("<div class="action-container">", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; font-family:Playfair Display; font-size:1.8rem; margin-bottom:25px;'>Optimisez vos restes en un clic</h2>", unsafe_allow_html=True)
    
    ingredients = st.text_area("", placeholder="Décrivez ici ce qu'il reste dans votre cuisine (ex: Dos de cabillaud, poireaux, demi-citron...)", label_visibility="collapsed", height=150)
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.button("LANCER L'ANALYSE CULINAIRE")
    
    st.markdown("<p style='text-align:center; font-size:0.85rem; color:#64748b; margin-top:20px;'>Usage gratuit • Résultats basés sur la haute gastronomie</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- RESULTATS ---
if submit:
    if not ingredients:
        st.warning("Veuillez fournir une liste d'ingrédients pour l'IA.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            with st.spinner('Génération de votre fiche recette personnalisée...'):
                prompt = f"Tu es AntigaspIA, un expert culinaire haut de gamme. Crée une recette précise avec ces restes : {ingredients}. Structure avec Titre élégant, Ingrédients, Étapes et un conseil antigaspillage pro."
                completion = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
                
                st.markdown("---")
                st.markdown("### 📋 Fiche Technique du Chef")
                st.write(completion.choices[0].message.content)
                st.balloons()
        except:
            st.error("Une erreur technique est survenue. Veuillez réessayer.")

# --- OPTIONS AVANCÉES & COMPTE ---
st.markdown("<div class='membership-section'>", unsafe_allow_html=True)
st.markdown("<h2 style='font-family:Playfair Display;'>Allez plus loin avec AntigaspIA</h2>", unsafe_allow_html=True)
st.markdown("<p style='color:#64748b;'>Personnalisez vos analyses et sauvegardez vos préférences nutritionnelles.</p>", unsafe_allow_html=True)

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("<div class='premium-card'><b>⚡️ Rapidité</b><br><small>Recettes en moins de 10 min</small></div>", unsafe_allow_html=True)
with col_b:
    st.markdown("<div class='premium-card'><b>🌱 Régimes</b><br><small>Végétarien, Keto, Sans Gluten</small></div>", unsafe_allow_html=True)
with col_c:
    st.markdown("<div class='premium-card'><b>📉 Budget</b><br><small>Calcul du coût par portion</small></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.button("CRÉER MON PROFIL DE CUISSON")
st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 0.8rem; margin-top: 80px; padding-bottom: 40px;'>© 2024 AntigaspIA - Excellence & Durabilité.</p>", unsafe_allow_html=True)
