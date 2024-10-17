cog_key = '0937d738fba24beaa9a2b2d69d4b3b5a'
cog_endpoint = 'https://eastasia.api.cognitive.microsoft.com/'
cog_region = 'eastasia'

print('Ready to use cognitive services in {} using key {}'.format(cog_region, cog_key))

import os
import IPython
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig

# Get spoken command from audio file
file_name = 'light-on.wav'
audio_file = os.path.join('data', 'speech', file_name)

# Configure speech recognizer
speech_config = SpeechConfig(cog_key, cog_region)
audio_config = AudioConfig(filename=audio_file) # Use file instead of default (microphone)
speech_recognizer = SpeechRecognizer(speech_config, audio_config)

# Use a one-time, synchronous call to transcribe the speech
speech = speech_recognizer.recognize_once()

# Play audio and show transcribed text
IPython.display.display(IPython.display.Audio(audio_file, autoplay=True),
                        IPython.display.HTML(speech.text))
