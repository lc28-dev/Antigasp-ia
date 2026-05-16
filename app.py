import streamlit as st
from groq import Groq

# 1. Configuration de la page
st.set_page_config(page_title="AntigaspIA", page_icon="🍽️", layout="wide")

# 2. Injection CSS Avancée (Zéro parasite, lisibilité maximale)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
    /* Image de fond ultra nette */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.5), rgba(15, 23, 42, 0.7)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Suppression définitive de TOUTES les boîtes et colonnes fantômes de Streamlit */
    div[data-testid="stHorizontalBlock"], div[data-testid="stVerticalBlock"] > div {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Titres principaux */
    .brand-title { 
        font-family: 'Playfair Display', serif; 
        font-size: 4.5rem; 
        text-align: center; 
        margin-top: 20px; 
        color: #FFFFFF !important; 
        text-shadow: 2px 2px 12px rgba(0, 0, 0, 0.9);
        font-weight: 800;
    }
    .brand-subtitle { 
        text-align: center; 
        color: #F8FAFC !important; 
        font-size: 1.3rem; 
        max-width: 800px;
        margin: 0 auto 30px auto; 
        font-weight: 500;
        line-height: 1.6;
        text-shadow: 1px 1px 6px rgba(0, 0, 0, 0.9);
    }

    /* Zone principale grand format (Toute la largeur) */
    .main-glass-panel {
        background: rgba(15, 23, 42, 0.65) !important;
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        padding: 40px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
        max-width: 950px;
        margin: 0 auto 30px auto;
    }

    /* Boîte de réception de la recette (Forcée en blanc sur fond sombre protecteur) */
    .recipe-box {
        background: rgba(10, 15, 30, 0.9) !important;
        border-left: 5px solid #F59E0B;
        padding: 30px;
        border-radius: 12px;
        margin-top: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    /* FORCE LE TEXTE DE L'IA EN BLANC PUR */
    .recipe-box, .recipe-box p, .recipe-box li, .recipe-box h1, .recipe-box h2, .recipe-box h3 {
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
    }

    /* Textarea stylisé */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: #0F172A !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
        font-weight: 500;
    }

    /* Grand bouton d'action orange */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 60px;
        background: linear-gradient(90deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border: none !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 25px rgba(245, 158, 11, 0.6) !important;
    }

    /* Bouton Connexion en haut à droite */
    .login-bar {
        max-width: 950px;
        margin: 0 auto;
        text-align: right;
        padding-right: 10px;
    }

    /* Signal visuel de succès */
    .success-indicator {
        text-align: center;
        background: #10B981;
        color: white;
        padding: 12px;
        border-radius: 8px;
        font-weight: bold;
        margin-top: 25px;
        animation: pulse 2s infinite;
    }
    
    label, span { color: #FFFFFF !important; }
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
    st.error("Clé GROQ_API_KEY manquante dans vos secrets.")
    st.stop()

# --- BARRE DE CONNEXION SUPÉRIEURE (Haut à Droite) ---
st.markdown("<div class='login-bar'>", unsafe_allow_html=True)
if not st.session_state.user_authenticated:
    with st.popover("🔑 Connexion Membre"):
        st.markdown("<p style='color:#0F172A !important; font-size:0.85rem;'>Connecte-toi pour sauvegarder tes préférences et ne plus avoir à les préciser à chaque fois !</p>", unsafe_allow_html=True)
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

# --- PANNEAU CENTRAL DE GÉNÉRATION (TOUTE LA LARGEUR) ---
st.markdown("<div class='main-glass-panel'>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-top:0; font-family:Playfair Display; font-size:1.8rem; color:white; text-align:center;'>🍳 Génération d'une recette délicieuse grâce à ce qu'il reste dans mon frigo !</h3>", unsafe_allow_html=True)

ingredients = st.text_area("", placeholder="Entrez vos ingrédients ici, séparés par une virgule... (Ex: 3 patates, reste de lardons, fond de crème liquide)", height=140, label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)
submit = st.button("Transformer mes restes en festin")

# --- TRAITEMENT ET RÉPONSE ---
if submit:
    if not ingredients:
        st.warning("Ajoutez au moins un ingrédient pour lancer la création.")
    else:
        with st.spinner('Création de votre fiche culinaire en cours...'):
            prompt = f"Tu es AntigaspIA. Crée une recette excellente, économique et claire avec : {ingredients}. Structure parfaitement avec un titre accrocheur, les ingrédients et les étapes."
            completion = client_groq.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
            
            # Message qui montre que la réponse est prête juste en dessous
            st.markdown("<div class='success-indicator'>✨ Votre recette sur-mesure a été générée avec succès ! Découvrez-la ci-dessous.</div>", unsafe_allow_html=True)
            
            # Conteneur de réponse avec texte forcé en BLANC
            st.markdown("<div class='recipe-box'>", unsafe_allow_html=True)
            st.markdown(completion.choices[0].message.content)
            st.markdown("</div>", unsafe_allow_html=True)
            st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #CBD5E1 !important; font-size: 0.95rem; margin-top: 50px; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);'>Économisez intelligemment. Consommez durablement.</p>", unsafe_allow_html=True)
