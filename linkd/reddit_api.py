import requests
def search_reddit(topic):
    url = f"https://www.reddit.com/search.json?q={topic}&limit=5"
    headers = {
        "User-Agent": "python-cli-tool"
    }
    try:
        response=requests.get(url,
        headers=headers,
        timeout=10
        )
        data=response.json()
        posts=data["data"]["children"]
        return posts
    except requests.exceptions.RequestException as error:
        print(f"\n Reddit data fetching Error: {error}")
        return [] 
