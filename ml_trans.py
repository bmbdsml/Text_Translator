import streamlit as st

from deep_translator import GoogleTranslator

# Title for the translation tool

st.title("Master ( Multi Language ) Localization Tool ")

# Dictionary mapping language names to their ISO codes

LANG_MAP = {
    "tamil": "ta",
    "hindi": "hi",
    "telugu": "te",
    "malayalam": "ml",
    "kannada": "kn",
    "marathi": "mr",
    "gujarati": "gu",
    "bengali": "bn",
    "urdu": "ur"
}

# User Interface for language selection

target_language = st.selectbox("Select the target language:", list(LANG_MAP.keys()))

# File uploader for the English text file

uploaded_file = st.file_uploader("Upload your English Master file", type=["txt"])

if uploaded_file is not None:
    
    # Read the content of the uploaded file
    
    english_content = uploaded_file.read().decode("utf-8")
    
    st.subheader("Original English Text")
    st.text(english_content)

    if st.button("Translate Now"):
        
        try:
            
            # Initialize translator and process text
            
            translator = GoogleTranslator(source='auto', target=LANG_MAP[target_language])
            
            # Handling potential long text by splitting if necessary 
            # (deep-translator handles standard text sizes well)
            
            translated_output = translator.translate(english_content)
            
            st.subheader(f"Translated Text ({target_language.capitalize()})")
            st.write(translated_output)
            
            # Option to download the translated text
            
            st.download_button(
            
                label="Download Translation",
                data=translated_output,
                file_name=f"translated_{target_language}.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            
            st.error(f"An error occurred: {e}")
