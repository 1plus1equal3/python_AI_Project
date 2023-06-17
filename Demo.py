import csv
import json
import math
from typing import List

import requests
from bs4 import BeautifulSoup
from pyvi import ViTokenizer
from collections import Counter

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
    str_list = list(article)
    i = 0
    while i != len(str_list):
        if str_list[i] == '<':
            while str_list[i] != '>':
                str_list[i] = ''
                i = i + 1
            if str_list[i] == '>':
                str_list[i] = ''
        i = i + 1
    res = ''.join(str_list)
    bad_word = ['.', ',', '(', ')', '...', '"', '+', ':']
    for i in bad_word:
        res = res.replace(i, '')
    return res


def split_word(article_text: str):
    words = ViTokenizer.tokenize(article_text)
    # link the word that containing 2-3 words by '_', return a string
    list_words = words.split()
    # split the string into meaning word in Vietnamese
    return list_words


def list_word(list_link: list):
    list_word = []
    for link in list_link:
        doc = clean_content(get_article(link))
        for word in split_word(doc):
            list_word.append(word)
    return list_word


def count_fre_in_article(list_word: list, word: str):
    count = 0
    if (word in list_word):
        for item in list_word:
            if (item == word):
                count = count + 1
    return count

def tf_idf(article_text: list):
    tf = {}
    words = Counter(article_text)
    length = len(article_text)
    for item in words:
        tf[item] = words[item]/length
    idf = {}
    with open('article.json','r') as file:
        articles = json.load(file)
    num_article = len(articles)
    for item in words:
        count = 0
        for article in articles:
            if item in article:
                count += 1
        idf[item] = math.log(num_article/(count+1))
    tf_idf = {}
    for item in words:
        tf_idf[item] = tf[item] * idf[item]
    return tf_idf

def read_csv_file(filename: str):
    sentiment_word = {}
    with open(filename, 'r',encoding='utf8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            key = row[0]
            value_str = row[1]
            value = float(value_str)
            sentiment_word[key] = value
    return sentiment_word

if __name__ == '__main__':

    print("Enter the link of the article: ")
    link = input()
    word_in_article = split_word(clean_content(get_article(link)))

    sentiment_words = {}
    sentiment_words = read_csv_file('sentiment_words.csv')
    tf_idf_article = tf_idf(word_in_article)

    vector = [0 for _ in range(len(sentiment_words))]
    i = -1
    pos_point = 0
    neg_point = 0
    neu_point = 0
    for item in sentiment_words:
        i = i + 1
        if (item in word_in_article):
            vector[i] = count_fre_in_article(word_in_article, item)
            if (sentiment_words[item] > 0.9):
                pos_point += sentiment_words[item] * vector[i] * tf_idf_article[item]
            elif (sentiment_words[item] < -1.0):
                neg_point -= sentiment_words[item] * vector[i] * tf_idf_article[item]
            else:
                neu_point += sentiment_words[item] * vector[i] * tf_idf_article[item]
    # print(vector)
    percent_pos = ((abs(pos_point)) / (abs(pos_point) + abs(neg_point) + abs(neu_point))) * 100
    percent_neg = ((abs(neg_point)) / (abs(pos_point) + abs(neg_point) + abs(neu_point))) * 100
    percent_neu = ((abs(neu_point)) / (abs(pos_point) + abs(neg_point) + abs(neu_point))) * 100
    print("Positive point: ", percent_pos, "%")
    print("Negative point: ", percent_neg, "%")
    print("Neutral point: ", percent_neu, "%")












