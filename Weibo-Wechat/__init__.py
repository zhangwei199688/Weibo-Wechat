from Cookies import getCookies
from spider import Spider

cookie=getCookies("13832405507","daohaolaji")
textlist=Spider.GetInfo("2656274875",cookie)
for text in textlist:
    print(text)

#A testing.delete later...