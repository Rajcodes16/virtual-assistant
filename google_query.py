import webbrowser
import wikipedia as googlescrap
import pywhatkit

def google_search(keyword):
    search_url = f"https://www.google.com/search?q={keyword}"
    #webbrowser.open(search_url)
    print("this is what i found on the web")
    speak("this is what i found on the web")

    try:
        pywhatkit.search(keyword)
        result=googlescrap.summary(keyword,3)
        print(result)

    except:
        print("no speakable data available")
        
