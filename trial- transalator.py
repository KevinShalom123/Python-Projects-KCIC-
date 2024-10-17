import requests
import uuid
import json
from nltk.translate.bleu_score import sentence_bleu

c_key = 'c2e5c006dc6e4f3aaa4fb8781448da41'
c_endpoint = 'https://api.cognitive.microsofttranslator.com/'
c_region = 'southeastasia'

print('Ready to utilize cognitive services in {} using key {}'.format(c_region, c_key))

def translate_text(c_region, c_key, txt, to_lang='fr', from_lang='en'):
    path = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0'
    params = '&from={}&to={}'.format(from_lang, to_lang)
    url = path + params

    headers = {
        'Ocp-Apim-Subscription-Key': c_key,
        'Ocp-Apim-Subscription-Region': c_region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': txt
    }]

    req = requests.post(url, headers=headers, json=body)
    resp = req.json()
    translated_text = resp[0]["translations"][0]["text"]
    return translated_text

# Reference translation for calculating BLEU score
reference_translation = "Je adore manger du shawarma."

txt_to_translate = "I adore consuming shawarma."

translation = translate_text(c_region, c_key, txt_to_translate, to_lang='fr', from_lang='en')
print('Original:', txt_to_translate)
print('Translated:', translation)
print('Reference:', reference_translation)

# Calculate BLEU score
bleu_score = sentence_bleu([reference_translation.split()], translation.split())
print('BLEU Score:', bleu_score)

