from functions import check_allow, get_html_page

# 検証したいURL
url = input("検証したいurlを入力")

# スクレイピング可能かチェック
if check_allow(url) == True:
  get_html_page(url)
else:
  print("スクレイピングできないページです。")  

