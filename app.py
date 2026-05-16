import streamlit as st
from groq import Groq
import os

# ==============================================================================
# 🚨 ÉTAPE DÉCISIVE : INTERCEPTION ET RE-ROUTAGE DU ROBOT GOOGLE ADSENSE (ads.txt)
# ==============================================================================
# Ce bloc s'exécute avant tout le reste. Si quelqu'un ou le robot de Google tente
# d'accéder à une page spéciale "ads.txt", on intercepte sa requête immédiatement.

try:
    # Récupération des paramètres d'URL de manière moderne sur Streamlit
    parametres_url = st.query_params
    
    # Si le robot cherche à lire le fichier de validation publicitaire via l'URL
    if "page" in parametres_url and parametres_url["page"] == "ads.txt":
        st.text("google.com, pub-1756718492717210, DIRECT, f08c47fec0942fa0")
        st.stop() # On arrête l'exécution ici pour ne lui envoyer QUE le texte brut approuvé
except Exception as e:
    # Sécurité pour éviter de planter l'application si les query_params échouent
    pass

# ==============================================================================
# 📐 CONFIGURATION ET CADRAGE RETINA POUR IPAD (Évite les dérapages latéraux)
# ==============================================================================
st.set_page_config(
    page_title="AntigaspIA", 
    page_icon="🍽️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 🎨 DESIGN CSS AVANCÉ : ADAPTATION RETINA IPAD & RENDU BLANC ABSOLU ANTI-GRIS
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
    
    /* Verrouillage des dimensions pour empêcher Safari sur iPad de glisser vers la droite */
    html, body, .stApp, .block-container {
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 auto !important;
    }

    /* Arrière-plan thématique haut de gamme */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.72), rgba(15, 23, 42, 0.93)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Nettoyage des bordures blanches et grises natives de Streamlit */
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

    /* Alignement et design du bouton d'authentification */
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

    /* Panneau de saisie central transparent */
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

    /* Forçage de lisibilité pour le menu des préférences (Texte noir sur fond blanc) */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="select"] * {
        color: #0F172A !important;
        font-weight: 500 !important;
    }

    /* Zone d'écriture des ingrédients */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 14px !important;
        font-size: 1.1rem !important;
        padding: 15px !important;
    }

    /* Bouton principal orange vibrant */
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

    /* Bandeau de notification de recette */
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

    /* 🛡️ STRUCTURE OPALE CONTRE LE TEXTE GRIS DE SAFARI SUR IPAD 🛡️ */
    .recipe-display-container {
        background: rgba(15, 23, 42, 0.88) !important;
        border: 2px solid rgba(255, 255, 255, 0.25);
        border-radius: 24px;
        padding: 35px;
        margin-top: 30px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
    }
    
    /* Blocage de couleur blanche absolue pour tous les formats de texte possibles générés par l'IA */
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
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8) !important;
    }

    /* Typographie des titres de la recette */
    .recipe-display-container h2, .recipe-display-container h3 {
        font-family: 'Playfair Display', serif !important;
        font-size: 2.1rem !important;
        font-weight: 800 !important;
        margin-top: 32px !important;
        margin-bottom: 16px !important;
        border-bottom: 2px solid rgba(245, 158, 11, 0.4) !important;
        padding-bottom: 8px !important;
        color: #F59E0B !important; /* Doré pour structurer visuellement */
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

    /* Style général des textes statiques de l'application */
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

# ==============================================================================
# 💾 GESTION DES SESSIONS ET COMPTES UTILISATEURS
# ==============================================================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_mail" not in st.session_state:
    st.session_state.user_mail = ""

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("Erreur critique : La clé d'API Groq est manquante dans les configurations serveurs.")
    st.stop()

# ==============================================================================
# 🔑 INTERFACE DE CONNEXION ÉPURÉE (POP-OVER RETINA)
# ==============================================================================
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

# ==============================================================================
# 🏛️ EN-TÊTE D'ACCUEIL & PRÉSENTATION DU PROJET
# ==============================================================================
st.markdown("<h1 class='main-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class='pro-manifesto'>
        Chaque année en France, des millions de tonnes de nourriture parfaitement saine finissent à la poubelle par simple manque d'idées. 
        <strong>Arrêtez définitivement de jeter vos aliments.</strong> Notre intelligence artificielle culinaire analyse instantanément vos restes 
        pour concevoir des fiches recettes sur-mesure, adaptées à votre frigo, saines et économiques.
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 🛠️ BLOC FORMULAIRE DE RECHERCHE ET DE CONFIGURATION DIÉTÉTIQUE
# ==============================================================================
st.markdown("<div class='generator-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display, serif; font-size:1.6rem; text-align:center; font-weight:700; color:#FFF;'>🍳 Quels ingrédients reste-t-il dans votre frigo ?</h3>", unsafe_allow_html=True)

# Zone de saisie textuelle pour l'utilisateur
liste_ingredients = st.text_area(
    "", 
    placeholder="Inscrivez vos ingrédients ici, séparés par une virgule... (Ex: restes de dinde, fromage frais, courgettes)", 
    height=110, 
    label_visibility="collapsed",
    key="frigo_input_ipad"
)

# Sélecteur multi-choix pour filtrer la recette selon le profil de l'utilisateur
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

# ==============================================================================
# 🧠 GÉNÉRATION PAR L'INTELLIGENCE ARTIFICIELLE & SÉCURISATION HTML BINDING
# ==============================================================================
if bouton_generer:
    if not liste_ingredients:
        st.warning("Veuillez renseigner au moins un ingrédient pour lancer l'analyse de l'IA.")
    else:
        with st.spinner('Création de votre fiche culinaire sur-mesure par notre Chef virtuel...'):
            
            filtre_texte = ", ".join(options_regimes)
            
            # Système de prompt forçant l'IA à n'utiliser que du HTML sémantique
            prompt_systeme = (
                f"Tu es AntigaspIA, un chef étoilé expert en éco-cuisine. Rédige une recette à partir de ces ingrédients : {liste_ingredients}. "
                f"Contrainte absolue : Tu devez adapter la recette selon ces critères : {filtre_texte}. "
                f"Tu dois obligatoirement formater ta réponse exclusivement en HTML brut (sans aucun bloc de code markdown, pas de ```html). "
                f"Utilise des balises <h2> pour le titre de la recette et les rubriques principales (Ingrédients, Préparation), des balises <ul> et <li> pour lister les ingrédients, "
                f"et des balises <ol> et <li> pour détailler les étapes de préparation chronologiques. Écris tout en français."
            )
            
            # Appel à l'API de Groq (Llama 3.3 70B Versatile)
            reponse_api = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt_systeme}], 
                model="llama-3.3-70b-versatile"
            )
            
            st.markdown("""
                <div class='scroll-indicator'>
                    ⬇️ VOTRE RECETTE PERSONNALISÉE EST PRÊTE CI-DESSOUS ⬇️
                </div>
            """, unsafe_allow_html=True)
            
            # Affichage dans l'enveloppe étanche rétroéclairée pour neutraliser le bug du texte gris de Safari
            contenu_recette = reponse_api.choices[0].message.content
            st.markdown(f"""
                <div class='recipe-display-container'>
                    {contenu_recette}
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# 📋 PIED DE PAGE ET BAS DE MANIFESTE
# ==============================================================================
st.markdown("<p style='text-align:center; font-weight:700; margin-top:40px; font-size:1rem; color:#FFFFFF;'>Économiser intelligemment. Consommer durablement. Cuisiner élégamment.</p>", unsafe_allow_html=True)
