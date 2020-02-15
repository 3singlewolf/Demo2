# _*_ coding=utf-8 _*_
#开发者：3singlewolf
#开发时间：2020-02-13
#开发工具：pycharm

import re  #导入正则表达式模块
import os   #导入操作系统模块
filename="shequ.txt"

def menu():
# 显示功能菜单
    print('''
    ╔—————————————————社区出入登记管理系统—————————————————╗
    ┃     ================功能菜单================      
    ┃                                                 
    ┃  选项                                           
    ┃   1    录入出入居民信息                              
    ┃   2    查找出入居民信息                               
    ┃   3    删除出入居民信息                              
    ┃   4    修改出入居民信息                              
    ┃   5    出入日期、体温排序                                               
    ┃   6    统计出入居民人数                              
    ┃   7    显示所有出入居民信息                         
    ┃   0    退出系统                                 
    ┃                                               
    ┃   ========================================     
    ┃   说明：通过数字或↑↓方向键选择菜单                
    ╚———————————————————————————————————————————————╝    
    ''')

#主函数
def main():
    ctrl=True
    while(ctrl):
        menu()  #显示
        option= input("请选择：")  #选择菜单项
        option_str= re.sub("[^0-9]","",option)
        #正则表达式匹配，功能：删除非数字内容，提取数字
        if option_str in ['0','1','2','3','4','5','6',"7"]:
            option_int = int(option_str)
            if option_int == 0:
                print("您已退出社区出入登记管理系统")
                ctrl=False
            elif option_int == 1:  #录入
                insert()
            elif option_int == 2:  #查找
                search()
            elif option_int == 3:  #删除
                delete()
            elif option_int == 4:  #修改
                modify()
            elif option_int == 5:  #排序
                sort()
            elif option_int == 6:  #统计人员总数
                total()
            elif option_int == 7:  #显示所有人员信息
                show()



'''1 录入信息'''

# 录入信息
def insert():
   residentList = []  #保存社区信息的列表
   mark = True  #是否继续添加
   while mark :
       id = input("请输入居民ID 如（1001）：")
       if not id : #id 为空，跳出循环
         break
       name = input("请输入居民名字：")
       if not name:
           break
       try:

           temperature= float(input("测量体温为(36.5):"))
           date = input("请输入出入日期(2020-02-14)：")
           phone = int (input("请输入通讯号码："))
           adress =input("请输入通讯地址:")


       except:
           print("输入无效，不是整数数值........请您重新录入信息")
           continue
       #将输入的信息保存到字典
       resident = {"id":id,"name":name,"temperature":temperature,"date":date ,"phone": phone,
                   "adress":adress}
       residentList.append(resident)#将字典添加到列表中
       inputMark=input("是否继续添加？（y/n）:")
       if inputMark=="y": #继续添加
           mark =True
       else: #不继续添加
           mark =False
   save(residentList)
   print("信息录入完毕！！！")


#保存信息

def save(resident):
    try:
        resident_txt=open(filename,"a")
    except Exception as e:#万能异常Exception，只要有异常就触发
        resident_txt=open(filename,"w") #文件不存在，创建文件并打开
    for info in resident:       #   列表转化为字符串，按行存储，添加换行符
        resident_txt.write(str(info)+"\n") # write（）将一个字符串或字符流写入,“{：}\n{：}”
    resident_txt.close()#关闭文件



''' 2 查找学生成绩信息  '''

# 查找信息
def search():
    mark = True
    resident_query = [] #保存查询结果列表
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename): #判断文件是否存在
            mode =input("按ID查询输入1；按姓名查询输入2：")
            if mode  == "1":
               id =input("请输入居民ID：")
            elif mode =="2":
                name =input("请输入居民姓名：")
            else:
                print("您输入有误，请重新输入！")
                search() #重新查询
            with open(filename,"r") as file: #打开文件
                resident = file.readlines() # 读取全部内容  然后依次筛选
                for list in resident :  #resident为列表[“{：}\n”]，列表里的每一行list 为字符串“{：}\n”
                    d = dict(eval(list)) #字符串转字典  #本身eval(list)后就是dict类型，加上dict没啥妨碍
                    if id != "":#判断是否按ID查
                       if d["id"] == id:
                           resident_query.append(d)#将找到的信息保存到列表中
                    elif name != "":  # 判断是否按姓名查
                        if d["name"]==name:
                            resident_query.append(d)#将找到的信息保存到列表中
                show_resident(resident_query)# 显示查询结果
                resident_query.clear() #清空列表
                inputMark = input(" 是否继续查询？（y/n）:")
                if inputMark == "y":
                    mark = True
                else:
                    mark =False
        else:
            print("数据为空，暂未保存信息......")
            return  # 结束执行退出函数


''' 3 删除人员信息 '''

