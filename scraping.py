import requests
from bs4 import BeautifulSoup
import time
from openpyxl import Workbook

#私のwebサイト
url = "https://hitsujienglish.com/"

# HTTPリクエストを送信してHTMLを取得する
response = requests.get(url)

# BeautifulSoupを使用してHTMLを解析する
soup = BeautifulSoup(response.content, 'html.parser')

# 記事タイトルを含むタグを見つける
title_tags = soup.find_all('h3', class_='post-card-title')

# Excelファイルを開く
workbook = Workbook()
sheet = workbook.active

# 記事タイトルをExcelに入力する
for i, title in enumerate(title_tags):
    sheet.cell(row=i+1, column=1, value=title.text.strip())
    
    # 2秒間のウェイト
    time.sleep(2)

# Excelファイルを保存する
workbook.save("articles.xlsx")
