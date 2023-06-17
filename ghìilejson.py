import math
from typing import List

import requests
from bs4 import BeautifulSoup
from pyvi import ViTokenizer
from collections import Counter
import json

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


if __name__ == '__main__':

    positiveLinks: list[str] = []
    negativeLinks: list[str] = []
    neutralLinks: list[str] = []
    posWords = []
    negWords = []
    neuWords = []
    bagWord = []
    positiveLinks.append("https://vneconomy.vn/dai-gia-game-vng-rot-22-5-trieu-usd-vao-funding-societies.htm")
    positiveLinks.append("https://vneconomy.vn/start-up-telio-nhan-22-5-trieu-usd-tu-vng.htm")
    positiveLinks.append("https://vneconomy.vn/vietcombank-xung-danh-don-vi-anh-hung.htm")
    positiveLinks.append("https://vneconomy.vn/vietcombank-60-nam-thap-sang-niem-tin-vuon-ra-bien-lon.htm")
    positiveLinks.append("https://vneconomy.vn/nhieu-uu-dai-lai-suat-cho-khach-hang-vay-von-tai-vietcombank-trong-thang-3-2023.htm")
    positiveLinks.append("https://vneconomy.vn/vietcombank-va-jcb-ra-mat-the-tin-dung-quoc-te-vietcombank-jcb-platinum.htm")
    positiveLinks.append("https://vneconomy.vn/vietcombank-giu-vung-vi-tri-ngan-hang-so-1.htm")
    positiveLinks.append("https://vneconomy.vn/bat-tay-doanh-nghiep-nhat-vinamilk-khoi-cong-to-hop-chan-nuoi-che-bien-bo-thit-500-trieu-usd.htm")
    positiveLinks.append("https://vneconomy.vn/tang-18-ve-gia-tri-thuong-hieu-vinamilk-dan-dau-cac-bang-xep-hang-lon-nganh-sua.htm")
    positiveLinks.append("https://vneconomy.vn/gia-nguyen-lieu-dau-vao-giam-tao-loi-the-cho-vinamilk.htm")
    positiveLinks.append("https://vneconomy.vn/gia-nguyen-lieu-dau-vao-giam-tao-loi-the-cho-vinamilk.htm")
    positiveLinks.append("https://vneconomy.vn/tang-18-ve-gia-tri-thuong-hieu-vinamilk-dan-dau-cac-bang-xep-hang-lon-nganh-sua.htm")
    positiveLinks.append("https://vneconomy.vn/vinamilk-doanh-thu-quy-3-2022-on-dinh-dong-tien-tu-hoat-dong-kinh-doanh-cai-thien.htm")
    positiveLinks.append("https://vneconomy.vn/mi-hao-hao-san-pham-viet-ngay-cang-vuon-ra-thuong-truong-chau-a.htm")
    positiveLinks.append("https://vneconomy.vn/viettel-global-lai-truoc-thue-gan-1-000-ty-trong-quy-1-2023.htm")
    positiveLinks.append("https://vneconomy.vn/doanh-thu-hop-nhat-cua-viettel-global-lan-dau-vuot-1-ty-usd-lai-truoc-thue-hon-3-000-ty-nam-2022.htm")
    positiveLinks.append("https://vneconomy.vn/viettel-tham-vong-vao-top-60-doanh-nghiep-quoc-phong-hang-dau-the-gioi-vao-nam-2030.htm")
    positiveLinks.append("https://vneconomy.vn/viettel-global-dat-hon-3-000-ty-dong-loi-nhuan-truoc-thue-nam-2022.htm")
    positiveLinks.append("https://vneconomy.vn/nam-dau-tien-viettel-hoat-dong-duoi-su-dieu-hanh-cua-the-he-lanh-dao-moi.htm")
    positiveLinks.append("https://vneconomy.vn/nam-trong-tay-1-000-ty-tien-mat-suc-khoe-viettel-construction-ra-sao.htm")
    positiveLinks.append("https://vneconomy.vn/viettel-cyber-security-ngan-chan-2-cuoc-tan-cong-ddos-lon-vao-thi-truong-chung-khoan-viet.htm")
    positiveLinks.append("https://vneconomy.vn/loi-nhuan-truoc-thue-quy-3-cua-viettel-global-dat-gan-2-400-ty-tang-5-lan-cung-ky.htm")
    positiveLinks.append("https://vneconomy.vn/viettel-6-nam-lien-tuc-la-doanh-nghiep-nop-thue-lon-nhat-viet-nam.htm")
    positiveLinks.append("https://vneconomy.vn/viettel-bung-no-suc-manh-khi-lop-tre-duoc-trao-quyen.htm")
    positiveLinks.append("https://vneconomy.vn/viettel-global-dat-muc-loi-nhuan-truoc-thue-gan-3-200-ty-dong-trong-nua-dau-nam-gap-3-5-lan-cung-ky.htm")
    positiveLinks.append("https://vneconomy.vn/hanh-trinh-15-nam-tu-nha-dau-tu-den-doanh-nghiep-duoc-dia-phuong-tin-tuong.htm")
    positiveLinks.append("https://vneconomy.vn/galaxy-z-series-chi-la-buoc-dem-de-cho-cong-nghe-cua-samsung.htm")
    positiveLinks.append("https://vneconomy.vn/samsung-electronics-co-quy-lai-ky-luc-nho-chip-nho.htm")
    positiveLinks.append("https://vneconomy.vn/ford-samsung-nam-trong-nhom-nhan-duoc-nhieu-tro-cap-nhat-tai-my-nam-2021.htm")
    positiveLinks.append("https://vneconomy.vn/nam-2023-techcombank-dieu-chinh-muc-tieu-loi-nhuan-22-000-ti-dong-top-dau-toan-nganh-ve-car-va-von-chu-so-huu.htm")
    positiveLinks.append("https://vneconomy.vn/nam-2022-techcombank-giu-vung-car-o-muc-cao-15-2-thu-hut-them-1-2-trieu-khach-hang-moi.htm")
    positiveLinks.append("https://vneconomy.vn/techcombank-tri-an-khach-hang-lon-nhat-tu-truoc-den-nay-voi-tong-tri-gia-den-100-ty-dong.htm")
    positiveLinks.append("https://vneconomy.vn/techcombank-tiep-tuc-da-tang-truong-an-tuong-trong-9-thang-dau-nam-2022.htm")
    positiveLinks.append("https://vneconomy.vn/techcombank-vao-top-10-thuong-hieu-xuat-sac-2022.htm")
    positiveLinks.append("https://vneconomy.vn/techcombank-duoc-moodys-nang-hang-tin-nhiem-len-ba2-trien-vong-on-dinh.htm")
    positiveLinks.append("https://vneconomy.vn/techcombank-keo-dai-chuoi-tang-truong-voi-lai-truoc-thue-6-800-ty-dong-trong-quy-1-2022.htm")
    positiveLinks.append("https://vneconomy.vn/lan-dau-ra-mat-bphone-moi-bang-livestream-bkav-chot-duoc-1-233-don-hang.htm")
    positiveLinks.append("https://vneconomy.vn/airb-cua-bkav-co-chen-chan-duoc-vao-thi-truong-tai-nghe-thong-minh.htm")
    positiveLinks.append("https://vneconomy.vn/bkav-muon-la-nha-cung-cap-camera-so-1-o-viet-nam.htm")
    positiveLinks.append("https://vneconomy.vn/bkav-tham-vong-chuyen-huong-sang-dich-vu-aiot-phan-khuc-pho-thong.htm")
    positiveLinks.append("https://vneconomy.vn/evn-co-02-san-pham-dat-giai-thuong-cong-nghe-so-make-in-viet-nam.htm")
    positiveLinks.append("https://vneconomy.vn/evn-nhan-giai-thuong-doanh-nghiep-chuyen-doi-so-xuat-sac-nam-2022.htm")
    positiveLinks.append("https://vneconomy.vn/dai-gia-game-vng-rot-22-5-trieu-usd-vao-funding-societies.htm")
    positiveLinks.append("https://vneconomy.vn/start-up-telio-nhan-22-5-trieu-usd-tu-vng.htm")
    positiveLinks.append("https://vneconomy.vn/vietcombank-xung-danh-don-vi-anh-hung.htm")
    positiveLinks.append("https://vneconomy.vn/vietcombank-60-nam-thap-sang-niem-tin-vuon-ra-bien-lon.htm")
    positiveLinks.append("https://vneconomy.vn/nhieu-uu-dai-lai-suat-cho-khach-hang-vay-von-tai-vietcombank-trong-thang-3-2023.htm")
    positiveLinks.append("https://vneconomy.vn/vietcombank-va-jcb-ra-mat-the-tin-dung-quoc-te-vietcombank-jcb-platinum.htm")
    positiveLinks.append("https://vneconomy.vn/vietcombank-giu-vung-vi-tri-ngan-hang-so-1.htm")

    negativeLinks.append("https://vneconomy.vn/vng-lo-gan-27-ty-ngay-trong-quy-dau-tien-nam-2021.htm")
    negativeLinks.append("https://vneconomy.vn/quy-2-2019-cong-ty-me-vng-lo-rong-102-ty-dong.htm")
    negativeLinks.append("https://vneconomy.vn/kinh-doanh-khong-hieu-qua-vng-dong-cua-game-auto-chess-vng.htm")
    negativeLinks.append("https://vneconomy.vn/dau-tu-vao-start-up-khien-loi-nhuan-cua-vng-giam-rat-manh-20210411063007363.htm")
    negativeLinks.append("https://vneconomy.vn/con-duong-thu-phi-va-nguy-co-sut-giam-nguoi-dung-cua-zalo.htm")
    negativeLinks.append("https://vneconomy.vn/quy-3-2020-vietcombank-bao-lai-giam-hon-21.htm")
    negativeLinks.append("https://vneconomy.vn/vng-tam-lo-hon-300-ty-sau-2-nam-dau-tu-vao-tiki.htm")
    negativeLinks.append("https://vneconomy.vn/giam-doc-dieu-hanh-kinh-doanh-noi-bo-va-kinh-doanh-quoc-te-cua-vnm-xin-tu-nhiem.htm")
    negativeLinks.append("https://vneconomy.vn/yeu-cau-bao-cao-thu-tuong-ve-viec-co-chat-cam-trong-mi-hao-hao-truoc-ngay-7-9.htm")
    negativeLinks.append("https://vneconomy.vn/xuat-hien-hanh-vi-kinh-doanh-buon-ban-goi-sup-acecook-hao-hao-tom-chua-cay-trai-phap-luat.htm")
    negativeLinks.append("https://vneconomy.vn/vu-mi-hao-hao-bi-thu-hoi-o-ireland-acecook-se-dieu-tra-va-co-bien-phap-xu-ly.htm")
    negativeLinks.append("https://vneconomy.vn/cung-cap-21-kenh-truyen-hinh-chua-duoc-cap-chung-nhan-viettel-bi-phat-40-trieu-dong.htm")
    negativeLinks.append("https://vneconomy.vn/co-phieu-cuoi-cung-trong-he-sinh-thai-flc-bi-dinh-chi-giao-dich.htm")
    negativeLinks.append("https://vneconomy.vn/thanh-hoa-cong-ty-con-cua-tap-doan-flc-dung-dau-trong-danh-sach-no-dong-bao-hiem-xa-hoi.htm")
    negativeLinks.append("https://vneconomy.vn/thanh-hoa-tap-doan-flc-tra-lai-14-hubway-tren-bai-bien-tri-gia-165-ty-cho-tp-sam-son-vi-thua-lo.htm")
    negativeLinks.append("https://vneconomy.vn/tong-giam-doc-flc-bui-hai-huyen-cung-hai-nu-tuong-xin-tu-nhiem.htm")
    negativeLinks.append( "https://vneconomy.vn/len-upcom-vao-ngay-3-3-toi-co-phieu-flc-lap-tuc-vao-dien-dinh-chi-giao-dich.htm")
    negativeLinks.append( "https://vneconomy.vn/chua-xac-dinh-duoc-von-dieu-le-hop-le-cua-ros-de-chap-thuan-giao-dich-tren-upcom.htm")
    negativeLinks.append("https://vneconomy.vn/flc-tiep-tuc-bi-cuong-che-hon-76-ty-dong.htm")
    negativeLinks.append("https://vneconomy.vn/tap-doan-flc-bi-cuc-thue-ha-noi-ngung-su-dung-hoa-don-de-cuong-che-no-thue.htm")
    negativeLinks.append( "https://vneconomy.vn/mang-chip-du-bao-lo-lon-samsung-electronics-sap-co-quy-loi-nhuan-thap-nhat-trong-14-nam.htm")
    negativeLinks.append("https://vneconomy.vn/loi-nhuan-cua-samsung-giam-manh-do-nhu-cau-chip-yeu-va-lam-phat-cao.htm")
    negativeLinks.append("https://vneconomy.vn/khoi-tien-mat-100-ty-usd-cua-de-che-samsung-khien-nha-dau-tu-sot-ruot.htm")
    negativeLinks.append("https://vneconomy.vn/pho-tong-giam-do-techcombank-dang-ky-ban-bot-co-phieu.htm")
    negativeLinks.append("https://vneconomy.vn/lo-du-lieu-ca-nhan-hon-200-nguoi-dung-tai-dich-vu-breport-cua-bkav.htm")
    negativeLinks.append("https://vneconomy.vn/hacker-thong-bao-da-ban-mot-phan-du-lieu-cua-bkav-gia-60-000-usd.htm")
    negativeLinks.append("https://vneconomy.vn/kho-khan-song-trung-cua-2-tap-doan-than-dien.htm")
    negativeLinks.append("https://vneconomy.vn/can-benh-ne-tranh-khong-dam-lam-so-trach-nhiem-dang-lan-rong.htm")

    neutralLinks.append("https://vneconomy.vn/vng-tinh-goi-them-300-trieu-usd-truoc-them-ipo-tai-my.htm")
    neutralLinks.append("https://vneconomy.vn/vng-duoc-quy-dau-tu-temasek-dinh-gia-toi-22-ty-usd.htm")
    neutralLinks.append("https://vneconomy.vn/ngay-5-1-2023-vng-len-san-upcom-voi-gia-240-000-dong-co-phieu.htm")
    neutralLinks.append("https://vneconomy.vn/tong-giam-doc-vietcombank-chung-toi-khong-han-che-cap-tin-dung-cho-bat-dong-san-nhung-doanh-nghiep-phai-ha-gia-xuong.htm")
    neutralLinks.append("https://vneconomy.vn/vietcombank-va-bao-hiem-xa-hoi-viet-nam-to-chuc-hoi-nghi-truc-tuyen.htm")
    neutralLinks.append("https://vneconomy.vn/chinh-phu-bo-sung-gan-7-700-ty-dong-von-cho-vietcombank.htm")
    neutralLinks.append("https://vneconomy.vn/em-trai-thanh-vien-hdqt-vinamilk-dang-ky-ban-het-co-phieu.htm")
    neutralLinks.append("https://vneconomy.vn/vinamilk-huy-lien-doanh-thuc-pham-va-do-uong-vibev-voi-kido.htm")
    neutralLinks.append("https://vneconomy.vn/cong-ty-co-phan-acecook-viet-nam.htm")
    neutralLinks.append("https://vneconomy.vn/viettel-idc-hop-tac-cung-firemon-tang-them-lua-chon-ve-giai-phap-bao-mat-cho-khach-hang.htm")
    neutralLinks.append("https://vneconomy.vn/viettel-virtual-soc-giai-phap-tong-the-giam-sat-an-toan-thong-tin-cho-to-chuc-doanh-nghiep.htm")
    neutralLinks.append("https://vneconomy.vn/ong-phung-van-cuong-lam-tong-giam-doc-viettel-global.htm")
    neutralLinks.append("https://vneconomy.vn/tap-doan-flc-bo-nhiem-tong-giam-doc-moi.htm")
    neutralLinks.append("https://vneconomy.vn/flc-len-ke-hoach-chuyen-nhuong-co-phieu-bamboo-airways.htm")
    neutralLinks.append("https://vneconomy.vn/tong-giam-doc-samsung-viet-nam-thong-tin-samsung-chuyen-day-chuyen-smartphone-tu-viet-nam-sang-an-do-la-khong-dung-su-that.htm")
    neutralLinks.append("https://vneconomy.vn/10-gia-toc-giau-nhat-chau-a-nha-samsung-dung-cuoi-bang.htm")
    neutralLinks.append("https://vneconomy.vn/samsung-sds-nhay-vao-thi-truong-logistics-viet-nam.htm")
    neutralLinks.append("https://vneconomy.vn/pho-thu-tuong-le-minh-khai-tiep-tong-giam-doc-tap-doan-samsung-electronics.htm")
    neutralLinks.append("https://vneconomy.vn/samsung-se-san-xuat-dai-tra-cac-san-pham-ban-dan-tai-viet-nam-tu-thang-7-2023.htm")
    neutralLinks.append("https://vneconomy.vn/samsung-tiep-tuc-lai-dam-nho-chip-nho-nha-dau-tu-van-lo-lang.htm")
    neutralLinks.append("https://vneconomy.vn/90-giao-dich-cua-khach-hang-techcombank-duoc-thuc-hien-qua-kenh-so-hoa.htm")
    neutralLinks.append("https://vneconomy.vn/moodys-cap-nhat-xep-hang-cua-techcombank-la-ba3.htm")
    neutralLinks.append("https://vneconomy.vn/techcombank-sap-chao-ban-6-3-trieu-co-phieu-esop-tang-von-dieu-le.htm")
    neutralLinks.append("https://vneconomy.vn/techcombank-phat-hanh-hon-6-trieu-co-phieu-esop-gia-10-000-dong.htm")
    neutralLinks.append("https://vneconomy.vn/cung-techcombank-va-doctor-anywhere-cham-soc-suc-khoe-chuan-singapore.htm")
    neutralLinks.append("https://vneconomy.vn/vinhomes-chuyen-nhuong-co-phan-du-an-lang-van-cho-cong-ty-me-vingroup.htm")
    neutralLinks.append("https://vneconomy.vn/nhu-cau-su-dung-dien-quy-2-tang-cao-evn-len-ke-hoach-cung-ung.htm")
    neutralLinks.append( "https://vneconomy.vn/van-tai-duong-sat-tang-truong-trai-chieu-5-thang-dau-nam-van-tai-khach-bung-no-hang-hoa-lai-giam-sau.htm")
    neutralLinks.append("https://vneconomy.vn/can-thao-go-nhung-vuong-mac-bat-cap-de-hoan-thanh-cac-muc-tieu-tang-truong-gdp.htm")

    #Combine links
    links = positiveLinks+negativeLinks+neutralLinks

    data = {}
    for i in range (0,len(links)):
        data[i+1] = split_word(clean_content(get_article(links[i])))
    with open('article.json','w') as file:
        json.dump(data,file)






