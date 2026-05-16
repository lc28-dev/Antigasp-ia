import streamlit as st
from groq import Groq

# 1. Configuration de la page
st.set_page_config(page_title="AntigaspIA", page_icon="🍽️", layout="wide")

# 2. Nettoyage CSS Cyber-Agressif (Zéro Blocs Parasites, Immersion Totale)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Playfair+Display:wght@700&display=swap');
    
    /* 1. FORCE L'IMAGE DE FOND SANS LE BLEU OPAQUE DE STREAMLIT */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.45), rgba(15, 23, 42, 0.65)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000') !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* 2. ÉLIMINATION RADICALE DES DEUX CASES PARASITES ET DU BLOC BLANC */
    div[data-testid="stHorizontalBlock"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    /* Force la disparition des boîtes vides générées en haut par l'ancien layout */
    div[data-testid="stVerticalBlock"] > div:has(div[class*="stAlert"]) {
        background: transparent !important;
    }

    /* 3. VISIBILITÉ DU TITRE ET DE L'ACCROCHE */
    .brand-title { 
        font-family: 'Playfair Display', serif; 
        font-size: 4.5rem; 
        text-align: center; 
        margin-top: 40px; 
        color: #FFFFFF !important; 
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.8);
        font-weight: 800;
    }
    .brand-subtitle { 
        text-align: center; 
        color: #F8FAFC !important; 
        font-size: 1.4rem; 
        margin-bottom: 40px; 
        font-weight: 600;
        text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.8);
    }

    /* 4. DESIGN GLASSMORPHISM ÉPURÉ POUR LES DEUX COLONNES */
    .glass-panel {
        background: rgba(15, 23, 42, 0.65) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        padding: 40px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        color: #FFFFFF !important;
        margin-bottom: 25px;
    }

    /* 5. TEXTAREA HAUTE VISIBILITÉ */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.95) !important;
        color: #0F172A !important;
        border-radius: 12px !important;
        border: 2px solid #E2E8F0 !important;
        font-size: 1.1rem !important;
        font-weight: 500;
    }

    /* 6. BOUTON ACTION ULTRA DYNAMIQUE (ORANGE LUXE) */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 60px;
        background: linear-gradient(90deg, #F59E0B 0%, #D97706 100%) !important;
        color: #0F172A !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        border: none !important;
        transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.02) translateY(-2px) !important;
        box-shadow: 0 12px 25px rgba(245, 158, 11, 0.6) !important;
    }

    /* 7. COULEURS BOUTONS AUTHENTIFICATION */
    /* Colonne Membre - S'identifier (Vert émeraude) */
    div[data-testid="column"]:nth-child(2) div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(1) .stButton>button {
        background: #10B981 !important;
        color: white !important;
        height: 48px;
    }
    /* Colonne Membre - S'inscrire (Bordure blanche haut de gamme) */
    div[data-testid="column"]:nth-child(2) div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(2) .stButton>button {
        background: transparent !important;
        color: #FFFFFF !important;
        border: 2px solid #FFFFFF !important;
        height: 48px;
    }

    /* Labels de formulaires forcés en blanc */
    label, p, span { color: #FFFFFF !important; }
    .humor-text { color: #94A3B8 !important; font-style: italic; font-size: 0.95rem; text-align: center; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- TRACKING DE SESSION ---
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "user_prefs" not in st.session_state:
    st.session_state.user_prefs = "Classique"

try:
    client_groq = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Clé GROQ_API_KEY manquante.")
    st.stop()

# --- EN-TÊTE IMMERSIF ---
st.markdown("<h1 class='brand-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Arrêtez de jeter les restes du frigo et transformez-les en une recette ultra-économique.</p>", unsafe_allow_html=True)

# --- DISPOSITION DES DEUX PANNEAUX ---
col_workspace, col_sidebar = st.columns([1.6, 1])

# --- PANNEAU GAUCHE : ESSAI DIRECT ---
with col_workspace:
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top:0; font-family:Playfair Display; font-size:1.8rem;'>🍳 Génération d'une recette délicieuse grâce à ce qu'il reste dans mon frigo !</h3>", unsafe_allow_html=True)
    
    if st.session_state.user_authenticated:
        st.markdown(f"<p style='color:#10B981; font-weight:700; margin-bottom:15px;'>● Profil Connecté : {st.session_state.user_email} ({st.session_state.user_prefs})</p>", unsafe_allow_html=True)
        
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
                
                st.markdown("<div class='glass-panel' style='background: rgba(15, 23, 42, 0.85) !important;'>", unsafe_allow_html=True)
                st.markdown("### 📋 Votre Protocole Anti-Gaspi")
                st.write(completion.choices[0].message.content)
                st.markdown("</div>", unsafe_allow_html=True)
                st.balloons()

# --- PANNEAU DROITE : ACCÈS CLIENTS ---
with col_sidebar:
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    
    if not st.session_state.user_authenticated:
        st.markdown("<h4 style='margin-top:0; font-size:1.3rem; letter-spacing:0.5px;'>🔐 ACCÈS MEMBRE PREMIUM</h4>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:0.9rem; color:#E2E8F0 !important;'>Entrez n'importe quel e-mail pour tester en direct l'interface utilisateur.</p>", unsafe_allow_html=True)
        
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
                    
        st.markdown("<p style='font-size:0.8rem; color:#94A3B8 !important; text-align:center; margin-top:20px; line-height:1.2;'>Note : L'intégration du module d'abonnement Stripe Premium est en cours de déploiement.</p>", unsafe_allow_html=True)
                    
    else:
        st.markdown("<h4 style='margin-top:0;'>⚙️ TABLEAU DE BORD</h4>", unsafe_allow_html=True)
        st.write(f"Utilisateur : **{st.session_state.user_email}**")
        
        st.session_state.user_prefs = st.selectbox("Votre profil de cuisson :", ["Classique", "Végétarien", "Économique Max", "Zéro Déchet Express"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Se déconnecter"):
            st.session_state.user_authenticated = False
            st.session_state.user_email = ""
            st.session_state.user_prefs = "Classique"
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

# Footer marketing
st.markdown("<p style='text-align: center; color: #E2E8F0 !important; font-size: 0.95rem; margin-top: 60px; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);'>Fini le gaspillage, place aux économies. Rejoignez la révolution culinaire intelligente.</p>", unsafe_allow_html=True)
