import streamlit as st
from groq import Groq

# 1. FIXATION STRICTE DE L'ÉCRAN IPAD (Mode centré sans dérapage latéral)
st.set_page_config(
    page_title="AntigaspIA", 
    page_icon="🍽️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS DE FORCE SÉCURITÉ - TEXTE BLANC INTENSE & ZÉRO GLISSEMENT HORIZONTAL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
    
    /* Blocage absolu des dimensions pour éliminer le flottement de l'iPad */
    html, body, .stApp, .block-container {
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 auto !important;
    }

    /* Arrière-plan sombre filtré */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.65), rgba(15, 23, 42, 0.88)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Suppression des bordures, cadres et fonds par défaut de Streamlit */
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

    /* En-tête de connexion discret (haut droite) */
    .discreet-login-container {
        text-align: right;
        margin-bottom: 25px;
        width: 100%;
    }
    div[data-testid="stPopover"] {
        display: inline-block !important;
    }
    div[data-testid="stPopover"] > button {
        background-color: rgba(15, 23, 42, 0.75) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
        border-radius: 8px !important;
        padding: 6px 14px !important;
        font-size: 0.85rem !important;
    }

    /* Structure du panneau principal */
    .generator-panel {
        background: rgba(30, 41, 59, 0.55) !important;
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        padding: 25px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.4);
        width: 100% !important;
        box-sizing: border-box;
    }

    /* Forçage de la visibilité des options de préférence (Multi-select / Pills) */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="select"] * {
        color: #0F172A !important; /* Écrit en noir dans la boîte de choix pour voir ce qu'on tape */
    }

    /* Textarea des ingrédients */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
    }

    /* Bouton d'action orange */
    .stButton>button {
        width: 100% !important;
        border-radius: 12px !important;
        height: 55px !important;
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        border: none !important;
    }

    /* Bandeau de notification vert */
    .scroll-indicator {
        text-align: center;
        background: #10B981 !important;
        color: #FFFFFF !important;
        padding: 12px;
        border-radius: 10px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 25px;
    }

    /* 🚨 TUNNEL DE SÉCURITÉ : BLANC DE BLANC ABSOLU ET INDÉTRONISABLE POUR L'IA 🚨 */
    .recipe-pure-white-box {
        color: #FFFFFF !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1.2rem !important;
        line-height: 1.8 !important;
        background: transparent !important;
        padding: 10px 0;
    }
    .recipe-pure-white-box h2, .recipe-pure-white-box h3, .recipe-pure-white-box h1 {
        color: #FFFFFF !important;
        font-family: 'Playfair Display', serif !important;
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        margin-top: 30px !important;
        margin-bottom: 12px !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.25);
        padding-bottom: 6px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) !important;
    }
    .recipe-pure-white-box p, .recipe-pure-white-box div, .recipe-pure-white-box span {
        color: #FFFFFF !important;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.9) !important;
    }
    .recipe-pure-white-box ul, .recipe-pure-white-box ol {
        color: #FFFFFF !important;
        margin-left: 25px !important;
        padding-left: 5px !important;
    }
    .recipe-pure-white-box li {
        color: #FFFFFF !important;
        margin-bottom: 10px !important;
        font-size: 1.15rem !important;
        list-style-position: outside !important;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.9) !important;
    }
    .recipe-pure-white-box strong {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* Typographies générales du site */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        color: #FFFFFF !important;
    }
    .pro-manifesto {
        font-size: 1.15rem;
        line-height: 1.6;
        text-align: center;
        margin-bottom: 30px;
        color: #FFFFFF !important;
    }
    .pro-manifesto strong {
        color: #F59E0B !important;
    }

    label, p, span, h4, h5 { color: #FFFFFF !important; }

    .inner-auth-form {
        background-color: #0F172A !important;
        padding: 10px;
        border-radius: 8px;
    }
    .inner-auth-form input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. INITIALISATION DES SESSIONS ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_mail" not in st.session_state:
    st.session_state.user_mail = ""

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Clé d'API Groq introuvable.")
    st.stop()

# --- 4. BARRE DE CONNEXION POP-OVER HAUT DROITE ---
st.markdown("<div class='discreet-login-container'>", unsafe_allow_html=True)
if not st.session_state.authenticated:
    with st.popover("🔑 Connexion / Inscription pour enregistrer vos régimes !"):
        st.markdown("<div class='inner-auth-form'>", unsafe_allow_html=True)
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

# --- 5. TITRE & MANIFESTE SÉCURISÉ ---
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

# --- 6. BLOC PRINCIPAL DE CONFIGURATION ---
st.markdown("<div class='generator-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display, serif; font-size:1.6rem; text-align:center; font-weight:700; color:#FFF;'>🍳 Que cache votre réfrigérateur aujourd'hui ?</h3>", unsafe_allow_html=True)

# Saisie des aliments
liste_ingredients = st.text_area(
    "", 
    placeholder="Inscrivez vos ingrédients ici, séparés par une virgule... (Ex: veau, patates, carottes)", 
    height=100, 
    label_visibility="collapsed",
    key="frigo_input_ipad"
)

# NOUVEAU MODULE : SÉLECTION DES PRÉFÉRENCES ET RÉGIMES ALIMENTAIRES
st.markdown("<p style='margin-top:15px; font-weight:700; font-size:1.05rem; color:#FFFFFF;'>🥗 Adapter la recette à vos objectifs & régimes :</p>", unsafe_allow_html=True)
options_regimes = st.multiselect(
    "Options de préférences",
    options=[
        "Aucun filtre particulier", "Végétarien", "Vegan / Végétalien", 
        "Sportif (Riche en protéines)", "Sans Gluten", "Sans Lactose", 
        "Faible en calories (Minceur)", "Format Familial (Enfants)", "Rapide (- de 15 min)"
    ],
    default=["Aucun filtre particulier"],
    label_visibility="collapsed"
)

st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)
bouton_generer = st.button("Transformer mes restes en un festin de chef", key="btn_execute_recipe")

