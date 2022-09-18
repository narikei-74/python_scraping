from urllib.parse import urlparse
import requests
import urllib.robotparser
from bs4 import BeautifulSoup

# スクレイピングOKかチェックする 
def check_allow(url):
  # ドメインを取得
  parse = urlparse(url)
  domain = parse.netloc

  # robots.txtを取得
  robots_txt_url = "https://" + domain + "/robots.txt"
  rp = urllib.robotparser.RobotFileParser()
  rp.set_url(robots_txt_url)
  rp.read()

  # スクレイピング許可チェック
  return rp.can_fetch('*', url)


# ページを取得し書き出す
def get_html_page(url):
  # ページの取得
  html = requests.get(url)
  soup = BeautifulSoup(html.content, "html.parser")
  
  print(soup.find("title").text)
