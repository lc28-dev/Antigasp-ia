import streamlit as st
from openai import OpenAI

# 1. Look du site (Mobile First)
st.set_page_config(page_title="AntiGaspi AI", page_icon="🥗")

st.markdown("""
    <style>
    .stApp { background-color: #f9f9f9; }
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 60px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Interface
st.title("🥗 AntiGaspi AI")
st.write("Cuisinez vos restes facilement !")

# Zone pour la clé API
with st.sidebar:
    st.header("⚙️ Réglages")
    api_key = st.text_input("Entre ta clé API OpenAI", type="password")

# Zone de saisie
ingredients = st.text_area("🛒 Liste tes ingrédients (ex: thon, riz, oeuf) :", height=150)

# 3. Logique
if st.button("🍳 TROUVER UNE RECETTE"):
    if not api_key:
        st.error("⚠️ Oublie pas ta clé API dans le menu à gauche !")
    elif not ingredients:
        st.warning("⚠️ Écris ce que tu as dans ton frigo !")
    else:
        try:
            client = OpenAI(api_key=api_key)
            with st.spinner('Le chef réfléchit...'):
                prompt = f"Crée une recette simple et rapide avec ces ingrédients : {ingredients}. Donne un titre et les étapes."
                
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
                
                st.markdown("### ✨ Ta Recette :")
                st.write(response.choices[0].message.content)
                st.balloons()
        except Exception as e:
            st.error(f"Erreur : {e}")
