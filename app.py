import streamlit as st
from groq import Groq

# 1. Configuration de la page
st.set_page_config(page_title="AntigaspIA", page_icon="🍽️", layout="wide")

# 2. CSS de Force Absolue (Anti-Gris, Anti-Bleu, Anti-Blanc)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
    /* 1. IMAGE DE FOND NETTE SANS COUCHE BLEUE */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.45), rgba(15, 23, 42, 0.7)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* 2. FORCE LA SUPPRESSION DE TOUTES LES BANDES BLEUES ET COLONNES */
    div[data-testid="stHorizontalBlock"], 
    div[data-testid="stVerticalBlock"] > div,
    .st-emotion-cache-1r6slb0, 
    .st-emotion-cache-6qobir,
    div[data-className="stSidebarUserContent"] {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* 3. INTERDICTION DU FOND BLANC SUR LE BOUTON CONNEXION (PASSAGE EN NOIR ENTIER) */
    div[data-testid="stPopover"] > button {
        background-color: #0F172A !important; /* FOND NOIR DE SÉCURITÉ */
        color: #FFFFFF !important; /* TEXTE BLANC FLASH */
        border: 2px solid #F59E0B !important; /* BORDURE ORANGE SUBTILE */
        border-radius: 10px !important;
        padding: 12px 24px !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
    }
    
    /* Évite que le bouton devienne blanc quand on clique dessus */
    div[data-testid="stPopover"] > button:focus, 
    div[data-testid="stPopover"] > button:active,
    div[data-testid="stPopover"] > button:hover {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border-color: #F59E0B !important;
    }

    /* 4. DESIGN DU PANNEAU CENTRAL EN VERRE */
    .main-glass-panel {
        background: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 40px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.7);
        max-width: 950px;
        margin: 0 auto 30px auto;
    }

    /* 5. TEXTES DU HAUT ET BAS FORCÉS EN BLANC PUR DURABLE */
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
        max-width: 850px;
        margin: 0 auto 40px auto; 
        font-weight: 600;
        line-height: 1.6;
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.95);
    }
    .footer-text {
        text-align: center; 
        color: #FFFFFF !important; 
        font-size: 1.2rem !important; 
        font-weight: 700 !important;
        margin-top: 60px; 
        text-shadow: 2px 2px 8px rgba(0,0,0,0.9);
    }

    /* 6. BOÎTE DE RÉPONSE IA NOIRE AVEC TEXTE BLANC */
    .recipe-box {
        background: #0F172A !important;
        border-left: 6px solid #F59E0B;
        padding: 35px;
        border-radius: 14px;
        margin-top: 30px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
    }
    .recipe-box, .recipe-box p, .recipe-box li, .recipe-box h1, .recipe-box h2, .recipe-box h3 {
        color: #FFFFFF !important;
        font-size: 1.15rem !important;
        line-height: 1.8 !important;
    }

    /* Inputs et Bouton d'action */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 12px !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 60px;
        background: linear-gradient(90deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border: none !important;
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.4);
    }

    .login-bar { max-width: 950px; margin: 0 auto; text-align: right; padding-top: 15px; }
    label, p, span, h3, h4 { color: #FFFFFF !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSIONS ---
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

try:
    client_groq = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Clé GROQ_API_KEY introuvable.")
    st.stop()

# --- BARRE DE CONNEXION SÉCURISÉE (HAUT DROITE - NOIR ET BLANC) ---
st.markdown("<div class='login-bar'>", unsafe_allow_html=True)
if not st.session_state.user_authenticated:
    with st.popover("🔑 Connexion / Inscription"):
        st.markdown("<p style='color:#0F172A !important; font-size:0.95rem; font-weight:700;'>Sauvegardez vos préférences pour ne plus avoir à les réécrire à chaque visite !</p>", unsafe_allow_html=True)
        email = st.text_input("Votre Email", placeholder="chef@exemple.com")
        if st.button("Valider l'accès"):
            if email:
                st.session_state.user_authenticated = True
                st.session_state.user_email = email
                st.rerun()
else:
    if st.button(f"👤 {st.session_state.user_email} (Déconnexion)"):
        st.session_state.user_authenticated = False
        st.session_state.user_email = ""
        st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# --- PRÉSENTATION DU PROJET (ANTI-GASPI) ---
st.markdown("<h1 class='brand-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("""
    <p class='brand-subtitle'>
        Chaque année, des millions de repas finissent à la poubelle par simple manque d'inspiration. 
        <b>Arrêtez définitivement de jeter les restes de votre frigo.</b> Notre système étudie vos ingrédients 
        pour concevoir instantanément des recettes sur mesure, gourmandes et ultra-économiques. Sauvez votre budget.
    </p>
""", unsafe_allow_html=True)

# --- PANNEAU DE CONTRÔLE CULINAIRE ---
st.markdown("<div class='main-glass-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display; font-size:1.8rem; text-align:center;'>🍳 Génération d'une recette délicieuse grâce à ce qu'il reste dans mon frigo !</h3>", unsafe_allow_html=True)

ingredients = st.text_area("", placeholder="Entrez vos restes ici... (Ex: 3 patates froides, un reste de lardons, un fond de crème)", height=140, label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)
submit = st.button("Transformer mes restes en festin")

# --- DESCENTE DE LA RÉPONSE IA ---
if submit:
    if not ingredients:
        st.warning("Veuillez inscrire des ingrédients présents dans votre frigo.")
    else:
        with st.spinner('Analyse et composition de votre recette...'):
            prompt = f"Tu es AntigaspIA. Rédige une excellente recette familiale, économique et claire à base de : {ingredients}. Structure avec un Titre, la liste des ingrédients, et les étapes."
            completion = client_groq.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
            
            st.markdown("<div style='text-align:center; background:#10B981; color:white; padding:14px; border-radius:10px; font-weight:700; margin-top:25px;'>✨ Votre recette personnalisée est prête ! Regardez juste en dessous.</div>", unsafe_allow_html=True)
            
            st.markdown("<div class='recipe-box'>", unsafe_allow_html=True)
            st.markdown(completion.choices[0].message.content)
            st.markdown("</div>", unsafe_allow_html=True)
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# --- TEXTE DU BAS FORCÉ EN BLANC PUR ---
st.markdown("<p class='footer-text'>Économiser intelligemment. Consommer durablement.</p>", unsafe_allow_html=True)
