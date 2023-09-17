import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile
import IPython.display as ipd

# Define a dictionary mapping language codes to full names
language_names = {
    "te": "Telugu",
    "fr": "French",
    "es": "Spanish",
    "bo": "Tibetan",
    "de": "German",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-CN": "Simplified Chinese",
    "ru": "Russian",
    "ar": "Arabic",
}

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def text_to_speech(text, target_language):
    tts = gTTS(text, lang=target_language)
    
    # Create a temporary file to save the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts.save(temp_audio.name)
        return temp_audio.name

st.title("Text Translator App")

# Get user input
user_input = st.text_area("Enter the text to translate:", "")
target_language_name = st.selectbox("Select the target language:", list(language_names.values()))

# Find the language code based on the selected language name
selected_language_code = [code for code, name in language_names.items() if name == target_language_name][0]

if st.button("Translate"):
    if user_input:
        translation = translate_text(user_input, selected_language_code)
        st.subheader("Translation:")
        st.write(translation)

        # Convert translation to speech
        audio_path = text_to_speech(translation, selected_language_code)
        st.audio(open(audio_path, 'rb').read(), format="audio/mp3")

    else:
        st.warning("Please enter some text to translate.")
