#encoding:utf-8
import requests
url="http://10.119.169.23:8092/program/pepprogramBasicInfo/getElementInfoUuid"
headers={
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
}
#发送get请求
response=requests.get(url,headers=headers)
print(response.text)
print(response.status_code)