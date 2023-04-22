import requests
from bs4 import BeautifulSoup

article_content = []

cleaned_content_of_each_article = []


def clean_content(content: str):
    cleaned_content = []
    """badWord = ["<div class=\"detail__content\">", "<p>", "</p>",
               "<div class=\"serviceBox09 imf-boxes\" id=\"box1681772110211\">",
               "<div class=\"box-settings\"><span class=\"fal fa-cog boxes-settings\">",
               "</span>", "</div>", "<style>", "</style>"]"""
    a = 0
    while True:
        x = content.find("<p>", a)
        y = content.find("</p>", x)
        if x < 0:
            break
        else:
            cleaned_content.append(content[x + 3:y])
            a = y+1
    return cleaned_content


def get_article(link: str):
    content = requests.get(link)
    # print(content.text)
    soup = BeautifulSoup(content.content, 'html.parser')
    # get article content (<p> tag)
    found_content = soup.find_all("div", class_="detail__content")
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
            cleaned_content_of_each_article.append(clean_content(article_content[i]))

        # print(article_content[i])
        print(article_content[1])
        print(cleaned_content_of_each_article[1][0])
        print(len(cleaned_content_of_each_article[1]))
        print(len(cleaned_content_of_each_article))
        print('Continue?')
        check = input()
        if check == 'n':
            break
