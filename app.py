import streamlit as st
from groq import Groq
import os
import json

# ==============================================================================
# 📐 CONFIGURATION ET SÉCURISATION DE LA PAGE NATIVE
# ==============================================================================
st.set_page_config(
    page_title="AntigaspIA — Cuisine Éco-Responsable", 
    page_icon="🍽️", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 🧲 INJECTION DE SÉCURITÉ ADSENSE DIRECTE (HORS IFRAME)
# ==============================================================================
st.html("""
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1756718492717210" crossorigin="anonymous"></script>
""")

# ==============================================================================
# 🎨 ARCHITECTURE STYLING CSS AVANCÉE (OPTIMISÉE BLANC PUR POUR IPAD)
# ==============================================================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&family=Playfair+Display:wght=600;700;800;900&display=swap');
    
    /* Neutralisation absolue des glissements latéraux indésirables sur tablettes Apple */
    html, body, .stApp, .block-container {
        max-width: 100vw !important;
        overflow-x: hidden !important;
        margin: 0 auto !important;
    }

    /* Arrière-plan cinématique avec overlay de protection pour le contraste */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.75), rgba(15, 23, 42, 0.95)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Suppression des containers blancs parasites de Streamlit */
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

    /* Alignement du module popover utilisateur à droite */
    .discreet-login-container {
        text-align: right;
        margin-bottom: 30px;
        width: 100%;
    }
    div[data-testid="stPopover"] {
        display: inline-block !important;
    }
    div[data-testid="stPopover"] > button {
        background-color: rgba(30, 41, 59, 0.8) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* Titrage Principal Typographie Luxe */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #FFFFFF 30%, #E2E8F0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    /* Grand Texte Manifeste */
    .pro-manifesto {
        font-size: 1.2rem;
        line-height: 1.7;
        text-align: center;
        max-width: 750px;
        margin: 0 auto 40px auto;
        color: #94A3B8 !important;
        font-weight: 400;
    }
    .pro-manifesto strong {
        color: #F59E0B !important;
        font-weight: 700;
    }

    /* Panneau d'action central effet "Glassmorphism" */
    .generator-panel {
        background: rgba(30, 41, 59, 0.55) !important;
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        padding: 35px;
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.45);
        width: 100% !important;
        box-sizing: border-box;
        margin-bottom: 40px;
    }

    /* Forçage visuel des Selectbox (Texte sombre lisible sur fond blanc pur) */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    div[data-baseweb="select"] * {
        color: #0F172A !important;
        font-weight: 600 !important;
    }
    
    /* 🌟 FIX RETINA IPAD : FORCE LE TEXTE DES TITRES DE SÉLECTEURS EN BLANC PUR 🌟 */
    div[data-testid="stWidgetLabel"] p, 
    label[data-testid="stWidgetLabel"] p,
    .st-emotion-cache-10trblm p,
    .st-emotion-cache-1p7n9v0 p {
        color: #FFFFFF !important;
        color: rgb(255, 255, 255) !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        margin-bottom: 8px !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5) !important;
    }

    /* Zone de saisie TextArea des ingrédients */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 16px !important;
        font-size: 1.15rem !important;
        padding: 18px !important;
        border: 2px solid transparent !important;
        font-weight: 500 !important;
    }

    /* Grand bouton d'exécution Or Ambré Cuit */
    .stButton>button {
        width: 100% !important;
        border-radius: 16px !important;
        height: 62px !important;
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px;
        border: none !important;
        box-shadow: 0 10px 25px rgba(217, 119, 6, 0.35) !important;
    }

    /* Indicateur de chargement / succès vert émeraude */
    .scroll-indicator {
        text-align: center;
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: #FFFFFF !important;
        padding: 16px;
        border-radius: 14px;
        font-weight: 800;
        margin-top: 30px;
        margin-bottom: 30px;
        font-size: 1.05rem;
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.25);
    }

    /* BLOC DE CONFINEMENT DU RENDU CULINAIRE */
    .recipe-display-container {
        background: rgba(15, 23, 42, 0.92) !important;
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 28px;
        padding: 40px;
        margin-top: 35px;
        box-shadow: 0 25px 55px rgba(0, 0, 0, 0.65);
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
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        margin-top: 35px !important;
        margin-bottom: 20px !important;
        border-bottom: 2px solid rgba(245, 158, 11, 0.4) !important;
        padding-bottom: 10px !important;
        color: #F59E0B !important;
    }

    .recipe-display-container p, .recipe-display-container li {
        font-size: 1.25rem !important;
        line-height: 1.9 !important;
        font-weight: 500 !important;
        color: #F8FAFC !important;
    }

    .recipe-display-container ul, .recipe-display-container ol {
        margin-left: 30px !important;
        padding-left: 0px !important;
    }

    .recipe-display-container li {
        margin-bottom: 14px !important;
        list-style-position: outside !important;
    }

    .inner-auth-form {
        background-color: #0F172A !important;
        padding: 20px;
        border-radius: 16px;
        width: 280px;
    }
    .inner-auth-form input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 10px !important;
    }
    
    .footer-text {
        text-align: center;
        font-weight: 600;
        margin-top: 50px;
        font-size: 1rem;
        color: #64748B !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 💾 VÉRIFICATION ET INITIALISATION DU SYSTEM STATS
# ==============================================================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_mail" not in st.session_state:
    st.session_state.user_mail = ""

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("Erreur d'accès : Clé d'API Groq manquante dans les Secrets.")
    st.stop()

# ==============================================================================
# 🔑 POP-OVER DE CONNEXION COMPTE
# ==============================================================================
st.markdown("<div class='discreet-login-container'>", unsafe_allow_html=True)
if not st.session_state.authenticated:
    with st.popover("🔑 Espace Chef : Connexion"):
        st.markdown("<div class='inner-auth-form'>", unsafe_allow_html=True)
        st.markdown("<p style='margin-top:0;font-weight:700;color:#FFF;'>Rejoindre la brigade</p>", unsafe_allow_html=True)
        mail_input = st.text_input("Adresse Email", placeholder="chef@antigaspia.fr", key="discreet_mail_key")
        if st.button("Valider l'accès", key="btn_discreet_submit"):
            if mail_input:
                st.session_state.authenticated = True
                st.session_state.user_mail = mail_input
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
else:
    if st.button(f"👤 Compte : {st.session_state.user_mail} (Déconnexion)", key="btn_discreet_logout"):
        st.session_state.authenticated = False
        st.session_state.user_mail = ""
        st.rerun()
st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# 🏛️ IDENTITÉ VISUELLE ET PRO-MANIFESTE EN HAUT
# ==============================================================================
st.markdown("<h1 class='main-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class='pro-manifesto'>
        Chaque année en France, des millions de tonnes de nourriture parfaitement saine finissent à la poubelle par simple manque d'idées. 
        <strong>Arrêtez définitivement de jeter vos aliments.</strong> Notre intelligence artificielle culinaire analyse instantanément vos restes 
        pour concevoir des fiches de recettes gastronomiques sur-mesure. Économisez de l'argent, préservez la planète et cuisinez comme un grand chef.
    </div>
""", unsafe_allow_html=True)

# ==============================================================================
# 🛠️ BLOC FORMULAIRE DE TRI ET PRÉFÉRENCES
# ==============================================================================
st.markdown("<div class='generator-panel'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    temps_preparation = st.selectbox("⏳ Temps disponible", ["Rapide (-20 min)", "Moyen (20-40 min)", "Prendre son temps (40+ min)"])
with col2:
    niveau_difficulte = st.selectbox("👨‍🍳 Niveau de cuisine", ["Débutant", "Intermédiaire", "Chef étoilé"])
with col3:
    type_plat = st.selectbox("🍽️ Type de repas", ["Plat principal", "Entrée créative", "Snack / Apéro", "Dessert surprise"])

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<p style='color:#FFFFFF; font-weight:700; font-size:1.05rem; margin-bottom:8px;'>🍳 Quels ingrédients reste-t-il dans votre frigo ?</p>", unsafe_allow_html=True)
liste_ingredients = st.text_area(
    "Label invisible",
    placeholder="Exemple : 2 tomates fatiguées, un demi-oignon, un reste de dinde, crème fraîche...", 
    height=120, 
    key="frigo_input_ipad",
    label_visibility="collapsed"
)

st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)
bouton_generer = st.button("Transformer mes restes en un festin de chef", key="btn_execute_recipe")

# ==============================================================================
# 🧠 REQUÊTAGE ET ENCAPSULATION DE LA RÉPONSE IA
# ==============================================================================
if bouton_generer:
    if not liste_ingredients:
        st.warning("Veuillez renseigner au moins un ingrédient pour lancer la création de la recette.")
    else:
        with st.spinner('Analyse des restes et composition de votre fiche culinaire...'):
            
            prompt_systeme = (
                f"Tu es AntigaspIA, un grand chef cuisinier étoilé et expert en optimisation anti-gaspillage. "
                f"Crée une recette magistrale de niveau '{niveau_difficulte}' pour un '{type_plat}' réalisable en '{temps_preparation}'. "
                f"Utilise en priorité absolue ces restes : {liste_ingredients}. "
                f"Contrainte technique majeure : Tu dois obligatoirement formater l'intégralité de ta réponse en code HTML sémantique et propre. "
                f"N'utilise jamais de balises ou blocs de code markdown (pas de ```html, pas de étoiles **). "
                f"Structure obligatoirement ton texte avec des balises <h2> pour les titres des grandes sections suivantes : "
                f"1. Nom de la recette (trouve un nom original de grand restaurant), 2. Ingrédients nécessaires, 3. Étapes de préparation (chronologiques), "
                f"4. L'astuce anti-gaspillage du Chef. Utilise des listes à puces <ul> avec des puces <li> pour les ingrédients et des listes ordonnées <ol> avec <li> pour les étapes."
            )
            
            reponse_api = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt_systeme}], 
                model="llama-3.3-70b-versatile"
            )
            
            st.markdown("""
                <div class='scroll-indicator'>
                    ⬇️ VOTRE FICHE CULINAIRE EXCLUSIVE EST PRÊTE CI-DESSOUS ⬇️
                </div>
            """, unsafe_allow_html=True)
            
            contenu_recette = reponse_api.choices[0].message.content
            st.markdown(f"""
                <div class='recipe-display-container'>
                    {contenu_recette}
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# 📋 FOOTER BRANDING
# ==============================================================================
st.markdown("<p class='footer-text'>Économiser intelligemment. Consommer durablement. Cuisiner élégamment.</p>", unsafe_allow_html=True)
