#encoding:utf-8
import requests
url="http://10.119.169.23:8092/program/pepprogramBasicInfo/initBasicInfo/?"
headers={
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
}
#url参数
payload={"programId":"1"}
#发送get请求
response=requests.post(url,headers=headers,params=payload)
#查看相应内容，response.txt是unicode格式的数据
print(response.text)
print(response.status_code)




