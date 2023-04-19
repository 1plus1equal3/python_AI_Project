import requests
from bs4 import BeautifulSoup
from google.cloud import language_v1
import six

article_content = []


def get_article(link: str):
    content = requests.get(link)
    # print(content.text)
    soup = BeautifulSoup(content.content, 'html.parser')
    # get article content (<p> tag)
    found_content = soup.find_all("div", class_="detail__content", )
    # print(soup.get_text())
    return str(found_content)


if __name__ == '__main__':
    check = True
    while check:
        baseUrl = 'https://vneconomy.vn/'
        links = []
        print("Enter company's name: ")
        company = input()
        url = 'https://search.hemera.com.vn/search/1/' + company + '/time/1'
        response = requests.get(url)
        # Get returned json object
        data = response.json()
        for i in range(0, 10):
            links.append(baseUrl + data['List'][i]['UrlArticle'] + '.htm')
            print(links[i])
            # Output all article's content to an array
            article_content.append(get_article(links[i]))
            print(article_content[i])

        print('Continue?')
        check = input()
        if check == 'n':
            break
