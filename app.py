import streamlit as st
import openai
import os

# Configura l'API key da secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

# Impostazioni della pagina
st.set_page_config(page_title="Voyager AI", page_icon="🧠")
st.title("🌍 Voyager AI")
st.write("Il tuo agente AI personale per scrivere articoli, pianificare viaggi e cercare informazioni.")

# Scelta del tipo di richiesta
task = st.selectbox("Cosa vuoi fare?", [
    "✍️ Scrivere un articolo",
    "🧭 Creare un itinerario di viaggio",
    "🔎 Fare una ricerca web"
])

# Area di input
prompt = st.text_ar_
