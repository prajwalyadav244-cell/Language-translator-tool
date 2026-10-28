# pip install streamlit deep-translator gtts
import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import io

st.set_page_config(page_title="CodeAlpha Translator")
st.title("🌐 Language Translation Tool - CodeAlpha")

text = st.text_area("Enter Text to Translate:")
langs = {'English':'en','Hindi':'hi','Marathi':'mr','Spanish':'es','French':'fr','German':'de','Japanese':'ja'}

col1, col2 = st.columns(2)
src = col1.selectbox("From", list(langs.keys()), index=0)
dest = col2.selectbox("To", list(langs.keys()), index=1)

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(source=langs[src], target=langs[dest]).translate(text)
        st.success(translated)
        st.write(f"Translated: {translated}")
        
        # Optional: Text-to-Speech
        tts = gTTS(translated, lang=langs[dest])
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        st.audio(buf, format='audio/mp3')
        
        # Optional: Copy button
        st.code(translated, language=None)
    else:
        st.warning("Please enter some text")
