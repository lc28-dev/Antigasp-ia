import streamlit as st
from groq import Groq

# 1. VERROUILLAGE STRICT DE L'ÉCRAN IPAD
st.set_page_config(
    page_title="AntigaspIA", 
    page_icon="🍽️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. INJECTION DIRECTE DU CODE ADSENSE DANS LE HEAD POUR LE ROBOT GOOGLE
# Cette méthode injecte le script directement à la racine pour que Google valide instantanément le site.
st.markdown(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1756718492717210"
     crossorigin="anonymous"></script>
    """,
    unsafe_allow_html=True
)

# 3. LE BLINDAGE CSS GLOBAL : FORCE DU BLANC ET FIXATION DE L'ÉCRAN
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
    
    /* Blocage absolu des dimensions pour éliminer les glissements et débordements sur iPad */
    html, body, .stApp, .block-container {
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 auto !important;
    }

    /* Arrière-plan filtré sombre */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.7), rgba(15, 23, 42, 0.9)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Nettoyage radical des structures de Streamlit (Plus de blocs gris ou noirs) */
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

    /* 🚨 LE MARTEAU PILON CSS : TOUT TEXTE DU SITE DEVIENT BLANC AVEC OMBRE PORTÉE NOIRE 🚨 */
    /* Cela s'applique aux paragraphes, listes, titres, numéros, textes générés ou écrits à la main */
    p, span, label, li, ul, ol, h1, h2, h3, h4, h5, h6, strong, div {
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.95), -1px -1px 0 rgba(0,0,0,0.95), 1px -1px 0 rgba(0,0,0,0.95), -1px 1px 0 rgba(0,0,0,0.95), 1px 1px 0 rgba(0,0,0,0.95) !important;
    }

    /* Zone de Connexion discrète en haut à droite */
    .discreet-login-container {
        text-align: right;
        margin-bottom: 25px;
        width: 100%;
    }
    div[data-testid="stPopover"] {
        display: inline-block !important;
    }
    div[data-testid="stPopover"] > button {
        background-color: rgba(15, 23, 42, 0.8) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 8px !important;
        padding: 6px 14px !important;
    }

    /* Panneau central translucide */
    .generator-panel {
        background: rgba(30, 41, 59, 0.45) !important;
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        padding: 25px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.5);
        width: 100% !important;
        box-sizing: border-box;
    }

    /* Le sélecteur de régimes (On force l'écriture interne en noir uniquement pendant la frappe) */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="select"] span, div[data-baseweb="select"] div {
        color: #0F172A !important;
        text-shadow: none !important;
    }

    /* Zone de texte des ingrédients */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
        text-shadow: none !important;
    }
    .stTextArea textarea span, .stTextArea textarea div {
        color: #0F172A !important;
        text-shadow: none !important;
    }

    /* Bouton d'action orange vif */
    .stButton>button {
        width: 100% !important;
        border-radius: 12px !important;
        height: 55px !important;
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        border: none !important;
        text-shadow: none !important;
    }
    .stButton>button span {
        color: #0F172A !important;
        text-shadow: none !important;
    }

    /* Bandeau vert */
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

    /* Conteneur de la recette générée */
    .recipe-output-box {
        margin-top: 20px;
        padding: 15px 0;
        font-size: 1.2rem !important;
        line-height: 1.85 !important;
    }
    .recipe-output-box h2 {
        font-family: 'Playfair Display', serif !important;
        font-size: 1.9rem !important;
        margin-top: 25px !important;
        border-bottom: 2px solid rgba(255,255,255,0.3);
        padding-bottom: 5px;
    }
    .recipe-output-box li {
        margin-left: 20px !important;
        list-style-position: outside !important;
    }

    /* Styles des titres d'accueil */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
    }
    .pro-manifesto {
        font-size: 1.15rem;
        line-height: 1.6;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Fenêtre pop-over de connexion */
    .inner-auth-form {
        background-color: #0F172A !important;
        padding: 10px;
        border-radius: 8px;
    }
    .inner-auth-form input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
    }
    .inner-auth-form input span {
        color: #0F172A !important;
        text-shadow: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. GESTION DES SESSIONS ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_mail" not in st.session_state:
    st.session_state.user_mail = ""

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Clé API Groq manquante dans les secrets.")
    st.stop()

# --- 5. COMPOSANT CONNEXION PREMIUM HAUT DROITE ---
st.markdown("<div class='discreet-login-container'>", unsafe_allow_html=True)
if not st.session_state.authenticated:
    with st.popover("🔑 Connexion / Inscription"):
        st.markdown("<div class='inner-auth-form'>", unsafe_allow_html=True)
        mail_input = st.text_input("Votre Email", placeholder="chef@exemple.com", key="discreet_mail_key")
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

# --- 6. ACCUEIL ET TEXTES ---
st.markdown("<h1 class='main-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class='pro-manifesto'>
        Chaque année en France, des millions de tonnes de nourriture parfaitement saine finissent à la poubelle par simple manque d'idées. 
        Un demi-citron qui s'assèche, un reste de lardons oubliés ou trois pommes de terre cuites de la veille ne méritent pas la décharge. 
        Arrêtez définitivement de jeter vos aliments. Notre algorithme culinaire de pointe analyse instantanément vos restes isolés 
        pour concevoir des fiches recettes d'excellence, adaptées à votre frigo, ultra-économiques et simples à réaliser.
    </div>
""", unsafe_allow_html=True)

# --- 7. ZONE DE TRAVAIL PRINCIPALE ---
st.markdown("<div class='generator-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display, serif; font-size:1.6rem; text-align:center; font-weight:700;'>🍳 Que cache votre réfrigérateur aujourd'hui ?</h3>", unsafe_allow_html=True)

# Saisie des ingrédients
liste_ingredients = st.text_area(
    "", 
    placeholder="Inscrivez vos ingrédients ici, séparés par une virgule... (Ex: veau, patates, carottes)", 
    height=100, 
    label_visibility="collapsed",
    key="frigo_input_ipad"
)

# Choix du profil et régime alimentaire
st.markdown("<p style='margin-top:15px; font-weight:700; font-size:1.05rem;'>🥗 Adapter la recette à vos objectifs & régimes :</p>", unsafe_allow_html=True)
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

# --- 8. TRAITEMENT ET AFFICHAGE IMPÉRIAL ---
if bouton_generer:
    if not liste_ingredients:
        st.warning("Veuillez ajouter des ingrédients.")
    else:
        with st.spinner('Création de votre fiche culinaire sur-mesure...'):
            
            filtre_texte = ", ".join(options_regimes)
            
            # Ordre strict : génération en HTML brut
            prompt_systeme = (
                f"Tu es AntigaspIA, un chef d'excellence. Rédige une recette gastronomique avec ces ingrédients : {liste_ingredients}. "
                f"Contrainte majeure : Tu dois impérativement respecter les régimes et préférences suivants : {filtre_texte}. "
                f"Tu dois obligatoirement rédiger ta réponse exclusivement en HTML brut (sans aucun bloc markdown, pas de ```html). "
                f"Utilise uniquement des balises <h2> pour les grands titres, des balises <ul> et <li> pour les listes d'ingrédients, "
                f"et des balises <ol> et <li> pour décrire précisément les étapes de préparation. Tout le texte doit être en français."
            )
            
            reponse_api = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt_systeme}], 
                model="llama-3.3-70b-versatile"
            )
            
            st.markdown("""
                <div class='scroll-indicator'>
                    ⬇️ VOTRE RECETTE UNIQUE EST PRÊTE ! DÉCOUVREZ-LA DIRECTEMENT CI-DESSOUS ⬇️
                </div>
            """, unsafe_allow_html=True)
            
            # Affichage dans la zone sécurisée blanche
            contenu_recette = reponse_api.choices[0].message.content
            st.markdown(f"""
                <div class='recipe-output-box'>
                    {contenu_recette}
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# --- 9. PIED DE PAGE ---
st.markdown("<p style='text-align:center; font-weight:700; margin-top:40px; font-size:1rem;'>Économiser intelligemment. Consommer durablement. Cuisiner élégamment.</p>", unsafe_allow_html=True)
