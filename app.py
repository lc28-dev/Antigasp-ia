import streamlit as st
from groq import Groq

# 1. Configuration Pro
st.set_page_config(page_title="AntigaspIA", page_icon="🍽️", layout="wide")

# 2. Injection CSS : Transparence, Animations et Contraste
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
    /* Image de fond visible partout */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.9)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Suppression des blocs blancs et gris par défaut de Streamlit */
    div[data-testid="stVerticalBlock"] > div {
        background-color: transparent !important;
    }
    
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: #1E293B !important;
        border-radius: 12px !important;
        border: 2px solid #E2E8F0 !important;
        font-size: 1.1rem !important;
    }

    /* Titres */
    .brand-title { font-family: 'Playfair Display', serif; font-size: 4rem; text-align: center; margin-top: 20px; color: #FFFFFF; }
    .brand-subtitle { text-align: center; color: #CBD5E1; font-size: 1.3rem; margin-bottom: 50px; font-weight: 600; }

    /* Panneaux effet "Verre" transparents */
    .glass-panel {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        color: #FFFFFF !important;
        margin-bottom: 20px;
    }

    /* Animation et design du bouton principal */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 60px;
        background: linear-gradient(90deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border: none !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
    }
    .stButton>button:hover {
        transform: scale(1.02) translateY(-2px) !important;
        box-shadow: 0 10px 25px rgba(245, 158, 11, 0.5) !important;
    }

    /* Customisation des boutons d'authentification pour casser la monotonie */
    div[data-testid="column"]:nth-child(1) .stButton>button {
        background: #22C55E !important; /* Vert pour s'identifier */
        color: white !important;
        height: 45px;
    }
    div[data-testid="column"]:nth-child(2) .stButton>button {
        background: transparent !important; /* Transparent bordé pour s'inscrire */
        color: #FFFFFF !important;
        border: 2px solid #FFFFFF !important;
        height: 45px;
    }

    /* Textes d'ambiance */
    .humor-text {
        font-style: italic;
        color: #94A3B8;
        font-size: 0.95rem;
        margin-top: 15px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALISATION ---
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "user_prefs" not in st.session_state:
    st.session_state.user_prefs = "Classique"

try:
    client_groq = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("🔑 Clé GROQ_API_KEY manquante.")
    st.stop()

# --- HEADER REFAIT ---
st.markdown("<h1 class='brand-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Arrêtez de jeter les restes du frigo et transformez-les en une recette ultra-économique.</p>", unsafe_allow_html=True)

# --- ESPACE DE TRAVAIL ---
col_workspace, col_sidebar = st.columns([1.6, 1])

# --- COLONNE GAUCHE : ESSAI IMMÉDIAT ---
with col_workspace:
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top:0; color:white;'>🍳 Génération d'une recette délicieuse grâce à ce qu'il reste dans mon frigo !</h3>", unsafe_allow_html=True)
    
    if st.session_state.user_authenticated:
        st.markdown(f"<p style='color:#22C55E; font-size:0.9rem;'>● Profil actif : {st.session_state.user_email} ({st.session_state.user_prefs})</p>", unsafe_allow_html=True)
    
    ingredients = st.text_area("", placeholder="Ouvrez votre frigo, regardez ce qui traîne et tapez tout ici... (Ex: 3 tomates fripées, un demi-oignon, un reste de poulet rôti)", height=160, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.button("Transformer mes restes en festin")
    
    st.markdown("<p class='humor-text'>Garantie 100% sans prise de tête. Même votre vieux morceau de fromage a droit à une seconde chance.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if submit:
        if not ingredients:
            st.warning("Ajoutez au moins un ingrédient, l'IA ne sait pas encore cuisiner le vide !")
        else:
            with st.spinner('Le Chef virtuel inspecte vos ingrédients...'):
                regime_context = st.session_state.user_prefs if st.session_state.user_authenticated else "Aucune restriction"
                prompt = f"Tu es AntigaspIA, expert anti-gaspi. Crée une recette gourmande, économique et rapide avec : {ingredients}. Contexte optionnel : {regime_context}. Donne lui un titre sympa."
                completion = client_groq.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
                
                st.markdown("<div class='glass-panel' style='background:rgba(15,23,42,0.8) !important;'>", unsafe_allow_html=True)
                st.markdown("### 📋 Votre Protocole Anti-Gaspi")
                st.write(completion.choices[0].message.content)
                st.markdown("</div>", unsafe_allow_html=True)
                st.balloons()

# --- COLONNE DROITE : AUTHENTIFICATION MUTÉE ---
with col_sidebar:
    st.markdown("<div class='glass-panel' style='background: rgba(15, 23, 42, 0.4) !important;'>", unsafe_allow_html=True)
    
    if not st.session_state.user_authenticated:
        st.markdown("<h4 style='color:white; margin-top:0;'>🔐 ACCÈS MEMBRE PREMIUM</h4>", unsafe_allow_html=True)
        st.write("Entrez n'importe quel e-mail pour simuler l'interface.")
        
        email_input = st.text_input("Adresse Email", placeholder="chef@exemple.com")
        password_input = st.text_input("Mot de passe", type="password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        col_btn_a, col_btn_b = st.columns(2)
        with col_btn_a:
            if st.button("S'identifier"):
                if email_input:
                    st.session_state.user_authenticated = True
                    st.session_state.user_email = email_input
                    st.rerun()
        with col_btn_b:
            if st.button("S'inscrire"):
                if email_input:
                    st.success("Profil enregistré.")
                    
        st.markdown("<p style='font-size:0.8rem; color:#94A3B8; text-align:center; margin-top:15px;'>Note : L'intégration du module d'abonnement Stripe Premium est en cours de déploiement.</p>", unsafe_allow_html=True)
                    
    else:
        st.markdown("<h4 style='color:white; margin-top:0;'>⚙️ TABLEAU DE BORD</h4>", unsafe_allow_html=True)
        st.write(f"Utilisateur : **{st.session_state.user_email}**")
        
        st.session_state.user_prefs = st.selectbox("Votre profil de cuisson :", ["Classique", "Végétarien", "Économique Max", "Zéro Déchet Express"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Se déconnecter"):
            st.session_state.user_authenticated = False
            st.session_state.user_email = ""
            st.session_state.user_prefs = "Classique"
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

# --- TEXTE MARKETING EN BAS ---
st.markdown("<p style='text-align: center; color: #64748B; font-size: 0.9rem; margin-top: 60px;'>Fini le gaspillage, place aux économies. Rejoignez la révolution culinaire intelligente.</p>", unsafe_allow_html=True)