# --- 7. APEL API ET SÉCURISATION HTML CONTRE SAFARI IPAD ---
if bouton_generer:
    if not liste_ingredients:
        st.warning("Veuillez renseigner au moins un ingrédient.")
    else:
        with st.spinner('Création de votre fiche culinaire sur-mesure...'):
            
            # Construction du filtre texte basé sur les puces sélectionnées
            filtre_texte = ", ".join(options_regimes)
            
            # Directive ultra-stricte : pas de markdown, uniquement des balises HTML standards
            prompt_systeme = (
                f"Tu es AntigaspIA, un chef d'excellence. Rédige une recette gastronomique avec ces ingrédients : {liste_ingredients}. "
                f"Contrainte majeure : Tu dois impérativement respecter les régimes et préférences suivants : {filtre_texte}. "
                f"Tu dois obligatoirement rédiger ta réponse exclusivement en HTML brut (pas de blocs markdown, pas de ```html). "
                f"Utilise uniquement des balises <h2> pour les titres, des balises <ul> et <li> pour les listes d'ingrédients, "
                f"et des balises <ol> et <li> pour décrire précisément les étapes de préparation. Tout le texte doit être en français."
            )
            
            reponse_api = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt_systeme}], 
                model="llama-3.3-70b-versatile"
            )
            
            # Affichage du bandeau vert uniquement
            st.markdown("""
                <div class='scroll-indicator'>
                    ⬇️ VOTRE RECETTE UNIQUE EST PRÊTE ! DÉCOUVREZ-LA DIRECTEMENT CI-DESSOUS ⬇️
                </div>
            """, unsafe_allow_html=True)
            
            # Injection de la structure HTML directement sur le fond d'écran dans le tunnel blanc
            contenu_recette = reponse_api.choices[0].message.content
            st.markdown(f"""
                <div class='recipe-pure-white-box'>
                    {contenu_recette}
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# --- 8. PIED DE PAGE ---
st.markdown("<p style='text-align:center; font-weight:700; margin-top:40px; font-size:1rem; color:#FFFFFF;'>Économiser intelligemment. Consommer durablement. Cuisiner élégamment.</p>", unsafe_allow_html=True)
