import streamlit as st
from groq import Groq
import os

# ==============================================================================
# 📐 CONFIGURATION ET INJECTION DU CODE DE VALIDATION ADSENSE
# ==============================================================================
st.set_page_config(
    page_title="AntigaspIA", 
    page_icon="🍽️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Injection officielle du script AdSense pour que le robot le trouve immédiatement
# Peu importe la page ou l'aperçu qu'AdSense essaie de charger.
st.html("""
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1756718492717210" crossorigin="anonymous"></script>
""")

# ==============================================================================
# 🎨 DESIGN CSS AVANCÉ : RENDU RETINA POUR IPAD
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=400;500;600;700;800&family=Playfair+Display:wght=700;800&display=swap');
    
    html, body, .stApp, .block-container {
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 auto !important;
    }

    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.72), rgba(15, 23, 42, 0.93)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    div[data-testid="stHorizontalBlock"], 
    div[data-testid="stVerticalBlock"] > div,
    .st-emotion-cache-1r6slb0, 
    .st-emotion-cache-6qobir,
    div[data-testid="stHeader"] {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    .discreet-login-container {
        text-align: right;
        margin-bottom: 25px;
        width: 100%;
    }
    div[data-testid="stPopover"] {
        display: inline-block !important;
    }
    div[data-testid="stPopover"] > button {
        background-color: rgba(30, 41, 59, 0.85) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
        border-radius: 10px !important;
        padding: 8px 16px !important;
        font-weight: 600 !important;
    }

    .generator-panel {
        background: rgba(30, 41, 59, 0.65) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 30px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        width: 100% !important;
        box-sizing: border-box;
        margin-bottom: 30px;
    }

    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="select"] * {
        color: #0F172A !important;
        font-weight: 500 !important;
    }

    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 14px !important;
        font-size: 1.1rem !important;
        padding: 15px !important;
    }

    .stButton>button {
        width: 100% !important;
        border-radius: 14px !important;
        height: 58px !important;
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(217, 119, 6, 0.35) !important;
    }

    .scroll-indicator {
        text-align: center;
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: #FFFFFF !important;
        padding: 15px;
        border-radius: 12px;
        font-weight: 800;
        margin-top: 25px;
        margin-bottom: 25px;
        box-shadow: 0 6px 15px rgba(16, 185, 129, 0.2);
    }

    .recipe-display-container {
        background: rgba(15, 23, 42, 0.88) !important;
        border: 2px solid rgba(255, 255, 255, 0.25);
        border-radius: 24px;
        padding: 35px;
        margin-top: 30px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
    }
    
    .recipe-display-container,
    .recipe-display-container h1,
    .recipe-display-container h2,
    .recipe-display-container h3,
    .recipe-display-container p,
    .recipe-display-container li,
    .recipe-display-container ul,
    .recipe-display-container ol,
    .recipe-display-container span,
    .recipe-display-container strong {
        color: #FFFFFF !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8) !important;
    }

    .recipe-display-container h2, .recipe-display-container h3 {
        font-family: 'Playfair Display', serif !important;
        font-size: 2.1rem !important;
        font-weight: 800 !important;
        margin-top: 32px !important;
        margin-bottom: 16px !important;
        border-bottom: 2px solid rgba(245, 158, 11, 0.4) !important;
        padding-bottom: 8px !important;
        color: #F59E0B !important;
    }

    .recipe-display-container p, .recipe-display-container li {
        font-size: 1.2rem !important;
        line-height: 1.85 !important;
        font-weight: 500 !important;
    }

    .recipe-display-container ul, .recipe-display-container ol {
        margin-left: 25px !important;
        padding-left: 5px !important;
    }

    .recipe-display-container li {
        margin-bottom: 12px !important;
        list-style-position: outside !important;
    }

    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.6rem;
        font-weight: 800;
        text-align: center;
        color: #FFFFFF !important;
        margin-bottom: 10px;
    }
    
    .pro-manifesto {
        font-size: 1.15rem;
        line-height: 1.6;
        text-align: center;
        margin-bottom: 35px;
        color: rgba(255, 255, 255, 0.9) !important;
    }
    
    .pro-manifesto strong { color: #F59E0B !important; }
    label, p, span, h4, h5 { color: #FFFFFF !important; }
    .inner-auth-form { background-color: #0F172A !important; padding: 15px; border-radius: 12px; }
    .inner-auth-form input { background-color: #FFFFFF !important; color: #0F172A !important; }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 💾 GESTION DES SESSIONS
# ==============================================================================
if "authenticated" not in st.session_state: st.session_state.authenticated = False
if "user_mail" not in st.session_state: st.session_state.user_mail = ""

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("Erreur d'API Groq manquante.")
    st.stop()

# Connexion Popover
st.markdown("<div class='discreet-login-container'>", unsafe_allow_html=True)
if not st.session_state.authenticated:
    with st.popover("🔑 Connexion / Inscription"):
        st.markdown("<div class='inner-auth-form'>", unsafe_allow_html=True)
        mail_input = st.text_input("Votre adresse Email", placeholder="chef@exemple.com", key="discreet_mail_key")
        if st.button("Se connecter", key="btn_discreet_submit"):
            if mail_input:
                st.session_state.authenticated = True
                st.session_state.user_mail = mail_input
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    if st.button(f"👤 {st.session_state.user_mail} (Déconnexion)", key="btn_discreet_logout"):
        st.session_state.authenticated = False
        st.session_state.user_mail = ""
        st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# Titre
st.markdown("<h1 class='main-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("<div class='pro-manifesto'><strong>Arrêtez définitivement de jeter vos aliments.</strong> Notre intelligence artificielle culinaire analyse instantanément vos restes.</div>", unsafe_allow_html=True)

# Formulaire
st.markdown("<div class='generator-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; text-align:center; color:#FFF;'>🍳 Quels ingrédients reste-t-il dans votre frigo ?</h3>", unsafe_allow_html=True)

liste_ingredients = st.text_area("", placeholder="Inscrivez vos ingrédients...", height=110, label_visibility="collapsed", key="frigo_input_ipad")

bouton_generer = st.button("Transformer mes restes en un festin de chef", key="btn_execute_recipe")

if bouton_generer:
    if not liste_ingredients:
        st.warning("Veuillez renseigner au moins un ingrédient.")
    else:
        with st.spinner('Création de votre fiche culinaire...'):
            prompt_systeme = f"Tu es AntigaspIA. Rédige une recette à partir de : {liste_ingredients}. Formate exclusivement en HTML brut (sans blocs de code markdown ```html). Utilise <h2>, <ul>, <li>."
            reponse_api = client.chat.completions.create(messages=[{"role": "user", "content": prompt_systeme}], model="llama-3.3-70b-versatile")
            
            st.markdown("<div class='scroll-indicator'>⬇️ RECETTE PRÊTE CI-DESSOUS ⬇️</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='recipe-display-container'>{reponse_api.choices[0].message.content}</div>", unsafe_allow_html=True)
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)
