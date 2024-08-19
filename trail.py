import speech_recognition as sr

def listen_for_wake_word():
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening for 'Hey Jarvis'...")
            audio = r.listen(source)

        try:
            wake_word = r.recognize_google(audio).lower()
            if "hey jarvis" in wake_word:
                print("Jarvis is now listening. Say your command.")
                process_command()
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Error occurred while processing audio.")

def process_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)

        # Here, you can add logic to execute the appropriate commands based on 'command'.
        # For example, you can implement if-else conditions to handle different commands.

        print("Command executed.")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that. Please repeat your command.")
    except sr.RequestError:
        print("Error occurred while processing audio.")

if __name__ == "__main__":
    print("Starting Jarvis...")
    listen_for_wake_word()