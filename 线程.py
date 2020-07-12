#参考url：https://www.cnblogs.com/leozhanggg/p/10335098.html
'''
线程表示在单独的控制线程中运行的活动，有两种方法可以指定该活动：
1、将调用对象传递给构造函数；
2、通过覆盖之类中的run()方法；
'''

#1、无线程
#　如果你对线程不太理解，我们可以打个比方，把线程数看作车辆数，
# 我们来完成一个简单的客运运输工作（以下为了方便理解，也加入相应注释）
# import time
# start=time.time()
# people=500 #假设有500人
# def action(num):
#     global people
#     while people>0:
#         people-=50 #每次运输50人
#         print('车辆编号：%d,当前车站人数：%d' %(num,people))
#         time.sleep(2)
# num=1 #车辆编号
# action(num)
# end=time.time()
# print('1、无线程所用时间：%0.3f' %(end-start))

#2、单线程
# import threading
# import time
# start=time.time()
# people=500
# def action(num):
#     global people
#     while people>0:
#         people-=50
#         print('车辆编号：%d，当前车站人数：%d' %(num,people))
#         time.sleep(1)
#
# num=1
# vehicle=threading.Thread(target=action,args=(num,))  #新建车辆
# vehicle.start() #启动车辆
# vehicle.join() #检查到站车辆
# end=time.time()
# print('2、单线程所用时间：%0.3f' %(end-start))

#3、多线程（传递对象方式）
#coding=utf-8
import threading
import time
people=500
class MyThread(threading.Thread):
    def __init__(self,num):
        super(MyThread,self).__init__()
        self.num=num
    def run(self):
        global people
        while people>0:
            people-=50
            print('车辆编号：%d，当前车站人数：%d' %(self.num,people))
            time.sleep(1)
start=time.time()
vehicles=[] #新建车辆组
for num in range(5):   #设置车辆数
    vehicle=MyThread(num)  #新建车辆
    vehicles.append(vehicle)  #添加车辆到车辆组中
    vehicle.start() #启动车辆
for vehicle in vehicles:
    vehicle.join()  #分别检查到站车辆
end=time.time()
print('3、多线程传递对象所用时间：%0.3f' %(end-start))

#4、多线程（覆盖之类模式）
#coding=utf-8
import threading
import time
people=500
class MyThread(threading.Thread):
    def __init__(self,num):
        super(MyThread,self).__init__()
        self.num=num
    def run(self):
        global people
        while people>0:
            people-=50
            print('车辆编号：%d，当前车站人数：%d' %(self.num,people))
            time.sleep(1)
start=time.time()
vehicles=[] #新建车辆组
for num in range(5):   #设置车辆数
    vehicle=MyThread(num)  #新建车辆
    vehicles.append(vehicle)  #添加车辆到车辆组中
    vehicle.start() #启动车辆
for vehicle in vehicles:
    vehicle.join()  #分别检查到站车辆
end=time.time()
print('4、多线程覆盖所用时间：%0.3f' %(end-start))



#多线程：https://www.cnblogs.com/leozhanggg/p/10317494.html






