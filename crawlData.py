import requests
from bs4 import BeautifulSoup
from pyvi import ViTokenizer

article_content = []

cleaned_content_of_each_article = []


def get_article(link: str):
    content = requests.get(link)
    # print(content.text)
    soup = BeautifulSoup(content.content, 'html.parser')
    # get article content (<p> tag)
    found_content = soup.find_all("div", class_="detail__content")
    # print(soup.get_text())
    return str(found_content)


def clean_content(article: str):
    str_list=list(article)
    i=0
    while i != len(str_list):
        if str_list[i] == '<':
            while str_list[i] != '>':
                str_list[i] = ''
                i=i+1
            if str_list[i] == '>':
                str_list[i] =''
        i=i+1
    res=''.join(str_list)
    bad_word=['.',',','(',')','...','"']
    for i in bad_word:
        res=res.replace(i,'')
    return res

def split_word(article_text: str):
    words=ViTokenizer.tokenize(article_text)
    #link the word that containing 2-3 words by '_', return a string
    list_words=words.split()
    #split the string into meaning word in Vietnamese
    return list_words


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

        #print(type(article_content[1]))#article content =>string
        
        print(split_word(cleaned_content_of_each_article[1]))
        #Test
        print('Continue?')
        check = input()
        if check == 'n':
            break
