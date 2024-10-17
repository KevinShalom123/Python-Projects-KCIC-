from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError
from jiwer import wer  # Install jiwer library to calculate WER

# Initialize the speech recognizer
recognizer = Recognizer()

# Ground truth transcription (replace with your actual ground truth)
ground_truth_transcription = "This is a sample ground truth transcription."

# Function to perform speech recognition
def speech_to_text():
    with Microphone() as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)  # Using Google Speech Recognition
            print("You said:", text)
            return text
        except UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return None
        except RequestError as e:
            print("Could not request results; {0}".format(e))
            return None

# Call the function to start speech recognition
recognized_text = speech_to_text()

# Calculate Word Error Rate (WER)
wer_score = wer(ground_truth_transcription, recognized_text)

# Calculate accuracy
accuracy = 1 - wer_score

# Output results
print("Word Error Rate (WER):", wer_score)
print("Accuracy:", accuracy)
