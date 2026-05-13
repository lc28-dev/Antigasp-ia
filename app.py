import streamlit as st
from groq import Groq

# 1. Configuration de la page
st.set_page_config(
    page_title="AntiGaspi AI",
    page_icon="🥗",
    layout="centered"
)

# 2. Design Personnalisé (CSS)
st.markdown("""
    <style>
    /* Fond de l'application */
    .stApp {
        background: linear-gradient(180deg, #F0F9FF 0%, #FFFFFF 100%);
    }
    
    /* Titre principal */
    h1 {
        color: #1E293B;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 800;
        text-align: center;
        padding-bottom: 0px;
    }
    
    /* Bouton principal */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5rem;
        background-color: #22C55E; /* Vert cuisine */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #16A34A;
        transform: translateY(-2px);
    }
    
    /* Zone de texte */
    .stTextArea textarea {
        border-radius: 12px;
        border: 1px solid #E2E8F0;
    }
    
    /* Carte de recette */
    .recipe-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #22C55E;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. En-tête
st.markdown("<h1>🥗 AntiGaspi AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B;'>Transformez vos restes en festin étoilé ✨</p>", unsafe_allow_html=True)

# 4. Connexion Groq
try:
    ma_cle = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=ma_cle)
except:
    st.error("🔑 Configuration de la clé API manquante.")
    st.stop()

# 5. Formulaire
st.write("---")
ingredients = st.text_area("🛒 Qu'avez-vous dans votre frigo ?", 
                           placeholder="Ex: 2 oeufs, un fond de crème, quelques champignons...",
                           help="Séparez les ingrédients par une virgule.")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    submit = st.button("🍳 Cuisiner maintenant")

# 6. Logique et Affichage
if submit:
    if not ingredients:
        st.warning("Veuillez entrer au moins un ingrédient !")
    else:
        try:
            with st.spinner('👨‍🍳 Le chef réfléchit à votre recette...'):
                prompt = f"""Tu es un chef cuisinier expert en anti-gaspillage. 
                Crée une recette appétissante en utilisant uniquement ou principalement ces ingrédients : {ingredients}.
                Structure ta réponse de la manière suivante :
                1. Un titre accrocheur avec un émoji.
                2. Temps de préparation et difficulté.
                3. Liste des ingrédients.
                4. Étapes de préparation numérotées.
                5. Une petite astuce du chef pour ne rien jeter."""
                
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile"
                )
                
                recette = chat_completion.choices[0].message.content
                
                st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
                st.markdown(recette)
                st.markdown('</div>', unsafe_allow_html=True)
                st.balloons()
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")

# Footer
st.markdown("<br><br><p style='text-align: center; color: #94A3B8; font-size: 12px;'>Fait avec ❤️ pour la planète</p>", unsafe_allow_html=True)
