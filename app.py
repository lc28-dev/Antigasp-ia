import streamlit as st
from groq import Groq

# 1. Configuration Pro
st.set_page_config(page_title="AntigaspIA | Espace Premium", page_icon="🍽️", layout="wide")

# 2. Design "Luxe & Dashboard"
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&family=Playfair+Display:wght@700&display=swap');
    
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.96), rgba(15, 23, 42, 0.98)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #FFFFFF;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .brand-title { font-family: 'Playfair Display', serif; font-size: 3.5rem; text-align: center; margin-top: 30px; }
    .brand-subtitle { text-align: center; color: #94A3B8; font-size: 1rem; margin-bottom: 40px; }

    /* Boite d'action blanche */
    .glass-panel {
        background: #FFFFFF;
        color: #1E293B;
        padding: 35px;
        border-radius: 16px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }

    /* Bouton principal */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 55px;
        background-color: #0F172A;
        color: #FFFFFF;
        font-weight: 700;
        text-transform: uppercase;
        border: none;
        transition: 0.2s;
    }
    .stButton>button:hover { background-color: #D9A139; color: #0F172A; }

    .stTextArea textarea { border-radius: 8px; border: 2px solid #E2E8F0; }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialisation des variables de session (Simulation)
if "user_authenticated" not in st.session_state:
    st.session_state.user_authenticated = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "user_prefs" not in st.session_state:
    st.session_state.user_prefs = "Classique"

# Vérification uniquement de la clé Groq
try:
    client_groq = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("🔑 Clé GROQ_API_KEY manquante ou incorrecte dans vos secrets Streamlit.")
    st.stop()

# --- HEADER ---
st.markdown("<h1 class='brand-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>Plateforme d'optimisation alimentaire propulsée par l'intelligence artificielle.</p>", unsafe_allow_html=True)

# --- ARCHITECTURE EN COLONNES ---
col_workspace, col_sidebar = st.columns([1.6, 1])

# --- COLONNE GAUCHE : ESSAI ET RECETTE ---
with col_workspace:
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top:0;'>📋 Analyse instantanée de vos restes</h3>", unsafe_allow_html=True)
    
    # Statut utilisateur dynamique
    if st.session_state.user_authenticated:
        st.markdown(f"<small style='color:#22C55E; font-weight:bold;'>● Connecté : {st.session_state.user_email} (Profil : {st.session_state.user_prefs})</small>", unsafe_allow_html=True)
    else:
        st.markdown("<small style='color:#64748B;'>○ Mode invité (Créez un compte à droite pour tester l'espace membre)</small>", unsafe_allow_html=True)
        
    ingredients = st.text_area("", placeholder="Listez vos ingrédients ici (ex: 2 blancs de poulet, crème fraîche, oignon...)", height=150, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.button("Générer ma fiche recette")
    st.markdown("</div>", unsafe_allow_html=True)

    if submit:
        if not ingredients:
            st.warning("Veuillez saisir vos ingrédients.")
        else:
            with st.spinner('Le Chef IA élabore votre protocole culinaire...'):
                # L'IA adapte la recette si l'utilisateur a configuré ses préférences
                regime_context = st.session_state.user_prefs if st.session_state.user_authenticated else "Aucune restriction"
                
                prompt = f"Tu es AntigaspIA, un chef de palace. Crée une recette stricte de niveau professionnel adaptée au profil ({regime_context}) avec uniquement ou principalement : {ingredients}. Structure avec Titre, Ingrédients, Instructions pas à pas."
                
                completion = client_groq.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("### 🍽️ Fiche Technique Exclusive")
                st.info(completion.choices[0].message.content)
                st.balloons()

# --- COLONNE DROITE : ESPACE MEMBRE SIMULÉ ---
with col_sidebar:
    st.markdown("<div style='background-color:#1E293B; padding:30px; border-radius:16px; border:1px solid #334155;'>", unsafe_allow_html=True)
    
    if not st.session_state.user_authenticated:
        st.markdown("<h4 style='color:white; margin-top:0;'>🔐 ACCÈS MEMBRE PREMIUM</h4>", unsafe_allow_html=True)
        st.write("Entrez n'importe quel e-mail pour tester l'interface utilisateur.")
        
        email_input = st.text_input("Adresse Email", placeholder="chef@exemple.com")
        password_input = st.text_input("Mot de passe", type="password")
        
        col_btn_a, col_btn_b = st.columns(2)
        with col_btn_a:
            if st.button("S'identifier"):
                if email_input:
                    st.session_state.user_authenticated = True
                    st.session_state.user_email = email_input
                    st.rerun()
                else:
                    st.warning("Entrez un email.")
        with col_btn_b:
            if st.button("S'inscrire"):
                if email_input:
                    st.success("Compte simulé créé ! Cliquez sur S'identifier.")
                    
    else:
        st.markdown("<h4 style='color:white; margin-top:0;'>⚙️ VOTRE PROFIL</h4>", unsafe_allow_html=True)
        st.write(f"Bonjour, **{st.session_state.user_email}**")
        
        # Enregistrement et changement en temps réel des préférences
        st.session_state.user_prefs = st.selectbox("Votre régime alimentaire :", ["Classique", "Végétarien", "Sportif (Protéines)", "Sans Gluten"])
        
        st.success("Préférences synchronisées en direct.")
        
        if st.button("Se déconnecter"):
            st.session_state.user_authenticated = False
            st.session_state.user_email = ""
            st.session_state.user_prefs = "Classique"
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 0.8rem; margin-top: 100px;'>© 2024 AntigaspIA - Infrastructure Cloud Sécurisée.</p>", unsafe_allow_html=True)