def delete():
   mark =True
   while mark: #循环标记
       residentId=input("请输入要删除的居民ID：")
       if residentId !="":
           if  os.path.exists(filename):
               with open(filename,"r") as rfile:
                   resident_old = rfile.readlines()
           else:
               resident_old =[]
           ifdel =False   # 标记是否删除
           if resident_old: # 如果存在信息
               with open(filename,"w") as wfile:  # 以写方式打开文件
                   d={} # 定义空字典
                   for list in resident_old:  #遍历文件的每一行  这样做的好处是减少占用内容，加快执行速度
                       d=dict(eval(list))  # 字符串转字典
                       if d["id"] != residentId:
                           wfile.write(str(d)+"\n")#如果不是删除的id就写入
                       else:                       #如是删除的id就不写入
                           ifdel =True  # 标记已经删除
                   if ifdel:
                       print("ID为%s 的居民信息已经被删除..."% residentId)
                   else:
                       print("没有找到ID为%s的居民信息..."%residentId)

           else:
               print("无居民信息...")
               break #跳出当前循环
           show()  # 显示全部信息
           inputMark = input("是否继续删除？（y/n）:")
           if inputMark == "y":
               mark = True
           else:
               mark = False   # 退出删除信息功能

''' 4 修改信息 '''

def modify():
   show()
   if os.path.exists(filename):
       with open(filename,"r") as rfile:
           resident_old = rfile.readlines()  #返回列表类型
   else:
       return  #遇到return函数就结束了
   residentname = input("请输入要修改的居民姓名：")
   with open(filename,"w") as wfile:
       for resident in resident_old:
               d =dict(eval(resident))
               if d["name"] == residentname:
                   print("找到了这位居民，可以修改他的信息！")
                   while True:
                       try:
                         d["name"]=input("请输入姓名：")
                         d["temperature"]=float(input("请输入测量体温："))
                         d["date"]=input("请输入出入日期：")
                         d["phone"]=int(input("请输入通讯号码："))
                         d["adress"] = input("请输入通讯地址：")

                       except:
                           print("您的输入有误，请重新输入：")
                       else:   #没有异常的话，接着try语句处理
                           break  # 跳出循环

                   resident = str(d)  # 将字典转换为字符串
                   wfile.write(resident+"\n")  # 将修改的字符串信息写入到文件
                   print("修改成功！")
               else:
                  wfile.write(resident)
   mark = input("是否继续修改其他居民信息？（y/n）：")
   if mark =="y":
       modify()  # 重新执行修改操作
   else:
       return  # 函数停止执行




''' 5 排列信息'''
def sort():
   show()
   if os.path.exists(filename):   # 判断文件是否存在
       with open(filename,"r") as file:  # 打开文件
           resident_old = file.readlines()  # 读取全部内容 返回值是列表类型["{:}\n,{:}\n..."]
           resident_new =[]
       for list in resident_old:
            d= dict(eval(list))       # eval能去除\n    {:},{:},...
            resident_new.append(d)   # 将转换后的字典添加到列表中[{:},{:},...]
   else:
       return
   paixu =input("请选择 （0 升序；1降序）：")
   if paixu == "0":   # 按升序排序
       mark = False  # 标记变量，为False表示升序排序
   elif paixu == "1":# 按降序排序
       mark = True # 标记变量，为True表示降序排序
   else:
       print("您的输入有误，请重新输入！")
       sort()
   mode = input("请选择排序方式（1按日期排序；2按体温排序）："
                )
   if mode ==  "1":
       resident_new.sort(key=lambda x:x["date"],reverse= mark )
   elif mode == "2":
       resident_new.sort(key=lambda x:x["temperature"],reverse = mark )
   else:
       print("您的输入有误，请重新输入！")
       sort()
   show_resident(resident_new)  # 显示排序结果



''' 6 统计居民总数'''

def total():
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            resident_old = rfile.readlines()  # 读取全部内容
            if resident_old:
                print("一共进出 %d 位居民！" % len(resident_old))
            else:
                print("还没有录入居民信息！")
    else:
        print("暂未保存数据信息...")


''' 7 显示所有居民信息 '''

def show():
    resident_new =[]
    if os.path.exists(filename):
        with open(filename,"r") as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            resident_new.append(eval(list))   # 将找到的居民信息保存到列表中
        if resident_new:
            show_resident(resident_new)
    else:
        print("暂未保存数据信息...")



#将保存在列表中的居民信息显示出来
def show_resident(residentList):
    if not residentList:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    format_title="{:^6}{:^8}{:^5}\t{:^10}\t{:<10}\t{:<15}"
    print(format_title.format("ID", "名字", "体温", "日期", "通讯号码", "通讯地址"))
    format_data = "{:^6}{:^8}{:^6}\t{:^10}\t{:^15}\t{:^15}"
    for info in residentList:
        print(format_data.format(
            info.get("id"), info.get("name"),
            str(info.get("temperature")), str(info.get("date")),
            str(info.get("phone")),
            str(info.get("adress"))
        ))


if __name__ == "__main__":
   main()
