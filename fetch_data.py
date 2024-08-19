import webbrowser

def google_search(keyword):
    search_url=f"https://www.google.com/search?q={keyword}"
    webbrowser.open(search_url)

if __name__== "__main__":
    print("welcome")
    while True:
        user_input= input("enter: ")
        if user_input.lower()=="exit":
            print("goodbye !")
            break;
        google_search(user_input)