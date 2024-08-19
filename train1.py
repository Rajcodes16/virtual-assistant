import speech_recognition as sr

def process_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
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

def main():
    r = sr.Recognizer()
    is_listening = False

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            wake_word = r.recognize_google(audio).lower()
            if "hey jarvis" in wake_word:
                if not is_listening:
                    print("Jarvis is now listening. Say your command.")
                    is_listening = True
                    process_command()
                    is_listening = False
            else:
                print("Waiting for 'Hey Jarvis' wake-up phrase...")
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Error occurred while processing audio.")

if __name__ == "__main__":
    print("Starting Jarvis...")
    main()