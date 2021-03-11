headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
from bs4 import BeautifulSoup as BS
import requests
url = 'https://www.google.ee/search?sxsrf=ALeKk00gLzcmg9QZyJ67Q-DHgOVmwaionA%3A1615462243748&source=hp&ei=Y_9JYMuBK4e1U6iyhYAB&iflsig=AINFCbYAAAAAYEoNc4WOy_-CYMwDZhLwnAa5dhqUmErV&q=random+facts&oq=random+facts&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBOgYIIxAnEBM6BAgjECc6CAguELEDEIMBOggIABCxAxCDAToLCAAQsQMQxwEQowI6AggAOgUIABCxAzoICAAQxwEQrwE6BwgAEIcCEBQ6CAgAEMcBEKMCOgIILjoECAAQClCPBFjXFmD8GWgAcAB4AIABZogBsgeSAQQxMS4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=gws-wiz&ved=0ahUKEwiLv7zpkajvAhWH2hQKHShZARAQ4dUDCAc&uact=5'
full_page = requests.get(url, timeout=3, headers=headers)
# print(full_page.text)
soup = BS(full_page.content, 'html.parser')
text_value = soup.findAll(class_="sW6dbe")
result=text_value[0].text
print(result)
text_value2=soup.findAll(class_="DRBylb")
result1=text_value2[0].text
print(result1)
