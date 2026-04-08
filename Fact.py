import requests

def fact():
    url = "https://today.zenquotes.io/api"

    a = requests.get(url)
    b = a.json()
    return b['data']['Events'][0]['text']

if __name__ == "__main__":
    fact = fact()
    print(fact)