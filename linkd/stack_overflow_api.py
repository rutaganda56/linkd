import requests

def get_stackOverFlowData(topic):
    url=f"https://stackoverflow.com/search?q={topic}"

    try:
        params={
            "order":"desc",
            "sort":"votes",
            "intitle":topic,
            "site":"stackoverflow"
        }
        response = requests.get(url,params=params,timeout=10)
        response.raise_for_status()

        data = response.json()

        return data.get('items',[])[:5]
    except requests.exceptions.RequestException as error:
        print(f"\n Stackoverflow error:{error}") 
        return []   
