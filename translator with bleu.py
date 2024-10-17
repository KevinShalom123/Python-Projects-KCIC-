cog_key = 'c2e5c006dc6e4f3aaa4fb8781448da41'
cog_endpoint = 'https://api.cognitive.microsofttranslator.com/'
cog_region = 'southeastasia'

print('Ready to use cognitive services in {} using key {}'.format(cog_region, cog_key))

# Create a function that makes a REST request to the Text Translation service
def translate_text(cog_region, cog_key, text, to_lang='fr', from_lang='en'):
    import requests, uuid, json

    # Create the URL for the Text Translator service REST request
    path = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0'
    params = '&from={}&to={}'.format(from_lang, to_lang)
    constructed_url = path + params

    # Prepare the request headers with Cognitive Services resource key and region
    headers = {
        'Ocp-Apim-Subscription-Key': cog_key,
        'Ocp-Apim-Subscription-Region':cog_region,
        
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Add the text to be translated to the body
    body = [{
        'text': text
    }]

    # Get the translation
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    return response[0]["translations"][0]["text"]


# Function to calculate BLEU score
def calculate_bleu(reference, hypothesis):
    from nltk.translate.bleu_score import corpus_bleu
    return corpus_bleu([[reference.split()]], [hypothesis.split()])

# Test the function
text_to_translate = "I love to eat biriyani"
reference_translation = "J'adore manger du shawarma"

translation = translate_text(cog_region, cog_key, text_to_translate, to_lang='fr', from_lang='en')
print('{} -> {}'.format(text_to_translate, translation))

# Calculate BLEU score if translation is available
if translation:
    bleu_score = calculate_bleu(reference_translation, translation)
    print("BLEU score:", bleu_score)
