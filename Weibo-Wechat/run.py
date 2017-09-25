from Cookies import getCookies
from spider import Spider
import itchat
from Id import user_guide,user_id_dict
from wechat import login_and_Choose_ID,send_message

global cookie
cookie=getCookies("13832405507","daohaolaji")

itchat.auto_login(hotReload=True)
itchat.send(user_guide, toUserName='filehelper')
@itchat.msg_register(itchat.content.TEXT)
def login_and_Choose_ID(msg):
        id=msg.text
        text_list=Spider.GetInfo(user_id_dict[id],cookie)
        text_list=list(text_list)
        if not text_list:
            itchat.send("还没有新微博",toUserName='filehelper')

        else:
             for text in text_list:
                itchat.send(text, toUserName='filehelper')
        itchat.send(user_guide, toUserName='filehelper')


if __name__ == '__main__':
    itchat.run()
