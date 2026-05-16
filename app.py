import streamlit as st
from groq import Groq

# 1. RETOUR À LA CONFIGURATION CENTRÉE (Bloque le flottement sur iPad)
st.set_page_config(
    page_title="AntigaspIA", 
    page_icon="🍽️", 
    layout="centered", # Fixe la page au milieu sans déborder sur les côtés
    initial_sidebar_state="collapsed"
)

# 2. CSS DE VERROUILLAGE ET BLANC ABSOLU POUR L'IA
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
    
    /* BLOCAGE TOTAL DU DÉFILEMENT HORIZONTAL */
    html, body, .stApp, .block-container {
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 auto !important;
        padding-x: 10px !important;
    }

    /* Image de fond fixe */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.55), rgba(15, 23, 42, 0.8)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Nettoyage des résidus Streamlit */
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

    /* BARRE DE CONNEXION DISCRÈTE (HAUT DROITE) */
    .discreet-login-container {
        text-align: right;
        margin-bottom: 20px;
        width: 100%;
    }
    
    div[data-testid="stPopover"] {
        display: inline-block !important;
    }
    div[data-testid="stPopover"] > button {
        background-color: rgba(15, 23, 42, 0.6) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 8px !important;
        padding: 8px 16px !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
    }

    /* PANNEAU CENTRAL DE TEXTE */
    .generator-panel {
        background: rgba(30, 41, 59, 0.6) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
        width: 100% !important;
        box-sizing: border-box;
    }

    /* LE CHAMP FRIGO */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 12px !important;
        font-size: 1.15rem !important;
        font-weight: 500 !important;
    }

    /* BOUTON D'ACTION ORANGE */
    .stButton>button {
        width: 100% !important;
        border-radius: 12px !important;
        height: 60px !important;
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        text-transform: uppercase !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3) !important;
    }

    /* LE BANDEAU VERT INDICATEUR */
    .scroll-indicator {
        text-align: center;
        background: #10B981 !important;
        color: #FFFFFF !important;
        padding: 15px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.15rem;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    /* 🚨 FORCE ABSOLUE DU BLANC POUR LA GÉNÉRATION DE L'IA (INGRÉDIENTS, TITRES, TEXTES, BULLETS) 🚨 */
    .recipe-direct-display, 
    .recipe-direct-display * {
        color: #FFFFFF !important;
        color: rgb(255, 255, 255) !important;
        font-size: 1.2rem !important;
        line-height: 1.8 !important;
        background: transparent !important;
    }
    
    /* Forçage spécifique sur les listes et puces générées par le Markdown de l'IA */
    .recipe-direct-display li, 
    .recipe-direct-display ul, 
    .recipe-direct-display ol, 
    .recipe-direct-display p, 
    .recipe-direct-display strong, 
    .recipe-direct-display h1, 
    .recipe-direct-display h2, 
    .recipe-direct-display h3 {
        color: #FFFFFF !important;
    }

    /* TITRE PRINCIPAL ET MANIFESTE */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        color: #FFFFFF !important;
    }
    .pro-manifesto {
        font-size: 1.15rem;
        font-weight: 500;
        line-height: 1.6;
        text-align: center;
        margin-bottom: 35px;
        color: #FFFFFF !important;
    }
    .pro-manifesto strong {
        color: #F59E0B !important;
        font-weight: 700;
    }

    /* Forçage de sécurité global du site */
    label, p, span, h1, h2, h3, h4, h5, h6 { 
        color: #FFFFFF !important; 
    }

    .inner-auth-form {
        background-color: #0F172A !important;
        padding: 15px;
        border-radius: 10px;
    }
    .inner-auth-form input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SYSTÈME DE SESSIONS ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_mail" not in st.session_state:
    st.session_state.user_mail = ""

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Le token de connexion Groq est manquant.")
    st.stop()

# --- 4. BARRE DE CONNEXION DISCRÈTE ---
st.markdown("<div class='discreet-login-container'>", unsafe_allow_html=True)
if not st.session_state.authenticated:
    with st.popover("🔑 Connexion / Inscription pour enregistrer vos régimes !"):
        st.markdown("<div class='inner-auth-form'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:0.9rem; margin-top:0;'>Inscrivez votre e-mail pour enregistrer vos préférences :</p>", unsafe_allow_html=True)
        mail_input = st.text_input("Votre Email", placeholder="chef@exemple.com", key="discreet_mail_key")
        if st.button("Valider et Enregistrer", key="btn_discreet_submit"):
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

# --- 5. TITRE ET MANIFESTE ACCROCHEUR ---
st.markdown("<h1 class='main-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class='pro-manifesto'>
        Chaque année en France, des millions de tonnes de nourriture parfaitement saine finissent à la poubelle par simple manque d'idées. 
        Un demi-citron qui s'assèche, un reste de lardons oubliés ou trois pommes de terre cuites de la veille ne méritent pas la décharge. 
        <strong>Arrêtez définitivement de jeter vos aliments.</strong> Notre algorithme culinaire de pointe analyse instantanément vos restes isolés 
        pour concevoir des fiches recettes d'excellence, adaptées à votre frigo, ultra-économiques et simples à réaliser. 
        Sauvez votre budget mensuel, honorez le travail de nos producteurs et repensez votre façon de cuisiner au quotidien.
    </div>
""", unsafe_allow_html=True)

# --- 6. BLOC CENTRAL DE GÉNÉRATION ---
st.markdown("<div class='generator-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display, serif; font-size:1.8rem; text-align:center; font-weight:700;'>🍳 Que cache votre réfrigérateur aujourd'hui ?</h3>", unsafe_allow_html=True)

liste_ingredients = st.text_area(
    "", 
    placeholder="Inscrivez vos ingrédients ici, séparés par une virgule... (Ex: 3 patates froides, lardon, fromage râpé)", 
    height=120, 
    label_visibility="collapsed",
    key="frigo_input_ipad"
)

st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)
bouton_generer = st.button("Transformer mes restes en un festin de chef", key="btn_execute_recipe")

# --- 7. DEPLOYEMENT DE LA RÉPONSE DIRECTE DE L'IA ---
if bouton_generer:
    if not liste_ingredients:
        st.warning("Veuillez mentionner vos ingrédients.")
    else:
        with st.spinner('Création de votre fiche culinaire sur-mesure...'):
            
            prompt_systeme = (
                f"Tu es AntigaspIA. Rédige une excellente recette, claire, lisible et familiale avec ces ingrédients : {liste_ingredients}. "
                f"Structure obligatoirement avec : un titre de recette sympa, la liste des ingrédients, et les étapes de préparation. Rédige tout en français."
            )
            
            reponse_api = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt_systeme}], 
                model="llama-3.3-70b-versatile"
            )
            
            # LE BANDEAU VERT UNIQUEMENT
            st.markdown("""
                <div class='scroll-indicator'>
                    ⬇️ VOTRE RECETTE UNIQUE EST PRÊTE ! DÉCOUVREZ-LA DIRECTEMENT CI-DESSOUS ⬇️
                </div>
            """, unsafe_allow_html=True)
            
            # AFFICHAGE DE LA RECETTE EN BLANC PUR SANS BLOC NOIR NI GRIS
            st.markdown("<div class='recipe-direct-display'>", unsafe_allow_html=True)
            st.markdown(reponse_api.choices[0].message.content)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# --- 8. PIED DE PAGE ---
st.markdown("<p style='text-align:center; font-weight:700; margin-top:50px; font-size:1.1rem; color:#FFFFFF;'>Économiser intelligemment. Consommer durablement. Cuisiner élégamment.</p>", unsafe_allow_html=True)
