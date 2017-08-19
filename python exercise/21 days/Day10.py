#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/19 14:56
# @Author  : Zhangyuanyuan
# @Site    : 
# @File    : Day10.py
# @Software: PyCharm Community Edition

import re
import urllib.request
import http.cookiejar


loginurl = 'https://www.douban.com/accounts/login'
## 将cookies绑定到一个opener  cookie由cookielib自动管理
cookie = http.cookiejar.CookieJar()
##安装opener,此后调用urlopen()时都会使用安装过的opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)

params={}
params['form_email']='***'
params['form_password']='***'
params['source']='https://www.douban.com/accounts/login'

response = opener.open(loginurl,urllib.parse.urlencode(params).encode('utf-8'))
if response.geturl()[0:33]=='https://accounts.douban.com/login':
    html = response.read().decode('utf-8')
    print(html)
    #获取验证码图片
    imgurl = re.search('img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image".*?/',html)
    if imgurl:
        url = imgurl.group(1)
        #将验证码图片保存到本地
        res = urllib.request.urlretrieve(url,'v.jpg')
        cap = re.search('<input type="hidden" name="captcha-id" value="(.*?)"/>',html)
        if cap:
            vcode = input('请输入图片上的验证码：')
            params['captcha-solution'] = vcode
            params['captcha-id'] = cap.group(1)
            params['user_login'] = "登录"
            #提交
            response = opener.open(loginurl,urllib.parse.urlencode(params).encode('utf-8'))
            if response.geturl() == "https://www.douban.com/":
                print("login usccess")
























