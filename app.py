import streamlit as st
from groq import Groq

# 1. Configuration de la page
st.set_page_config(page_title="AntigaspIA", page_icon="🍽️", layout="wide")

# 2. CSS de Force Absolue (Pas de bandes bleues, pas de fond blanc, lisibilité max)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
    /* Image de fond principale nettoyée */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.5), rgba(15, 23, 42, 0.75)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* NETTOYAGE RADICAL DES ANCIENNES BANDES BLEUES DE STREAMLIT */
    div[data-testid="stHorizontalBlock"], 
    div[data-testid="stVerticalBlock"] > div,
    .st-emotion-cache-1r6slb0, 
    .st-emotion-cache-6qobir {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Grand bloc central en verre transparent */
    .main-glass-panel {
        background: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 40px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.6);
        max-width: 800px;
        margin: 0 auto 30px auto;
    }

    /* Petit bloc interne pour séparer proprement la zone connexion */
    .auth-section {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px dashed rgba(255, 255, 255, 0.2);
        padding: 25px;
        border-radius: 16px;
        margin-top: 40px;
    }

    /* Titres en Blanc Lumineux Porté */
    .brand-title { 
        font-family: 'Playfair Display', serif; 
        font-size: 4.5rem; 
        text-align: center; 
        margin-top: 20px; 
        color: #FFFFFF !important; 
        text-shadow: 3px 3px 15px rgba(0, 0, 0, 0.95);
        font-weight: 800;
    }
    .brand-subtitle { 
        text-align: center; 
        color: #FFFFFF !important; 
        font-size: 1.3rem; 
        max-width: 800px;
        margin: 0 auto 40px auto; 
        font-weight: 500;
        line-height: 1.6;
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.95);
    }

    /* Zone de réponse de l'IA (Texte Blanc sur fond Sombre Protecteur) */
    .recipe-box {
        background: #0F172A !important;
        border-left: 6px solid #F59E0B;
        padding: 35px;
        border-radius: 14px;
        margin-top: 30px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
    }
    .recipe-box, .recipe-box p, .recipe-box li, .recipe-box h1, .recipe-box h2, .recipe-box h3, .recipe-box span {
        color: #FFFFFF !important;
        font-size: 1.15rem !important;
        line-height: 1.8 !important;
    }

    /* Inputs de texte (Frigo et email) */
    .stTextArea textarea, .stTextInput input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 12px !important;
        font-weight: 500 !important;
    }

    /* Bouton d'action principal Orange */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 55px;
        background: linear-gradient(90deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border: none !important;
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.3);
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        transform: translateY(-1px);
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.5);
    }

    /* Bouton de validation de connexion gris foncé */
    div.auth-section .stButton>button {
        background: #1E293B !important;
        color: #FFFFFF !important;
        height: 45px;
        font-size: 0.95rem;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }

    /* Forçage de tous les labels en Blanc */
    label, p, span, h3, h4, .footer-text { color: #FFFFFF !important; text-shadow: 1px 1px 4px rgba(0,0,0,0.4); }
    
    .footer-text {
        text-align: center; 
        font-size: 1.2rem !important; 
        font-weight: 700 !important;
        margin-top: 60px; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONFIGURATION DES SESSIONS ---
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

try:
    client_groq = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Clé GROQ_API_KEY introuvable dans vos Secrets Streamlit.")
    st.stop()

# --- PRÉSENTATION CONCEPT (SANS IA, MARKETING PRO) ---
st.markdown("<h1 class='brand-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("""
    <p class='brand-subtitle'>
        Chaque année, des millions de repas finissent à la poubelle par simple manque d'inspiration. 
        <b>Arrêtez définitivement de jeter les restes de votre frigo.</b> Notre système étudie vos produits 
        pour concevoir instantanément des fiches recettes sur mesure, gourmandes et ultra-économiques. Sauvez votre budget.
    </p>
""", unsafe_allow_html=True)

# --- PANNEAU UNIQUE CENTRAL ---
st.markdown("<div class='main-glass-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display; font-size:1.8rem; text-align:center;'>🍳 Génération d'une recette délicieuse grâce à ce qu'il reste dans mon frigo !</h3>", unsafe_allow_html=True)

# Zone de texte principale (Frigo)
ingredients = st.text_area("Vos ingrédients restants :", placeholder="Ex: 3 patates froides, un reste de lardons, un fond de crème liquide...", height=130, label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)
submit = st.button("Transformer mes restes en festin")

# --- TRAITEMENT ET ESSAI DIRECT ---
if submit:
    if not ingredients:
        st.warning("Veuillez inscrire des ingrédients présents dans votre frigo.")
    else:
        with st.spinner('Analyse et composition de votre recette...'):
            prompt = f"Tu es AntigaspIA. Rédige une excellente recette familiale, économique et claire à base de : {ingredients}. Structure avec un Titre accrocheur, la liste des ingrédients, et les étapes."
            completion = client_groq.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
            
            st.markdown("<div style='text-align:center; background:#10B981; color:white; padding:14px; border-radius:10px; font-weight:700; margin-top:25px;'>✨ Votre recette personnalisée est prête ! Découvrez-la ci-dessous.</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='recipe-box'>", unsafe_allow_html=True)
            st.markdown(completion.choices[0].message.content)
            st.markdown("</div>", unsafe_allow_html=True)
            st.balloons()

# --- ZONE D'INSCRIPTION / CONNEXION DIRECTEMENT INTÉGRÉE (TOUT EN BAS DU BLOC) ---
st.markdown("<div class='auth-section'>", unsafe_allow_html=True)
if not st.session_state.user_authenticated:
    st.markdown("<h4 style='margin-top:0; font-size:1.2rem; font-family:Playfair Display;'>🔐 Connecte-toi pour sauver tes préférences</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:0.95rem; margin-bottom:15px; opacity:0.9;'>Ajoute ton email pour que tes futurs réglages soient sauvegardés automatiquement à chaque visite (plus besoin de les repréciser !).</p>", unsafe_allow_html=True)
    
    email_user = st.text_input("Adresse e-mail :", placeholder="chef@exemple.com", key="main_auth_email")
    
    if st.button("S'identifier / S'inscrire", key="main_auth_submit"):
        if email_user:
            st.session_state.user_authenticated = True
            st.session_state.user_email = email_user
            st.rerun()
else:
    st.markdown(f"<p style='color:#10B981 !important; font-weight:700; margin-top:0;'>● Compte connecté : {st.session_state.user_email}</p>", unsafe_allow_html=True)
    if st.button("Se déconnecter", key="main_auth_logout"):
        st.session_state.user_authenticated = False
        st.session_state.user_email = ""
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True) # Fin auth-section
st.markdown("</div>", unsafe_allow_html=True) # Fin main-glass-panel

# --- TEXTE DU BAS FORCÉ EN BLANC ---
st.markdown("<p class='footer-text'>Économiser intelligemment. Consommer durablement.</p>", unsafe_allow_html=True)
