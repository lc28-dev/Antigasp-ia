import streamlit as st
from groq import Groq

# 1. CONFIGURATION DE PAGE ULTRA-LARGE
st.set_page_config(
    page_title="AntigaspIA - Cuisine Durable", 
    page_icon="🍽️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. DESIGN GLOBAL ET INJECTION CSS AGRESSIVE (Anti-Bleu, Anti-Gris, Contraste Max)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');
    
    /* Image de fond plein écran avec un filtre sombre pour la lisibilité */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.6), rgba(15, 23, 42, 0.8)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* NETTOYAGE ABSOLU DES COUCHES BLEU MARINE DE STREAMLIT */
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

    /* SUPPRESSION DES MARGES INUTILES EN HAUT SUR IPAD */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
    }

    /* BARRE SUPÉRIEURE DE CONNEXION (EN HAUT À DROITE) */
    .top-header-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 10px 20px;
    }

    /* BLOC D'INSCRIPTION EN HAUT À DROITE - ENTIÈREMENT STYLISÉ SANS BLANC */
    .custom-auth-box {
        background: rgba(15, 23, 42, 0.85) !important;
        border: 2px solid rgba(245, 158, 11, 0.4);
        border-radius: 16px;
        padding: 20px;
        width: 350px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }

    /* TYPOGRAPHIE ET TITRES */
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 5rem;
        font-weight: 800;
        text-align: center;
        color: #FFFFFF !important;
        margin-top: 10px;
        margin-bottom: 5px;
        text-shadow: 3px 3px 20px rgba(0, 0, 0, 0.9);
    }

    /* TEXTE PROFESSIONNEL ANTI-GASPILLAGE */
    .pro-manifesto {
        font-size: 1.35rem;
        font-weight: 500;
        line-height: 1.7;
        text-align: center;
        color: #F8FAFC !important;
        max-width: 950px;
        margin: 0 auto 40px auto;
        text-shadow: 2px 2px 12px rgba(0, 0, 0, 0.9);
    }
    .pro-manifesto strong {
        color: #F59E0B !important;
        font-weight: 700;
    }

    /* BLOC DE GÉNÉRATION PRINCIPAL (TOUTE LA LARGEUR DE LECTURE) */
    .generator-panel {
        background: rgba(30, 41, 59, 0.7) !important;
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        padding: 45px;
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 40px 80px rgba(0, 0, 0, 0.7);
        max-width: 1100px;
        margin: 0 auto 30px auto;
    }

    /* CHAMP DE TEXTE (FRIGO) */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 2px solid rgba(255,255,255,0.1) !important;
        border-radius: 14px !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        padding: 15px !important;
    }
    .stTextArea textarea:focus {
        border-color: #F59E0B !important;
    }

    /* GRAND BOUTON ORANGE LUMINEUX */
    .stButton>button {
        width: 100%;
        border-radius: 14px;
        height: 65px;
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        font-size: 1.2rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: none !important;
        box-shadow: 0 6px 25px rgba(245, 158, 11, 0.4);
        transition: all 0.2s ease-transform;
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 35px rgba(245, 158, 11, 0.6) !important;
    }

    /* DESIGN ET FLÈCHE INDICATRICE APRÈS GÉNÉRATION */
    .scroll-indicator {
        text-align: center;
        background: #10B981 !important;
        color: #FFFFFF !important;
        padding: 16px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.2rem;
        margin: 30px 0;
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4);
        animation: pulseAnimation 2s infinite;
    }
    
    @keyframes pulseAnimation {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }

    /* BOÎTE DE RÉPONSE DE L'IA (BLANC INTENSE SUR FOND NOIR COMPLET PROTECTEUR) */
    .recipe-output-card {
        background: #090D16 !important;
        border-left: 8px solid #F59E0B;
        padding: 40px;
        border-radius: 18px;
        margin-top: 25px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.8);
    }
    .recipe-output-card, 
    .recipe-output-card p, 
    .recipe-output-card li, 
    .recipe-output-card h1, 
    .recipe-output-card h2, 
    .recipe-output-card h3,
    .recipe-output-card strong {
        color: #FFFFFF !important;
        font-size: 1.2rem !important;
        line-height: 1.85 !important;
    }

    /* PROTECTION DES LABELS ET DE TOUS LES TEXTES CONTRE LE BLEU MARINE */
    label, p, span, h1, h2, h3, h4, h5, h6 { 
        color: #FFFFFF !important; 
        text-shadow: 1px 1px 4px rgba(0,0,0,0.5);
    }

    /* TEXTES À L'INTÉRIEUR DES INPUTS D'AUTHENTIFICATION (BLANC INTERDIT EN FOND) */
    .custom-auth-box .stTextInput input {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 8px !important;
    }

    /* FOOTER BLANC SUR */
    .footer-brand {
        text-align: center;
        color: #FFFFFF !important;
        font-size: 1.25rem !important;
        font-weight: 700;
        margin-top: 70px;
        text-shadow: 2px 2px 10px rgba(0,0,0,1);
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. GESTION DU SYSTÈME DE SESSION ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_mail" not in st.session_state:
    st.session_state.user_mail = ""

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Le token de connexion Groq est manquant dans vos secrets système.")
    st.stop()


# --- 4. DISPOSITION SUPÉRIEURE : INSCRIPTION & CONNEXION EN HAUT À DROITE ---
st.markdown("<div class='top-header-container'>", unsafe_allow_html=True)

# Simulation de mise en page haute droite propre via des colonnes invisibles larges
col_vide, col_auth = st.columns([2.5, 1])

with col_auth:
    st.markdown("<div class='custom-auth-box'>", unsafe_allow_html=True)
    if not st.session_state.authenticated:
        st.markdown("<h5 style='margin-top:0; font-weight:700; color:#F59E0B !important;'>🔑 Espace Privé</h5>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:0.88rem; line-height:1.4; opacity:0.95; margin-bottom:12px;'>Connecte-toi pour que tes préférences soient sauvegardées ! Plus besoin de les préciser à chaque fois.</p>", unsafe_allow_html=True)
        
        login_input = st.text_input("Adresse Email", placeholder="exemple@domaine.com", key="auth_mail_node", label_visibility="collapsed")
        
        if st.button("S'identifier / S'inscrire", key="btn_auth_validate"):
            if login_input:
                st.session_state.authenticated = True
                st.session_state.user_mail = login_input
                st.rerun()
    else:
        st.markdown(f"<p style='color:#10B981 !important; font-weight:700; margin:0 0 10px 0;'>✓ Connecté : {st.session_state.user_mail}</p>", unsafe_allow_html=True)
        if st.button("Se déconnecter du compte", key="btn_auth_logout"):
            st.session_state.authenticated = False
            st.session_state.user_mail = ""
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# --- 5. TITRE PRINCIPAL & MANIFESTE GRAND LOGICIEL (ANTI-GASPILLAGE) ---
st.markdown("<h1 class='main-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("""
    <div class='pro-manifesto'>
        Chaque année en France, des millions de tonnes de nourriture parfaitement saine finissent à la poubelle par simple manque d'idées. 
        Un demi-citron qui s'assèche, un reste de lardons oubliés ou trois pommes de terre cuites de la veille ne méritent pas la décharge. 
        <strong>Arrêtez définitivement de jeter vos ressources.</strong> Notre algorithme culinaire de pointe analyse instantanément vos restes isolés 
        pour concevoir des fiches recettes d'excellence, adaptées à votre frigo, ultra-économiques et simples à réaliser. 
        Sauvez votre budget mensuel, honorez le travail de nos producteurs et repensez votre façon de cuisiner au quotidien.
    </div>
""", unsafe_allow_html=True)


# --- 6. PANNEAU CENTRAL DE GÉNÉRATION (TOUTE LA LARGEUR) ---
st.markdown("<div class='generator-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display, serif; font-size:2.2rem; text-align:center; font-weight:700;'>🍳 Que cache votre réfrigérateur aujourd'hui ?</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; opacity:0.8; font-size:1.05rem; margin-bottom:20px;'>Indiquez vos aliments restants ci-dessous, notre cuisine s'occupe de créer le plat parfait.</p>", unsafe_allow_html=True)

# Zone de saisie géante
liste_ingredients = st.text_area(
    "", 
    placeholder="Inscrivez vos ingrédients ici, séparés par une simple virgule... (Exemple: 3 patates froides, un reste de lardons, un fond de crème liquide, un demi-oignon)", 
    height=150, 
    label_visibility="collapsed",
    key="input_frigo_user"
)

st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)
bouton_generer = st.button("Transformer mes restes en un festin de chef", key="btn_main_generation")


# --- 7. TRAITEMENT, DISPOSITIF DE DESCENTE ET RÉPONSE DE L'IA ---
if bouton_generer:
    if not liste_ingredients:
        st.warning("Veuillez mentionner au moins un ingrédient ou reste présent dans votre cuisine pour initier la création.")
    else:
        with st.spinner('Analyse des saveurs et rédaction de votre fiche culinaire sur-mesure...'):
            
            # Requête API Groq
            prompt_systeme = (
                f"Tu es AntigaspIA, un chef expert en cuisine zéro-déchet. Génère une recette excellente, "
                f"très claire et économique avec exclusivement ces ingrédients : {liste_ingredients}. "
                f"Structure obligatoirement ta réponse avec : un titre de recette accrocheur, un récapitulatif des ingrédients "
                f"et les étapes de préparation numérotées de façon limpide. Rédige l'intégralité du texte en français."
            )
            
            reponse_api = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt_systeme}], 
                model="llama-3.3-70b-versatile"
            )
            
            # CONTENEUR DE SIGNALISATION (Montre que la réponse est en dessous)
            st.markdown("""
                <div class='scroll-indicator'>
                    ⬇️ VOTRE RECETTE UNIQUE EST PRÊTE ! DÉCOUVREZ VOTRE FICHE DE CUISINE JUSTE CI-DESSOUS ⬇️
                </div>
            """, unsafe_allow_html=True)
            
            # AFFICHAGE DE LA FICHE RECETTE EN BLANC INTENSE SUR NOIR
            st.markdown("<div class='recipe-output-card'>", unsafe_allow_html=True)
            st.markdown(reponse_api.choices[0].message.content)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Animation festive de fin
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True) # FIN DU GENERATOR PANEL


# --- 8. PIED DE PAGE PROFESSIONNEL ET PROPRE (BLANC NET) ---
st.markdown("<p class='footer-brand'>Économiser intelligemment. Consommer durablement. Cuisiner élégamment.</p>", unsafe_allow_html=True)
