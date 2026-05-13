import streamlit as st
from groq import Groq

# Config de la page
st.set_page_config(page_title="AntiGaspi AI")

st.title("🥗 AntiGaspi AI")

# Sidebar pour la clé
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Clé API Groq", type="password")

# Entrée texte
ingredients = st.text_area("Ingrédients (ex: riz, oeufs)")

# Bouton
if st.button("🍳 TROUVER UNE RECETTE"):
    if not api_key:
        st.error("Ajoute ta clé API dans le menu à gauche !")
    elif not ingredients:
        st.warning("Écris tes ingrédients !")
    else:
        try:
            client = Groq(api_key=api_key)
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"Fais une recette avec : {ingredients}"}]
            )
            st.markdown("### ✨ Ta Recette :")
            st.write(completion.choices[0].message.content)
        except Exception as e:
            st.error(f"Erreur : {e}")
