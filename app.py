import streamlit as st
from groq import Groq

# 1. Look du site (Mobile First)
st.set_page_config(page_title="AntiGaspi AI (Groq)", page_icon="🥗")

st.markdown("""
    <style>
    .stApp { background-color: #f9f9f9; }
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 60px;
        background-color: #f6521e; /* Couleur Groq */
        color: white;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Interface
st.title("🥗 AntiGaspi AI")
st.write("Cuisinez vos restes gratuitement avec Groq !")

# Zone pour la clé API
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input("Entre ta clé API Groq (gsk_...)", type="password")
    st.info("Obtiens ta clé gratuite sur console.groq.com")

# Zone de saisie
ingredients = st.text_area("🛒 Ce qu'il reste dans ton frigo :", height=150)

# 3. Logique Groq
if st.button("🍳 TROUVER UNE RECETTE"):
    if not api_key:
        st.error("⚠️ Oublie pas ta clé API Groq dans le menu à gauche !")
    elif not ingredients:
        st.warning("⚠️ Écris ce que tu as dans ton frigo !")
    else:
        try:
            # Initialisation du client Groq
            client = Groq(api_key=api_key)
            
            with st.spinner('L\'IA de Groq cuisine pour vous...'):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"Crée une recette simple avec ces ingrédients : {ingredients}. Donne un titre et les étapes.",
                        }
                    ],
                    model="llama3-8b-8192", # Modèle gratuit et super rapide
                )
                
                recette = chat_completion.choices[0].message.content
                st.markdown("### ✨ Ta Recette Express :")
                st.write(recette)
                st.balloons()
        except Exception as e:
            st.error(f"Erreur Groq : {e}")

st.divider()
st.caption("AntiGaspi AI x Groq - Zéro frais, Zéro déchet.")
