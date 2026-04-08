import requests
from bs4 import BeautifulSoup

def history():
    url = "https://www.history.com"

    r = requests.get(url)
    res = r.status_code
    soup = BeautifulSoup(r.text, 'html.parser')
    a = soup.find_all(class_="z91jpy0 _1jnz0oc1y zu4ptk0 g1fwxflr")

    title = []
    link = []

    for i in range(2):
        title1 = a[i].find("h3").string
        link1 = a[i].get('href')
        title.append(title1)
        link.append(link1)
    return title, link

if __name__ == "__main__":
    res = history()
    print(res)