import streamlit as st
from groq import Groq

# 1. Configuration de la page
st.set_page_config(page_title="AntigaspIA", page_icon="🍽️", layout="wide")

# 2. CSS Radical : Destruction des blocs fantômes et Forçage du Blanc Pur
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
    /* IMAGE DE FOND NETTE SANS SUPERPOSITION */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.4), rgba(15, 23, 42, 0.65)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* SUPPRESSION RADICALE DE LA BANDE BLEUE / BLOCS FANTÔMES MID-PAGE */
    div[data-testid="stHorizontalBlock"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    /* Élimine les résidus de l'ancien layout en colonnes */
    div[data-testid="stBlock"] {
        background: transparent !important;
        border: none !important;
    }

    /* TITRES EN BLANC PUR ÉCLATANT */
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

    /* ZONE DE GÉNÉRATION GRAND FORMAT */
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

    /* FORCE LE STYLE DU BOUTON DE CONNEXION (Plus de bloc blanc invisible) */
    div[data-testid="stPopover"] > button {
        background-color: #1E293B !important; /* Gris anthracite pro */
        color: #FFFFFF !important; /* Écrit en blanc */
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
    }
    
    /* BOÎTE DE RÉPONSE IA FORCÉE EN BLANC */
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

    /* ZONE DE TEXTE (INPUT FRIGO) */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
        font-weight: 500;
    }

    /* BOUTON ORANGE D'ACTION PRINCIPALE */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 60px;
        background: linear-gradient(90deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border: none !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 30px rgba(245, 158, 11, 0.6) !important;
    }

    /* ALIGNEMENT BOUTON CONNEXION */
    .login-bar {
        max-width: 950px;
        margin: 0 auto;
        text-align: right;
        padding-top: 15px;
    }

    /* SIGNAL DE RÉUSSITE VERT */
    .success-indicator {
        text-align: center;
        background: #10B981 !important;
        color: #FFFFFF !important;
        padding: 14px;
        border-radius: 10px;
        font-weight: 700;
        margin-top: 25px;
    }
    
    /* TOUT LE TEXTE SECONDAIRE FORCÉ EN BLANC */
    label, span, p, h3, h4 { color: #FFFFFF !important; }
    
    .footer-text {
        text-align: center; 
        color: #FFFFFF !important; 
        font-size: 1.1rem !important; 
        font-weight: 700 !important;
        margin-top: 60px; 
        text-shadow: 2px 2px 8px rgba(0,0,0,0.9);
    }
    </style>
    """, unsafe_allow_html=True)

# --- TRACKING DE SESSION ---
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

try:
    client_groq = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Clé GROQ_API_KEY manquante.")
    st.stop()

# --- BARRE DE CONNEXION (HAUT À DROITE) ---
st.markdown("<div class='login-bar'>", unsafe_allow_html=True)
if not st.session_state.user_authenticated:
    with st.popover("🔑 Connexion Membre"):
        st.markdown("<p style='color:#0F172A !important; font-size:0.9rem; font-weight:600;'>Connecte-toi pour que tes préférences soient sauvegardées ! Plus besoin de les préciser à chaque fois.</p>", unsafe_allow_html=True)
        email = st.text_input("Email", placeholder="chef@exemple.com")
        if st.button("S'identifier / S'inscrire"):
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

# --- EN-TÊTE PROFESSIONNEL ET ENGAGÉ ---
st.markdown("<h1 class='brand-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("""
    <p class='brand-subtitle'>
        Chaque année, des millions de tonnes de nourriture finissent à la poubelle par simple manque d'inspiration. 
        <b>Arrêtez de jeter les restes de votre frigo.</b> Notre technologie analyse instantanément vos ingrédients isolés 
        pour concevoir des fiches recettes haut de gamme, sur mesure et ultra-économiques. Sauvez votre budget, honorez vos produits.
    </p>
""", unsafe_allow_html=True)

# --- PANNEAU CENTRAL (TOUTE LA LARGEUR) ---
st.markdown("<div class='main-glass-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display; font-size:1.8rem; text-align:center;'>🍳 Génération d'une recette délicieuse grâce à ce qu'il reste dans mon frigo !</h3>", unsafe_allow_html=True)

ingredients = st.text_area("", placeholder="Entrez vos ingrédients ici, séparés par une virgule... (Ex: 3 patates, reste de lardons, fond de crème liquide)", height=140, label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)
submit = st.button("Transformer mes restes en festin")

# --- TRAITEMENT DE LA RECETTE ---
if submit:
    if not ingredients:
        st.warning("Ajoutez au moins un ingrédient pour lancer la création.")
    else:
        with st.spinner('Création de votre fiche culinaire en cours...'):
            prompt = f"Tu es AntigaspIA. Crée une recette excellente, économique, claire et structurée avec : {ingredients}. Écris impérativement tout ton texte en français."
            completion = client_groq.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
            
            # Indicateur de succès
            st.markdown("<div class='success-indicator'>✨ Votre recette sur-mesure a été générée avec succès ! Découvrez-la ci-dessous.</div>", unsafe_allow_html=True)
            
            # Bloc réponse en BLANC SUR NOIR CONTRASTÉ
            st.markdown("<div class='recipe-box'>", unsafe_allow_html=True)
            st.markdown(completion.choices[0].message.content)
            st.markdown("</div>", unsafe_allow_html=True)
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# --- TEXTE DE FIN EN BLANC ULTRA-LISIBLE ---
st.markdown("<p class='footer-text'>Économiser intelligemment. Consommer durablement.</p>", unsafe_allow_html=True)
