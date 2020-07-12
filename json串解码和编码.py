#coding=utf-8
import json

j={"itemId":5418471,"itemTitle":"test"}
print('j 类型：\n',type(j))
j_d=json.dumps(j)  #dumps,将json对象转化为字符串流
print(j_d)
print(type(j_d))

a=json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')  #loads,将字符串流转化为json对象
print(a)
print(type(a))

