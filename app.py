import streamlit as st
from groq import Groq

# 1. Configuration de la page
st.set_page_config(page_title="AntiGaspi AI | Solutions Alimentaires", page_icon="📈", layout="centered")

# 2. Design "Minimaliste Premium" (Style SaaS 2024)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Fond épuré */
    .stApp { background-color: #FFFFFF; }

    /* Barre de navigation simulée */
    .nav-bar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 20px 0; margin-bottom: 40px; border-bottom: 1px solid #F1F5F9;
    }
    .login-btn {
        background: #F8FAFC; padding: 8px 16px; border-radius: 6px;
        color: #0F172A; font-weight: 600; text-decoration: none; font-size: 0.9rem;
        border: 1px solid #E2E8F0;
    }

    /* Section Hero */
    .hero-title { 
        color: #0F172A; font-weight: 800; text-align: center; 
        font-size: 2.8rem; line-height: 1.1; margin-bottom: 15px;
    }
    .hero-subtitle { 
        text-align: center; color: #475569; font-size: 1.2rem;
        max-width: 600px; margin: 0 auto 40px auto;
    }

    /* Zone d'action principale */
    .main-card {
        background: #FFFFFF; padding: 40px; border-radius: 24px;
        border: 1px solid #E2E8F0; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.05);
        margin-bottom: 40px;
    }

    /* Bouton d'action massif */
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.8rem;
        background-color: #0F172A; color: white; font-weight: 700;
        font-size: 1.1rem; border: none; transition: all 0.2s ease;
        margin-top: 20px;
    }
    .stButton>button:hover { background-color: #1E293B; transform: translateY(-1px); }

    /* Témoignages sobres */
    .testimonial {
        font-style: italic; color: #475569; border-left: 3px solid #0F172A;
        padding-left: 20px; margin: 30px 0; font-size: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.markdown("""
    <div class='nav-bar'>
        <div style='font-weight:800; font-size:1.2rem; color:#0F172A;'>ANTIGASPI.AI</div>
        <a href='#' class='login-btn'>S'identifier / Créer un compte</a>
    </div>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("<h1 class='hero-title'>Ne gaspillez plus.<br>Cuisinez intelligemment.</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>L'intelligence artificielle au service de votre budget et de l'environnement.</p>", unsafe_allow_html=True)

# --- ZONE D'ACTION PRINCIPALE ---
with st.container():
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    
    st.markdown("### 🛠 Configurer votre analyse")
    
    col1, col2 = st.columns(2)
    with col1:
        regime = st.selectbox("Préférences", ["Aucune restriction", "Végétarien", "Vegan", "Sans Gluten", "Paléo"])
    with col2:
        budget = st.selectbox("Objectif Budget", ["Économique", "Standard", "Gastronomique"])

    # On met l'accent sur l'entrée des ingrédients
    ingredients = st.text_area("📋 Liste des ingrédients restants :", 
                               placeholder="Ex: 3 carottes, 1/2 oignon, reste de poulet...",
                               height=120)
    
    submit = st.button("LANCER L'OPTIMISATION CULINAIRE")
    st.markdown("</div>", unsafe_allow_html=True)

# --- LOGIQUE IA ---
if submit:
    if not ingredients:
        st.error("Veuillez saisir au moins un ingrédient pour lancer l'IA.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            with st.spinner('Analyse des combinaisons optimales...'):
                prompt = f"Expert culinaire. Recette {regime} budget {budget} avec : {ingredients}. Structure claire : Titre, Ingrédients, Instructions précises."
                completion = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
                
                st.markdown("### 💎 Votre Solution Sur-Mesure")
                st.success(completion.choices[0].message.content)
                
                # Option de sauvegarde (pour inciter à créer un compte)
                st.info("💡 **Voulez-vous enregistrer cette recette ?** Créez un compte pour retrouver vos préférences et vos historiques d'analyses.")
        except:
            st.error("Service momentanément indisponible.")

# --- PREUVE SOCIALE SOBRE ---
st.write("---")
st.markdown("#### Retours sur l'efficacité de la solution")

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""
        <div class='testimonial'>
            "Une approche pragmatique du gaspillage. Les recettes sont techniquement justes et adaptées au budget familial."
            <br><b>— Antoine M., Gestionnaire de patrimoine</b>
        </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown("""
        <div class='testimonial'>
            "Outil indispensable pour optimiser ses courses. La précision de l'IA sur les ingrédients de substitution est bluffante."
            <br><b>— Dr. Claire Lefebvre, Nutritionniste</b>
        </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 0.8rem; margin-top: 60px;'>AntiGaspi AI © 2024 - Technologie au service de la durabilité.</p>", unsafe_allow_html=True)
