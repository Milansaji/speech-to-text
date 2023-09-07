import speech_recognition as sr
from gtts import gTTS

recognizer = sr.Recognizer()  # Corrected the typo in 'recognizer'

while True:
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = recognizer.listen(source)
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if 'ad' in command:
            print(command)
            
        if 'stop' in command:
            print("stopped Listening...")
            break

    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
