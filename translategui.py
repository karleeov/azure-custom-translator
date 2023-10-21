import requests
import uuid
import json
import streamlit as st

# Add your key and endpoint
key = "d60fc21f5d5c4afe952d62caddce9672"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "Global"
path = '/translate'
constructed_url = endpoint + path

lang_options = {
    "Chinese (Traditional)": "zh-Hant",
    "English": "en"
}

# Streamlit UI
st.title("GTI HKJC Translator")
text_to_translate = st.text_area("Enter the text to translate:")
selected_lang = st.selectbox("Select Language:", list(lang_options.keys()))

if st.button("Translate"):
    params = {
        'api-version': '3.0',
        'to': [lang_options[selected_lang]],
        'category': 'd992f74e-7588-4f96-b547-bb396ddb4ada-SPORTS'
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text_to_translate
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    st.json(response)

