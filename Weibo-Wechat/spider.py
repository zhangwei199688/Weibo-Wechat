import requests
import time
from headers import agents
from random import choice
from lxml import etree

class Spider(object):
    def __init__(self,userid,cookies):
        self.userid = userid
        self.cookies = cookies
        self.GetInfo(self.userid,self.cookies)

    def get_path(self,html):
        return etree.HTML(html)

    def GetInfo(self,userid,cookies):
        while True:
            PageNum=1
            Start_url="https://weibo.cn/u/"+userid+"?page="+str(PageNum)
            header={"User-Agent":choice(agents)}
            session=requests.session()
            try:
                html=session.get(url=Start_url,cookies=cookies,headers=header).content
            except Exception as e:
                print("请求失败或页面已经到头")
                exit()
            tree=self.get_path(html)
            Tweets=tree.xpath("//span[@class=\"ctt\"]")
            for tweet in Tweets:
                if  "今天" in tweet.xpath("..//span[@class=\"ct\"]/text()"):
                    text=tweet.xpath("string(.)")
                    print(text)
                    print("\n\n")
                else:
                    exit()
            PageNum+=1






