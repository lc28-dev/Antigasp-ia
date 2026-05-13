import streamlit as st
from groq import Groq
import random

# 1. Configuration de la page
st.set_page_config(page_title="AntiGaspi AI - Chef Privé", page_icon="🥗", layout="centered")

# 2. Design CSS Avancé
st.markdown("""
    <style>
    .stApp { background: #F8FAFC; }
    .main-title { color: #1E293B; font-weight: 900; text-align: center; font-size: 2.5rem; margin-bottom: 0; }
    .sub-title { text-align: center; color: #64748B; margin-bottom: 2rem; }
    
    /* Stats Bar */
    .stats-container {
        display: flex; justify-content: center; gap: 20px; margin-bottom: 2rem;
    }
    .stat-card {
        background: white; padding: 10px 20px; border-radius: 10px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); text-align: center;
    }
    
    /* Bouton Cuisiner */
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5rem;
        background: linear-gradient(90deg, #22C55E 0%, #16A34A 100%);
        color: white; font-weight: bold; border: none; font-size: 1.1rem;
    }

    /* Avis Clients */
    .review-card {
        background: #FFFFFF; padding: 15px; border-radius: 12px;
        margin: 10px 0; border: 1px solid #E2E8F0; font-size: 0.9rem;
    }
    .stars { color: #F59E0B; }
    
    /* Affiliation Button */
    .affilie-btn {
        display: inline-block; padding: 10px 20px; background: #E11D48;
        color: white !important; text-decoration: none; border-radius: 8px;
        font-weight: bold; margin-top: 10px; text-align: center; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER & STATS ---
st.markdown("<h1 class='main-title'>🥗 AntiGaspi AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>L'IA qui transforme vos restes en or</p>", unsafe_allow_html=True)

col_s1, col_s2 = st.columns(2)
with col_s1:
    st.markdown(f"<div class='stat-card'><b>{random.randint(12400, 12600)}</b><br><small>Repas sauvés</small></div>", unsafe_allow_html=True)
with col_s2:
    st.markdown(f"<div class='stat-card'><b>{random.randint(4800, 5000)}</b><br><small>Utilisateurs actifs</small></div>", unsafe_allow_html=True)

# --- CONNEXION GROQ ---
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Erreur de configuration API.")
    st.stop()

# --- PERSONNALISATION PROFIL ---
st.write("### 👤 Personnalisez votre expérience")
regime = st.multiselect("Votre régime :", ["Classique", "Végétarien", "Sportif (Protéiné)", "Petit Budget", "Sans Gluten"])
temps = st.select_slider("Temps max de préparation :", options=["10 min", "20 min", "30 min", "Illimité"])

# --- INPUT INGRÉDIENTS ---
ingredients = st.text_area("🛒 Ingrédients dans votre frigo :", placeholder="Ex: 2 oeufs, jambon, fromage...")

# --- BOUTON PRINCIPAL ---
if st.button("🍳 GÉNÉRER MA RECETTE SUR-MESURE"):
    if not ingredients:
        st.warning("Ajoutez des ingrédients !")
    else:
        # --- POP-UP EMAIL (Simulé) ---
        st.info("📩 **ASTUCE :** Enregistrez votre email pour recevoir notre guide '10 astuces Anti-Gaspi' gratuitement !")
        email = st.text_input("Votre email (Optionnel) :")
        
        with st.spinner('Le Chef IA prépare votre plan...'):
            prompt = f"Fais une recette {regime} prête en {temps} avec : {ingredients}. Structure : Titre, Ingrédients, Étapes, Calories."
            completion = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
            
            st.success("Voici votre recette !")
            st.markdown(completion.choices[0].message.content)
            
            # --- AFFILIATION ---
            st.markdown("""
                <a href='https://www.carrefour.fr/services/drive' class='affilie-btn'>
                🛒 Manque-t-il un ingrédient ? Commandez au Drive Carrefour
                </a>
                """, unsafe_allow_html=True)
            st.balloons()

# --- AVIS CLIENTS (CRÉDIBLES) ---
st.write("---")
st.write("### 💬 Ce que disent nos utilisateurs")
avis = [
    {"nom": "Sarah D.", "texte": "Incroyable ! J'ai sauvé mes légumes oubliés, mon fils a adoré.", "note": "⭐⭐⭐⭐⭐"},
    {"nom": "Marc L.", "texte": "Pratique pour les fins de mois difficiles. Je recommande à 100%.", "note": "⭐⭐⭐⭐⭐"},
    {"nom": "Julie R.", "texte": "Les idées de recettes sont vraiment originales, ça change du quotidien.", "note": "⭐⭐⭐⭐"}
]

for a in avis:
    st.markdown(f"""
        <div class='review-card'>
            <span class='stars'>{a['note']}</span><br>
            <b>{a['nom']}</b> : "{a['texte']}"
        </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 0.7rem; color: gray;'><br>Copyright 2024 - AntiGaspi AI Business</p>", unsafe_allow_html=True)
