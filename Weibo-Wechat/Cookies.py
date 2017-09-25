from selenium import webdriver
import time
import json

def  getCookies(userid,pwd):
    try:
        #driver=webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        #driver.set_window_size(800, 600)
        driver=webdriver.Firefox(executable_path = 'D:\Python\geckodriver')
        driver.get("https://passport.weibo.cn/signin/login")
        time.sleep(1)
    except Exception as e:
        print("webdriver启动失败，请重试")
        exit()

    try:
        user=driver.find_element_by_xpath("//*[@id=\"loginName\"]")
        user.clear()
        user.send_keys(userid)

        password=driver.find_element_by_xpath("//*[@id=\"loginPassword\"]")
        password.clear()
        password.send_keys(pwd)
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id=\"loginAction\"]").click()
        time.sleep(10)
    except Exception as e:
        print("登陆过程出现问题，请重试")
        print(e)
        exit()

    if "微博 - 随时随地发现新鲜事" in driver.title:
        print("微博登陆成功...开始获取cookies")
        time.sleep(3)
    else:
        print("登陆失败，可能是密码输入错误或其他原因，请重试")
        exit()

    try:
        cookies={}
        for ele in driver.get_cookies():
            cookies[ele["name"]]=ele["value"]
        print("获取cookie成功")
        driver.close()
        return cookies
    except Exception as e:
        print("获取cookie失败")
        exit()




