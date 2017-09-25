import requests
import time
from headers import agents
from random import choice
from lxml import etree

def get_path(html):
    return etree.HTML(html)

class Spider(object):
    def GetInfo(userid,cookies):
        PageNum = 1
        while True:
            Start_url="https://weibo.cn/u/"+userid+"?page="+str(PageNum)
            header={"User-Agent":choice(agents)}
            session=requests.session()
            try:
                html=session.get(url=Start_url,cookies=cookies,headers=header).content
            except Exception as e:
                print("请求失败或页面已经到头")
                exit()
            tree=get_path(html)
            Tweets=tree.xpath("//div[@class=\"c\"and @id]")
            if not(("今天" in Tweets[0].xpath(".//span[@class=\"ct\"]/text()")[0]) or ("前" in Tweets[0].xpath(".//span[@class=\"ct\"]/text()")[0])):
                Tweets.pop(0)
            for tweet in Tweets:
                time=tweet.xpath(".//span[@class=\"ct\"]/text()")[0].split(" ")[0]
                if ("今天" in time) or ("前" in time):

                    text=tweet.xpath(".//span[@class=\"ctt\"]")[0].xpath("string(.)")
                    text=text+"\n"+time
                    yield text
                else:
                    return

            PageNum+=1






