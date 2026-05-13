import streamlit as st
from groq import Groq

# 1. Configuration du nom du site
st.set_page_config(page_title="AntiGaspi AI", page_icon="🥗")

st.title("🥗 AntiGaspi AI")
st.write("Écrivez vos ingrédients, je trouve une recette !")

# 2. Connexion automatique à ta clé secrète (définie dans les Secrets Streamlit)
try:
    ma_cle = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=ma_cle)
except Exception as e:
    st.error("Erreur de configuration : assure-toi d'avoir ajouté GROQ_API_KEY dans les Secrets de Streamlit.")
    st.stop()

# 3. Zone d'écriture pour les utilisateurs
ingredients = st.text_area("🛒 Vos ingrédients :", placeholder="Ex: riz, tomates, oeufs...")

# 4. Bouton pour lancer la recherche
if st.button("🍳 TROUVER MA RECETTE"):
    if not ingredients:
        st.warning("Écris d'abord tes ingrédients !")
    else:
        try:
            with st.spinner('L\'IA réfléchit...'):
                # L'IA prépare la réponse
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": "Fais une recette simple avec : " + ingredients}],
                    model="llama-3.3-70b-versatile"
                )
                
                # Affichage du résultat
                st.markdown("### ✨ Ta Recette :")
                st.write(chat_completion.choices[0].message.content)
                st.balloons()
        except Exception as e:
            st.error(f"Désolé, une erreur est survenue : {e}")
