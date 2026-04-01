import requests

def reddit():
    url = "https://www.reddit.com/r/HistoryMemes/.json"
    result = requests.get(url)
    z = result.json()
    a = z['data']
    b = a['children']
    title = []
    url = []
    for i in range (10):
        c = b[i]
        d = c['data']
        if d['is_video'] == True:
            pass
        else:
            title.append(d['title'])
            url.append(d['url'])
    return title, url