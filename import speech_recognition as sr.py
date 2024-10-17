import speech_recognition as sr
from jiwer import wer

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)  # Using Google Speech Recognition
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None

# Function to calculate Word Error Rate (WER)
def calculate_wer(reference, hypothesis):
    return wer(reference, hypothesis)

# Call the function to start speech recognition
recognized_text = speech_to_text()

# Example reference transcript
reference_transcript = "This is an example reference transcript."

# Calculate WER if recognized text is available
if recognized_text:
    wer_result = calculate_wer(reference_transcript, recognized_text)
    print("Word Error Rate:", wer_result)
