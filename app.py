import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages.")

language_options = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi"
}

text_to_translate = st.text_area("Enter Text")

source_language = st.selectbox(
    "Select Source Language",
    list(language_options.keys())
)

target_language = st.selectbox(
    "Select Target Language",
    list(language_options.keys())
)

if st.button("Translate"):
    if text_to_translate.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated_text = GoogleTranslator(
            source=language_options[source_language],
            target=language_options[target_language]
        ).translate(text_to_translate)

        st.subheader("Translated Text")
        st.success(translated_text)