#参考url：https://www.cnblogs.com/beer/p/4973116.html
#coding=utf-8
#获取博客的排名并自动邮件通知

from bs4 import BeautifulSoup
from time import sleep
import requests
import logging
import threading
import smtplib
from email.header import Header
from email.mime import multipart
from email.message import Message
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

__author__='zhangbinghui'

def get_nums(blogs_des):
    #得到具体的积分和排名的值；
    split_str=blogs_des.split('-')[1].strip()
    return split_str
def get_blog_ranks():
    #解析页面获取博客积分和排名
    url = 'https://www.cnblogs.com/laozhangceshi/ajax/sidecolumn.aspx?blogApp=laozhangceshi'
    res=requests.get(url)
    soup=BeautifulSoup(res.text)
    lis=soup.findAll('div')
    for item in lis:
        if 'siderbar_scorerank' ==item.get('id'):
            li_lists=item.findAll('li')
            for li_item in li_lists:
                if u'积分' in li_item.text:
                    score=get_nums(li_item.text)
                elif u'排名' in li_lists:
                    rank=get_nums(li_item.text)
                else:
                    print('Error')

get_blog_ranks()













