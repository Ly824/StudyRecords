import requests
from bs4 import BeautifulSoup

# 目标网站
url = 'https://quotes.toscrape.com'

# 获取网页内容
response = requests.get(url)
response.encoding = 'utf-8'  # 设置正确的编码

if response.status_code == 200:
    print("网页获取成功!")
else:
    print(f"网页获取失败，状态码: {response.status_code}")

# 使用 BeautifulSoup 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的名言
quotes = soup.find_all('div', class_='quote')

# 提取并打印每个名言和对应的作者
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    # 强制以UTF-8编码输出
    print(f'“{text}” —— {author}'.encode('utf-8').decode('utf-8'))
