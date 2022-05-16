import requests
from bs4 import BeautifulSoup

url="https://gadgets360.com/mobiles"

cont = requests.get(url)
htmlContent = cont.content

soup = BeautifulSoup(htmlContent, "html.parser")
print(soup.prettify)


title = soup.title
print(title)


import mysql.connector
import pymysql

con = pymysql.connect(user='root',password='',host='localhost',database="scrapping")
cur = con.cursor()

#cur.execute("CREATE TABLE mobileset4(URLS VARCHAR(10000))")
# caption = soup.find_all("div", class_="caption")
# print(caption)
#all_links = set()

anchor = soup.find_all("a")

for links in anchor:
  x = links.get('href')
  #print(links.get('href'))
  qry = ("INSERT INTO `mobileset4`(`URLS`) VALUES (%s)")
  cur.execute(qry, x)

con.commit()
con.close()

print("Insertion successfull!!")
print(cur.rowcount, "record inserted.")