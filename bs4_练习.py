#coding=utf-8
from bs4 import BeautifulSoup
import requests
headers = {'content-type': 'application/x-www-form-urlencoded','Accept-Encoding':'gzip, deflate, br','Accept-Language': 'zh-CN,zh;q=0.9'}
#关于乱码问题
#https://blog.csdn.net/guoxinian/article/details/83047746

file=requests.get('https://www.dytt8.net/').content.decode('gbk','ignore').encode('utf-8')
# print(file)
bs=BeautifulSoup(file,'html.parser') #设置缩进格式，显示代码
# print(bs)
# print(bs.title)
# a_div=bs.findAll('a')
# # print(a_div)
# dict={}
# i=1
# for i in range(len(a_div)):
#     dict[a_div[i].text]=a_div[i]['href']
#     # print(a_div[i].text,':',a_div[i]['href'])
# print(dict)
# print(list(dict.items()))
#导出列表到excel表
result=open('dainying.xlsx','w',encoding='gbk')
result.write('X\tY\n')
print('************爬虫具体的值******************')
print(bs)
#得到所有电影名字以及对应的url
dict_movie={}
for item in bs.select('a'):
    # print(item.text,':',item['href'])
    dict_movie[item.text]=item['href']
del dict_movie['']
# print(dict_movie)
import pandas as pd
df=pd.DataFrame(list(dict_movie.items()))
df.columns=['电影名','网址']
# print(df)
df.to_excel('movie.xlsx')

#循环遍历
m=bs.select('#menu a',limit=4)
print(m)
for i in range(len(m)):
    print(m[i].text,m[i]['href'])
    r=requests.get(m[i]['href']).content.decode('gbk', 'ignore').encode('utf-8')
    bs=BeautifulSoup(r,'html.parser')
    print(bs.select('a'))
