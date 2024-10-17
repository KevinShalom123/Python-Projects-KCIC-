import speech_recognition as sr

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
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# Call the function to start speech recognition
speech_to_text()

