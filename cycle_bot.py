import requests, bs4, re
from urllib.parse import urljoin
start_url = 'http://www.racingaustralia.horse/'

def make_soup(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup

def get_links(url):
    soup = make_soup(url)
    a_tags = soup.find_all('a', href=re.compile(r"^/FreeFields/"))
    links = [urljoin(start_url, a['href'])for a in a_tags]  # convert relative url to absolute url
    return links

def get_tds(link):
    soup = make_soup(link)
    tds = soup.find_all('td',  class_="horse")
    if not tds:
        print(link, 'do not find hours tag')
    else:
        for td in tds:
            print(td.text)

if __name__ == '__main__':
    links = get_links(start_url)
    for link in links:
        get_tds(link)
