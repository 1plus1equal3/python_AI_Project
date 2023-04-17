import requests
from bs4 import BeautifulSoup


def get_article(link: str):
    content = requests.get(link)
    # print(content.text)
    soup = BeautifulSoup(content.content, 'html.parser')
    # get article content (<p> tag)
    article_content = soup.find_all("div", "detail__content")
    print(article_content)


if __name__ == '__main__':
    baseUrl = 'https://vneconomy.vn/'
    links = []
    company = input()
    url = 'https://search.hemera.com.vn/search/1/' + company + '/time/1'
    response = requests.get(url)
    # Get returned json object
    data = response.json()
    for i in range(0, 10):
        links.append(baseUrl + data['List'][i]['UrlArticle'] + '.htm')
        print(links[i])
    get_article(links[0])
