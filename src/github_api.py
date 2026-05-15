import requests

def search_github(topic):
    url=f"https://api.github.com/search/repositories?q={topic}&per_page=3"
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()

        data=response.json()

        return data["items"]
    except requests.exceptions.RequestException as error:
        print(f"\n Github Api Error:{error}")
        return []    
