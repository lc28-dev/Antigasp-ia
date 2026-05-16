import streamlit as st
from groq import Groq

# 1. Configuration Pro
st.set_page_config(page_title="AntigaspIA | Haute Cuisine Circulaire", page_icon="🍽️", layout="wide")

# 2. Design Visuel Immersif (Style SaaS Pro)
# On utilise une image de fond réaliste, des cartes, et des contrastes forts.
# L'image de fond est une cuisine pro sombre, propre et réaliste.
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&family=Playfair+Display:wght@700&display=swap');
    
    /* Fond Immersif (Cuisine sombre/pro) */
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.95), rgba(15, 23, 42, 0.98)), 
                          url('https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #FFFFFF;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* En-tête */
    .brand-title {
        font-family: 'Playfair Display', serif;
        color: #FFFFFF;
        font-size: 3.8rem;
        font-weight: 800;
        text-align: center;
        margin-top: 50px;
        letter-spacing: -2px;
    }
    .brand-subtitle {
        text-align: center;
        color: #94A3B8;
        font-size: 1.1rem;
        max-width: 600px;
        margin: 0 auto 50px auto;
        opacity: 0.8;
    }

    /* Bloc de Saisie Central */
    .action-container {
        background-color: #FFFFFF;
        color: #1E293B;
        max-width: 800px;
        margin: 0 auto 40px auto;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);
    }

    /* Style du bouton d'action principal */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 65px;
        background-color: #0F172A; /* Bleu nuit pro */
        color: #FFFFFF;
        font-weight: 700;
        font-size: 1.1rem;
        text-transform: uppercase;
        border: none;
        transition: background 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #D9A139; /* Jaune moutarde au survol */
        color: #0F172A;
    }

    /* Style des zones de texte */
    .stTextArea textarea {
        border-radius: 8px;
        border: 2px solid #CBD5E1;
        padding: 15px;
    }

    /* Carte d'option (Simulé Firebase) */
    .pref-card {
        background-color: #1E293B;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin: 10px;
        text-align: center;
    }
    .pref-title { color: #FFFFFF; font-weight: 700; margin-bottom: 5px; }
    .pref-desc { color: #94A3B8; font-size: 0.85rem; }
    
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION & CONNEXION (Simulé API Supabase/Firebase) ---
col_n1, col_n2, col_n3 = st.columns([1,2,1])
with col_n3:
    st.write("---") # Ligne pour l'espace sur mobile
    st.button("🔑 S'identifier / Compte Pro", help="Intégration d'API type Supabase/Firebase gratuite au début")

# --- TITRE & SOUS-TITRE ---
st.markdown("<h1 class='brand-title'>AntigaspIA</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>L'excellence culinaire au service de vos restes. Solution professionnelle pour particuliers exigeants.</p>", unsafe_allow_html=True)

# --- ZONE D'ESSAI DIRECT (CE QUI SAUTE AUX YEUX) ---
with st.container():
    st.markdown("<div class="action-container">", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; font-family:Playfair Display; font-size:1.8rem;'>Faites le test instantané</h2>", unsafe_allow_html=True)
    st.write("Dites-moi simplement ce qu'il reste dans votre cuisine.")
    
    ingredients = st.text_area("", placeholder="Ex: Un fond de crème, 2 oeufs, reste de quinoa...", label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    submit = st.button("Lancer l'analyse culinaire")
    
    st.markdown("<p style='text-align:center; font-size:0.8rem; color:#64748B; margin-top:15px;'>Usage gratuit • Résultat basé sur la haute gastronomie</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- CONNEXION GROQ ET LOGIQUE IA ---
if submit:
    if not ingredients:
        st.warning("Veuillez renseigner vos ingrédients.")
    else:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            with st.spinner('L\'IA prépare votre recette exclusive...'):
                prompt = f"Tu es un chef cuisinier de luxe. Crée une recette unique avec ces ingrédients : {ingredients}. Structure avec Titre accrocheur, Ingrédients précis, Étapes et un conseil antigaspillage."
                completion = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.3-70b-versatile")
                
                recette_finale = completion.choices[0].message.content
                
                st.markdown("---")
                st.markdown("### 📋 Fiche Recette du Chef")
                st.info(recette_finale)
                
                # --- AFFILIATION drive ---
                st.markdown("""
                    <div style='text-align:center;'>
                        <a href='https://www.carrefour.fr/services/drive' style='display:inline-block; padding: 12px 24px; background:#D9A139; color:#0F172A; text-decoration:none; border-radius:5px; font-weight:bold; margin-top:10px;'>
                            🛒 Commander les ingrédients manquants (Drive Carrefour)
                        </a>
                    </div>
                    """, unsafe_allow_html=True)
                
                # --- EXEMPLE INTÉGRATION API IMAGE (PAYANT PLUS TARD) ---
                # image_url = app_image_api.generate(recette_finale)
                # st.image(image_url, caption="Photo de votre plat (API image en option)")
                st.balloons()
        except Exception as e:
            st.error(f"Erreur serveur : {e}")

# --- SECTION OPTIONS (SIMULATION API CONNEXION/PRÉFÉRENCES) ---
st.write("---")
st.markdown("### 👥 Votre Profil Privé (Intégration API de Connexion)")
st.write("Sauvegardez vos données, historique et préférences culinaires en créant un compte (Exemple d'intégration type Firebase gratuite au début).")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class='pref-card'>
            <div class='pref-title'>HistoriIA</div>
            <div class='pref-desc'>Retrouvez vos 50 dernières créations culinaires.</div>
        </div>
        """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='pref-card'>
            <div class='pref-title'>Profil NutritionIA</div>
            <div class='pref-desc'>Sauvegardez vos préférences (Végé, Sportif, Sans Gluten).</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.button("📦 CRÉER MON PROFIL DE CHEF")

# Footer
st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 0.8rem; margin-top: 80px;'>© 2024 AntigaspIA Technologies - L'Excellence & la Durabilité Culinaires.</p>", unsafe_allow_html=True)

 
