import streamlit as st
from groq import Groq

# 1. Configuration Pro
st.set_page_config(page_title="AntigaspIA | Haute Cuisine Circulaire", page_icon="🍽️", layout="wide")

# 2. Design "Luxe & Sobriété"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
    
    .stApp { background-color: #ffffff; font-family: 'Inter', sans-serif; }

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

    .membership-section {
        background: #f8fafc;
        padding: 60px 20px;
        margin-top: 40px;
        border-radius: 30px;
        text-align: center;
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
# Correction de la ligne qui posait problème dans image_4.png
st.markdown('<div class="action-container">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center; font-family:Playfair Display; font-size:1.8rem; margin-bottom:25px;'>Optimisez vos restes en un clic</h2>", unsafe_allow_html=True)

ingredients = st.text_area("", placeholder="Décrivez ici ce qu'il reste dans votre cuisine (ex: Dos de cabillaud, poireaux, demi-citron...)", label_visibility="collapsed", height=150)

st.markdown("<br>", unsafe_allow_html=True)
submit = st.button("LANCER L'ANALYSE CULINAIRE")

st.markdown("<p style='text-align:center; font-size:0.85rem; color:#64748b; margin-top:20px;'>Usage gratuit • Résultats basés sur la haute gastronomie</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- LOGIQUE IA ---
if submit:
    if not ingredients:
        st.warning("Veuillez fournir une liste d'ingrédients.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            with st.spinner('Génération de votre fiche recette...'):
                prompt = f"Tu es AntigaspIA, expert culinaire. Crée une recette gastronomique avec : {ingredients}."
                completion = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
                st.markdown("---")
                st.markdown("### 📋 Votre Fiche Recette")
                st.info(completion.choices[0].message.content)
                st.balloons()
        except:
            st.error("Erreur de connexion. Vérifiez votre clé API dans les secrets.")

# --- OPTIONS DE COMPTE ---
st.markdown("""
    <div class="membership-section">
        <h2 style="font-family:Playfair Display;">Allez plus loin avec AntigaspIA</h2>
        <p style="color:#64748b; margin-bottom:30px;">Créez un compte pour sauvegarder vos préférences et vos régimes (Végétarien, Keto, etc.)</p>
    </div>
    """, unsafe_allow_html=True)

col_a, col_b, col_c = st.columns([1,2,1])
with col_b:
    st.button("S'INSCRIRE GRATUITEMENT")

st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 0.8rem; margin-top: 80px; padding-bottom: 40px;'>© 2024 AntigaspIA - Excellence & Durabilité.</p>", unsafe_allow_html=True)
