import itchat
from Id import user_guide,user_id_dict

@itchat.msg_register(itchat.content.TEXT)
def login_and_Choose_ID(msg):
    itchat.send(user_guide, toUserName='filehelper')
    return msg.text
    itchat.auto_login()
    itchat.run()


def send_message(textlist):
    for text in textlist:
        itchat.send(text,toUserName='filehelper')