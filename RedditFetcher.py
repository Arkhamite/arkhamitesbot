import requests
from fake_useragent import UserAgent

def get_browser_headers():
    ua = UserAgent()
    return {
        'User-Agent': ua.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0',
    }

def reddit():
    url = "https://www.reddit.com/r/HistoryMemes/.json"
    proxy = {"http": "http://84.17.47.150:9002"}
    headers = get_browser_headers()
    result = requests.get(url, headers=headers, proxies=proxy)
    status = result.status_code
    if status == 200:
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
    else:
        return status

if __name__ == "__main__":
    a = reddit()
    if type(a) == tuple:
        print(type(a))
        title, url = a
        print(title)
    else:
        print(type(a))
        print(a)