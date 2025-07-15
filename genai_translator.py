import streamlit as st
from googletrans import Translator

# Initialize translator
translator = Translator()

# Language options (ISO 639-1 codes)
language_map = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Tamil": "ta",
    "Japanese": "ja",
    "Chinese": "zh-cn"
}

# Streamlit UI
st.set_page_config(page_title="🌍 Free Language Translator", layout="centered")
st.title("🌍 Free Language Translator using Google Translate")

source_lang = st.selectbox("From Language:", list(language_map.keys()), index=0)
target_lang = st.selectbox("To Language:", list(language_map.keys()), index=1)

text_input = st.text_area("Enter text to translate:")

if st.button("🔁 Translate"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating..."):
            try:
                result = translator.translate(
                    text_input,
                    src=language_map[source_lang],
                    dest=language_map[target_lang]
                )
                st.success("✅ Translation complete!")
                st.text_area("Translated Text:", value=result.text, height=150)
            except Exception as e:
                st.error(f"❌ Error: {e}")
