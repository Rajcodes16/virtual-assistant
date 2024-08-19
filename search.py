import requests

def get_google_search_results(api_key, search_query):
    base_url = "https://www.googleapis.com/customsearch/v1"
    cx = "YOUR_CUSTOM_SEARCH_ENGINE_ID"  # Replace this with your Custom Search Engine ID
    params = {
        "key": api_key,
        "cx": cx,
        "q": search_query
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for errors

        data = response.json()
        search_results = data.get('items', [])
        
        return search_results
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

# Replace 'YOUR_API_KEY' with your actual API key obtained from the Google Developers Console.
api_key = "YOUR_API_KEY"
search_query = "Python programming"

results = get_google_search_results(api_key, search_query)

# Display the search results
if results:
    for idx, result in enumerate(results, 1):
        print(f"{idx}. {result['title']}: {result['link']}")
else:
    print("No search results found.")
