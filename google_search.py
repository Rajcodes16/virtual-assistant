import pyttsx3
import requests
from bs4 import BeautifulSoup

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_google_search_results(query):
    try:
        url = f"https://www.google.com/search?q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error occurred while fetching search results: {e}")
        return None

def parse_google_search_results(html):
    soup = BeautifulSoup(html, "html.parser")
    search_results = soup.find_all("div", class_="tF2Cxc")
    return search_results

def main():
    speak("Hello! I am Jarvis, your virtual assistant. How can I help you?")
    while True:
        try:
            query = input("You: ").strip().lower()
            if query == "exit":
                speak("Goodbye!")
                break

            html = get_google_search_results(query)
            if html is not None:
                search_results = parse_google_search_results(html)
                if search_results:
                    result_text = search_results[0].text
                    print("Jarvis:", result_text)
                    speak(result_text)
                else:
                    print("Jarvis: No search results found.")
                    speak("Sorry, I couldn't find any relevant search results.")
            else:
                print("Jarvis: An error occurred while fetching search results.")
                speak("Sorry, an error occurred while fetching search results.")

        except KeyboardInterrupt:
            speak("Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("Sorry, something went wrong. Please try again.")

if __name__ == "__main__":
    main()