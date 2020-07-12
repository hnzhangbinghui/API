'''
beautifulsoup4是爬虫必学的技能，
1、主要功能是从网页抓取数据；
2、自动将输入或输出文档转为Unicode编码，
3、支持python标准库的html解析器，还支持一些第三方的解析器；
4、默认使用的是python的解析器，lxml解析器更加强大，速度更快；
5、bs4和lxml一样，bs4也是一个html，xml的解析器，主要功能是如何和提取html xml数据；
'''

#得到一个html网页的所有标签内容
import re
from bs4 import BeautifulSoup
file=open(r'C:/Users/LX/Desktop/a.html','rb')
html=file.read()
bs=BeautifulSoup(html,'html.parser') #设置缩进格式，显示代码
'''******************第一部分******************'''
# # print(bs)
# # print('格式化html结构\n',bs.prettify())
# print('得到title标签的名称：\n',bs.title) #得到title标签的名称
# print('得到title的name:\n',bs.title.text)  #得到title标签的文本内容
# print('得到head标签：',bs.head,'\n','得到link标签的url的值：\n',bs.link['href'],'\n',bs.link['type'])
# print('得到div的值:\n',bs.div,'得到div的id的值\n',bs.div['id'])
# print('得到a的值：',bs.a)  #这样只是的到的第一个标签为a的值；
# print('得到所有a标签的值01：',bs.findAll('a'))
# a_all=bs.findAll('a')
# print('通过findall得到所有a标签的值，类型是 ：',type(a_all))
# for i in range(len(a_all)):
#     print('得到所有a标签的href的值：',a_all[i].text,':',a_all[i]['href'])
# print('得到所有a标签的值02：',bs.find(id='u1'))
# for item in bs.findAll('a'):
#     print(item.text,':',item.get('href'),item.get_text())
# print('*****************根据标签的到具体的所有的a标签的值****************')
# a_all02=bs.find(id='u1')
# print(type(a_all02))
# print(a_all02.find_all_next())
# for i in range(len(a_all02.find_all_next())):
#     print('根据对应的得到具体的值：\n',a_all02.find_all_next()[i]['href'],':',a_all02.find_all_next()[i].text)
'''******************第二部分******************'''
# #beautifulsoup4 将复杂的html文档转换成一个复杂的属性结构，每个节点都是python对象
# #将对象分为四类：Tag，NAVIGablestring，beautifulsoup，comment；
# #1、tag，标签,
# print('得到title标签所有的内容：\n',bs.title)
# print('得到header标签所有的内容：\n',bs.head)
# print('得到a标签所有的内容：\n',bs.a)
# print('a标签的类型：',type(bs.a))
# print('得到标签的属性值：：：\n',bs.a.text,bs.a['href'],bs.a['name'],bs.a.get('class'),bs.a.get('href'))
# #可以通过soup加标签名轻松地获取这些标签的内容，这些对象的类型是bs4.element.Tag，注意，他查找的是在所有内容中的第一个符合要求的标签
# print(bs.name) # [document] #bs 对象本身比较特殊，它的 name 即为 [document]
# print(bs.head.name)  # head #对于其他内部标签，输出的值便为标签本身的名称
# print('通过attrs得到的是一个字典：\n',bs.a.attrs)  # 在这里，我们把 a 标签的所有属性打印输出了出来，得到的类型是一个字典。
# print(bs.a.attrs['href'])
# print(bs.a['href'],bs.a.get('href'))  ##还可以利用get方法，传入属性的名称，二者是等价的
# bs.a['name']='新闻'
# print(bs.a['name'])   # 可以对这些属性和内容等等进行修改
# # 还可以对这个属性进行删除 del bs.a['class']
#
# #2、得到标签内部的文字，用  .string即可
# print(bs.title.string)
# print(bs.a.string,bs.a['name'],bs.a.text)
#
# #3、beautifulsoup对象表示的是一个文档的内容，大部分时候，可以把它当做tag对象，是一个特殊的tag，
# # 可以分别获取他的类型，名称，以及属性；
# print(bs.a.attrs)
# print(type(bs.name))
# #4、comment对象是一个特殊类型的 navigablestring 对象，其输出的内容不包括注释符号
# print(bs.a)
# print(bs.a.string)
# print(type(bs.a.string))

'''******************第三部分******************'''
# #遍历文档树
# #1、comments 获取 tag的所有子节点，返回一个list
# #tag 的.contents 属性可以将tag的   子节点  以列表   的方式输出
# print('得到所有div标签的所有子节点：\n',bs.div.contents)
# print('得到div所有子节点的长度：\n',len(bs.div.contents))
# print('通过列表索引获取他的某一个元素：\n',bs.div.contents[1])
#
# #2、  .children  获取tag的所有子节点，返回一个生成器
# for child in bs.div.children:
#     print('得到body标签的子节点：',child)
#     for ch in child:
#         print('子节点的子节点',ch)
#
# print('得到tag所有的子孙节点：\n',bs.body.descendants)
# '''5.3、.descendants：获取Tag的所有子孙节点
#
# 5.4、.strings：如果Tag包含多个字符串，即在子孙节点中有内容，可以用此获取，而后进行遍历
#
# 5.5、.stripped_strings：与strings用法一致，只不过可以去除掉那些多余的空白内容
#
# 5.6、.parent：获取Tag的父节点
#
# 5.7、.parents：递归得到父辈元素的所有节点，返回一个生成器
#
# 5.8、.previous_sibling：获取当前Tag的上一个节点，属性通常是字符串或空白，真实结果是当前标签与上一个标签之间的顿号和换行符
#
# 5.9、.next_sibling：获取当前Tag的下一个节点，属性通常是字符串或空白，真是结果是当前标签与下一个标签之间的顿号与换行符
#
# 5.10、.previous_siblings：获取当前Tag的上面所有的兄弟节点，返回一个生成器
#
# 5.11、.next_siblings：获取当前Tag的下面所有的兄弟节点，返回一个生成器
#
# 5.12、.previous_element：获取解析过程中上一个被解析的对象(字符串或tag)，可能与previous_sibling相同，但通常是不一样的
#
# 5.13、.next_element：获取解析过程中下一个被解析的对象(字符串或tag)，可能与next_sibling相同，但通常是不一样的
#
# 5.14、.previous_elements：返回一个生成器，可以向前访问文档的解析内容
#
# 5.15、.next_elements：返回一个生成器，可以向后访问文档的解析内容
#
# 5.16、.has_attr：判断Tag是否包含属性'''
#
# print('得到父节点：\n',bs.a.parent)

