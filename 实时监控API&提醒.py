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

class BlogRankMonitor(object):
    #博客园积分排名监控工具
    def __init__(self,id):
        self.gap_seconds=60*30 #间隔时间为30分钟
        self.url_fmt='https://www.cnblogs.com/%s/ajax/sidecolumn.aspx?blogApp=%s'
        self.id=id
        self.score=0
        self.rank=0
        self.his_score=0
        self.his_rank=0
    def get_blog_ranks(self):
        #解析页面获取博客积分和排名
        url=self.url_fmt % (self.id,self.id)
        res=requests.get(url)
        soup=BeautifulSoup(res.text)
        lis=soup.findAll('div')
        for item in lis:
            if 'siderbar_scorerank' ==item.get('id'):
                li_lists=item.findAll('li')
                for li_item in li_lists:
                    if u'积分' in li_item.text:
                        self.score=get_nums(li_item.text)
                    elif u'排名' in li_lists:
                        self.rank=get_nums(li_item.text)
                    else:
                        print('Error')
            continue

    def monitor_score_rank(self):
        #监控博客积分和排名的变化
        while True:
            self.get_blog_ranks()
            print(self.score,self.rank)
            if self.score != self.his_score or self.rank != self.his_rank:
                mail_title='[e-notice]:blog-rank-changes'
                mail_body='[%s]time-(score,rank):old-(%s,%s),now-(%s,%s)' \
                          %(self.id,self.his_score,self.rank,self.score,self.rank)
                print('得到监控的分数和排名：',mail_body)
    def start_score_rank_thread(self):
        #开启监控的线程
        thread.start_new_thread(self.monitor_score_rank(),())

if __name__=='__main__':
    BlogRankMonitor('laozhangceshi')



#让主线程一直运行，利用while循环
while 1:
    sleep(3600)



















