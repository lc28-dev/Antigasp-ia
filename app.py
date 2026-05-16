import streamlit as st
from groq import Groq
import os
import re

# 1. FIXATION STRICTE DE L'ÉCRAN IPAD (Mode centré sans dérapage latéral)
st.set_page_config(
    page_title="AntigaspIA", 
    page_icon="🍽️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. PATCH SUPRÊME ADSENSE : Injection chirurgicale dans le vrai 'index.html' du serveur
def injecter_adsense_dans_le_coeur():
    try:
        # Localisation du fichier index.html natif de la bibliothèque Streamlit installée sur le serveur
        import streamlit.web.cli as cli
        streamlit_dir = os.path.dirname(st.__file__)
        index_path = os.path.join(streamlit_dir, "static", "index.html")
        
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                html_content = f.read()
            
            code_adsense = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1756718492717210" crossorigin="anonymous"></script>'
            
            # Si le code n'est pas déjà présent dans le Head, on l'injecte de force juste avant </head>
            if "ca-pub-1756718492717210" not in html_content:
                modified_html = html_content.replace("</head>", f"{code_adsense}</head>")
                with open(index_path, "w", encoding="utf-8") as f:
                    f.write(modified_html)
    except Exception as e:
        # Évite de bloquer l'application en cas de restriction de droits d'écriture
        pass

# Exécution immédiate du patch au démarrage de la page
injecter_adsense_dans_le_coeur()

# 3. CSS DE FORCE MAXIMALE - RENDU TEXTE BLANC ET INTEGRATION IPAD RETINA
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
    
    /* Blocage absolu des dimensions pour éliminer le flottement latéral de l'iPad */
    html, body, .stApp, .block-container {
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 auto !important;
    }

    /* Arrière-plan sombre filtré d'excellence */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.7), rgba(15, 23, 42, 0.9)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Nettoyage complet des structures par défaut de Streamlit */
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

    /* En-tête de connexion popover aligné à droite */
    .discreet-login-container {
        text-align: right;
        margin-bottom: 25px;
        width: 100%;
    }
    div[data-testid="stPopover"] {
        display: inline-block !important;
    }
    div[data-testid="stPopover"] > button {
        background-color: rgba(30, 41, 59, 0.8) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 10px !important;
        padding: 8px 16px !important;
        font-weight: 600 !important;
    }

    /* Panneau de contrôle principal (Zone formulaire) */
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

    /* Forçage de la visibilité pour le sélecteur multi-choix (Écriture noire sur fond blanc obligatoire) */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="select"] * {
        color: #0F172A !important;
        font-weight: 500 !important;
    }

    /* Zone de texte de saisie des ingrédients */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 14px !important;
        font-size: 1.1rem !important;
        padding: 15px !important;
    }

    /* Grand bouton d'action orange cuit */
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
        box-shadow: 0 8px 20px rgba(217, 119, 6, 0.3) !important;
        transition: all 0.2s ease;
    }

    /* Alerte verte de succès */
    .scroll-indicator {
        text-align: center;
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: #FFFFFF !important;
        padding: 15px;
        border-radius: 12px;
        font-weight: 800;
        margin-top: 25px;
        margin-bottom: 25px;
        letter-spacing: 0.5px;
        box-shadow: 0 6px 15px rgba(16, 185, 129, 0.2);
    }

    /* 🛡️ BOÎTE DE RENDU BLANC ABSOLU - CONTRE-ATTAQUE CONTRE LE GRIS DE SAFARI 🛡️ */
    .recipe-display-container {
        background: rgba(15, 23, 42, 0.85) !important;
        border: 2px solid rgba(255, 255, 255, 0.2);
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
        color: rgb(255, 255, 255) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    .recipe-display-container h2, .recipe-display-container h3 {
        font-family: 'Playfair Display', serif !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
        margin-top: 30px !important;
        margin-bottom: 15px !important;
        border-bottom: 2px solid rgba(255, 255, 255, 0.25) !important;
        padding-bottom: 8px !important;
        color: #F59E0B !important; /* Donne une touche de couleur dorée aux sous-titres de la recette */
    }

    .recipe-display-container p, .recipe-display-container li {
        font-size: 1.2rem !important;
        line-height: 1.8 !important;
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

    /* Éléments textuels fixes de l'application */
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
    .pro-manifesto strong {
        color: #F59E0B !important;
    }

    label, p, span, h4, h5 { color: #FFFFFF !important; }

    .inner-auth-form {
        background-color: #0F172A !important;
        padding: 15px;
        border-radius: 12px;
    }
    .inner-auth-form input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. CONFIGURATION DES SESSIONS SÉCURISÉES ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_mail" not in st.session_state:
    st.session_state.user_mail = ""

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Clé d'API Groq introuvable dans l'espace Secrets.")
    st.stop()

# --- 5. EN-TÊTE COMPTE UTILISATEUR (POP-OVER RETINA) ---
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

# --- 6. IDENTITÉ VISUELLE ET PRO-MANIFESTO ---
st.markdown("<h1 class='main-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class='pro-manifesto'>
        Chaque année en France, des millions de tonnes de nourriture parfaitement saine finissent à la poubelle par simple manque d'idées. 
        <strong>Arrêtez définitivement de jeter vos aliments.</strong> Notre intelligence artificielle culinaire analyse instantanément vos restes 
        pour concevoir des fiches recettes sur-mesure, adaptées à votre frigo, saines et économiques.
    </div>
""", unsafe_allow_html=True)

# --- 7. BLOC PANNEAU DE CONFIGURATION ---
st.markdown("<div class='generator-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display, serif; font-size:1.6rem; text-align:center; font-weight:700; color:#FFF;'>🍳 Quels ingrédients reste-t-il dans votre frigo ?</h3>", unsafe_allow_html=True)

# Zone de saisie principale des restes
liste_ingredients = st.text_area(
    "", 
    placeholder="Inscrivez vos ingrédients ici, séparés par une virgule... (Ex: restes de poulet, crème, champignons)", 
    height=110, 
    label_visibility="collapsed",
    key="frigo_input_ipad"
)

# Configuration dynamique des profils diététiques
st.markdown("<p style='margin-top:18px; font-weight:700; font-size:1.1rem; color:#FFFFFF;'>🥗 Adapter la recette à votre profil et objectif :</p>", unsafe_allow_html=True)
options_regimes = st.multiselect(
    "Options de préférences",
    options=[
        "Aucun filtre particulier", "Végétarien", "Vegan / Végétalien", 
        "Sportif (Riche en protéines)", "Sans Gluten", "Sans Lactose", 
        "Faible en calories (Minceur)", "Format Familial (Pour les enfants)", "Recette Express (- de 15 min)"
    ],
    default=["Aucun filtre particulier"],
    label_visibility="collapsed"
)

st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)
bouton_generer = st.button("Transformer mes restes en un festin de chef", key="btn_execute_recipe")

# --- 8. TRAITEMENT API ET INJECTION DU CONTENU ---
if bouton_generer:
    if not liste_ingredients:
        st.warning("Veuillez renseigner au moins un ingrédient pour lancer la recherche.")
    else:
        with st.spinner('Création de votre fiche culinaire sur-mesure...'):
            
            filtre_texte = ", ".join(options_regimes)
            
            # Ordre strict interdisant le markdown pour forcer le respect du CSS blanc
            prompt_systeme = (
                f"Tu es AntigaspIA, un chef étoilé expert en éco-cuisine. Rédige une recette à partir de ces ingrédients : {liste_ingredients}. "
                f"Contrainte absolue : Tu dois adapter la recette selon ces préférences : {filtre_texte}. "
                f"Tu dois obligatoirement formater ta réponse exclusivement en HTML brut (sans blocs de code markdown, pas de ```html). "
                f"Utilise des balises <h2> pour le titre de la recette et les titres de rubriques (Ingrédients, Préparation), des balises <ul> et <li> pour la liste des ingrédients, "
                f"et des balises <ol> et <li> pour les étapes de préparation étape par étape. Écris tout en français."
            )
            
            reponse_api = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt_systeme}], 
                model="llama-3.3-70b-versatile"
            )
            
            st.markdown("""
                <div class='scroll-indicator'>
                    ⬇️ VOTRE RECETTE PERSONNALISÉE EST PRÊTE CI-DESSOUS ⬇️
                </div>
            """, unsafe_allow_html=True)
            
            # Affichage sécurisé dans le panneau rétroéclairé sombre (le texte ressort obligatoirement en blanc brillant)
            contenu_recette = reponse_api.choices[0].message.content
            st.markdown(f"""
                <div class='recipe-display-container'>
                    {contenu_recette}
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# --- 9. PIED DE PAGE ---
st.markdown("<p style='text-align:center; font-weight:700; margin-top:40px; font-size:1rem; color:#FFFFFF;'>Économiser intelligemment. Consommer durablement. Cuisiner élégamment.</p>", unsafe_allow_html=True)