'''******************第四部分******************'''
#搜索文档树
#find_all,过滤器，这些过滤器贯穿整个搜索API，过滤器可以别用在tag的name中，节点的属性等；

#1、name参数，字符串过滤，会查找与字符串完全匹配的内容
a_list=bs.find_all('a')
print(a_list,'\n')
for al in a_list:
    print(al['href'])
#正则表达式过滤，如果传入的是正则表达式，那么beautifulsoup4会通过search（）来匹配内容
print('********正则表达式*********')
t_list=bs.find_all(re.compile('title'))    #标签值
for item in t_list:
    print(item)
print('********传入列表进行测试*********')
#传入列表，beautifulsoup4将会与列表中的任一元素匹配到节点返回
t_list2=bs.find_all(['a','link'])
for item in t_list2:
    print(item)
print('********传入方法进行测试*********')
#可以传入一个方法，来进行匹配
def name_is_exists(tag):
    return tag.has_attr("name")
t_list = bs.find_all(name_is_exists)
for item in t_list:
    print(item)
print('********传入kwargs进行测试*********')
t_list3=bs.find_all(id='head')   # 查询id=head的Tag
print(t_list3)

# 查询href属性包含ss1.bdstatic.com的Tag
t_list4=bs.find_all(href=re.compile('http://news.baidu.com'))
print(t_list4)

# 查询所有包含class的Tag(注意：class在Python中属于关键字，所以加_以示区别)
t_list5=bs.find_all(class_='mnav')
print('搜索class为mnav的标签：\n',t_list5)
print(type(t_list5))

# #attrs 参数，并不是所有的属性都可以使用上面这种方式进行搜索，比如HTML的data-*属性：
# t_list6=bs.find_all(attrs={'data-foo':'value'})
# for item in t_list6:
#     print(item)
#4、（重点）通过text参数，搜索文档中字符串内容，与name参数的可选值一样，text参数接受字符串，正则表达式，列表等；
print('***********通过text进行搜索*************')
tt=bs.find_all(text='新闻 ')
for item in tt:
    print(item)
tt=bs.find_all(text=['新闻 ','hao123 ','贴吧 '])
for item in tt:
    print(item)
tt=bs.find_all(text=re.compile(' '))    #正则表达式
for item in tt:
    print(item)

#当我们搜索text的一些特殊属性是，同样可以传入一个方法来达到我们的目的
def length_is_two(text):
    return text and len(text) == 3
t_list = bs.find_all(text=length_is_two)
for item in t_list:
    print('通过方法：',item)

#5、非常重要，通过limit参数，来限制返回的数量；

t_list = bs.find_all("a",limit=2)
for item in t_list:
    print('只返回前两条：\n',item)

'''find_all除了上面一些常规的写法，还可以对其进行一些简写：
# 两者是相等的
# t_list = bs.find_all("a") => t_list = bs("a")
t_list = bs("a") # 两者是相等的
# t_list = bs.a.find_all(text="新闻") => t_list = bs.a(text="新闻")
t_list = bs.a(text="新闻")'''
print('*********find**************')
#find(),将返回符合条件的第一个tag，也可以用find_all（）方法，传入limit=1即可；
print(bs.find('a'))
print(bs.find_all('a',limit=1))
#从结果可以看出find_all，尽管传入了limit=1，但是返回值仍然为一个列表，当我们只需要取一个值时，远不如find方法方便
#T通过find，如果没有找到None
print('找不到的标签，返回None：',bs.find('zhang'))

#通过bs.div来获得第一个div标签，如果我们需要获取第一个div下的第一个div；
print(bs.div.div.div.div)
# bs.div.div等价于bs.find('div').find('div')

'''******************第五部分******************'''

#Tag 获取beautifulsoup 对象的 .select() 方法中传入字符串参数，既可以使用css选择器的语法；
print('通过标签名来查找：',bs.select('title'))  #返回的是列表
print(bs.select('a'))
print('通过类名查找：',bs.select('.mnav'),'\n',len(bs.select('.mnav')))  #通过类名来查找，前面要有个点
print('通过id来查找：\n',bs.select('#u1'))

#组合查找
print('组合查找：\n',bs.select('div .bri'))
print('组合查找2：\n',bs.select('div #u1'))

#属性查找
print('通过属性查找：\n',bs.select('a[class="mnav"]'))   #得到的是列表
#直接子标签查找
print(bs.select("div > a"))
#兄弟节点标签查找
print(bs.select(".mnav ~ .bri"))
#获取内容
for item in bs.select('a'):
    print(item.text,item.get('href'))


#参考url：http://www.jsphp.net/python/show-24-214-1.html







