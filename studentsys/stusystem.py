#作者：Ourjune
#开发时间：2021/12/28 19:
file_stu='students.txt'
import os
def menu():
    print('=======================================================================')
    print('------------------------------功能菜单----------------------------------')
    print('\t\t\t\t\t\t1、录入学生信息')
    print('\t\t\t\t\t\t2、查找学生信息')
    print('\t\t\t\t\t\t3、删除学生信息')
    print('\t\t\t\t\t\t4、修改学生信息')
    print('\t\t\t\t\t\t5、排序')
    print('\t\t\t\t\t\t6、统计学生总人数')
    print('\t\t\t\t\t\t7、显示所有学生信息')
    print('\t\t\t\t\t\t0、退出系统')
    print('-----------------------------------------------------------------------')
def main():
    while True:
        menu()
        try:
            choice=int(input('请选择以上菜单'))
        except ValueError:
            print('只能输入数字串哦！！')
        if choice in range(0,8):
            if choice==0:
                answer=input('你确定要退出系统吗y/n')
                if answer=='y'or answer=='Y':
                    print('谢谢您的使用！')
                    break #退出系统
                else:
                    continue
            elif choice==1:
                insert()  #录入学生
            elif choice==2:
                search()  #查找学生
            elif choice==3:
                delete()  #删除学生
            elif choice==4:
                modify()  #修改学生
            elif choice==5:
                sort()    #排序
            elif choice==6:
                total()   #统计学生总人数
            elif choice==7:
                show()    #显示出所有学生信息
def insert():
    stu_list=[]
    while True:
        id=int(input('请输入学号（如1001）：'))
        name=input('请输入姓名：')
        if not id:
            break
        elif not name:
            break
        try:
            english=input('请输入英语成绩')
            math=input('请输入数学成绩')
            chinese=input('请输入语文成绩')
        except:
            print('输入成绩不合法,请重新输入')
            continue
        stu_dict={'id':id,'name':name,'english':english,'math':math,'chinese':chinese}
        stu_list.append(stu_dict)
        anser=input('是否继续添加？y/n\n')
        if anser=='y'or anser=='Y':
            continue
        else:
            break
    #调用save（）函数
    save(stu_list)
    print('学生信息录入完毕！！')
def save(list):
    try:
        file=open(file_stu,'a',encoding='utf-8')
    except:
        file=open(file_stu,'w',encoding='utf-8')
    for item in list:
        file.write(str(item)+'\n')
    file.close()
def search():
    student_qury=[]
    while True:
        id=''
        name=''
        if os.path.exists(file_stu):
            mode=input('输入1表示按id查找，输入2表示按姓名查找')
            if mode=='1':
                id=int(input('请输入需要查询的id:'))
            elif mode=='2':
                name=input('请输入需要查询的姓名:')
            else:
                print('你输入有误，请重新输入!')
                search()
            with open(file_stu,'r',encoding='utf-8')as rfile:
                r1=rfile.readlines()
                for item in r1:
                    d=dict(eval(item))
                    if d['id']!=''or d['name']!='':
                        if d['id'] == id:
                            student_qury.append(d)
                        elif d['name'] == name:
                            student_qury.append(d)
            #显示查询结果
            show_student(student_qury)
            #清空列表
            student_qury.clear()
            answer=input('是否要继续查询y/n\n')
            if answer=='y'or answer=='Y':
                continue
            else:
                break
        else:
            print('无学生信息！！')
def show_student(lst):
    if len(lst)==0:
        print('没有查询到学生信息')
        return
    #定义标题显示格式
    format_title='{:^6}\t{:^6}\t{:^8}\t{:^6}\t{:^1}\t{:^10}'
    print(format_title.format('Id','姓名','英语成绩','数学成绩','语文成绩','总成绩'))
    #定义内容显示格式
    format_data='{:^6}\t{:^7}\t{:^4}\t{:^8}\t{:^7}\t{:^11}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('math'),
                                 item.get('chinese'),
                                 int(item.get('english'))+int(item.get('math'))+int(item.get('chinese'))
                                 ))
def delete():
    while True:
        stu_id = int(input('请输入需要删除的学生id：'))
        if stu_id!='':
            if os.path.exists(file_stu):
                with open(file_stu,'r',encoding='utf-8')as file:
                    f1=file.readlines()  #读出来的放进列表
            else:
                f1=[]
            flag=False  #标记是否删除
            if f1:
                with open(file_stu,'w',encoding='utf-8')as wfile:
                    d={}
                    for item in f1: #遍历出来的是字符串类型
                        #print(type(item),item)
                        d=dict(eval(item))  #将字符串转换成字典存储
                        #print(type(d),d)
                        if d['id']!=stu_id:
                            #print(str(d)+'\n')
                            wfile.write(str(d)+'\n')
                        else:
                            flag=True
                    if flag:
                        print('id为{0}的学生已经被删除！！'.format(stu_id))
                    else:
                        print('没有找到id为{0}的学生！'.format(stu_id))
            else:
                print('无学生信息')
                break
            show()
            anser=input('是否继续删除？y/n')
            if anser == 'y' or anser == 'Y':
                continue
            else:
                break
def modify():
    show()
    if os.path.exists(file_stu):
        with open(file_stu,'r',encoding='utf-8')as file:
            stu_old=file.readlines()
    else:
        return
    stu_id = int(input('请输入需要修改的学生id'))
    if stu_id!='':
        with open(file_stu, 'w', encoding='UTF-8')as wfile:
            for item in stu_old:
                d=dict(eval(item))
                if d['id']==stu_id:
                    print('找到学生信息，可以修改她的相关信息了！')
                    while True:
                        try:
                            d['name']=input('请输入姓名：')
                            d['english']=input('请输入英语成绩：')
                            d['python']=input('请输入数学成绩：')
                            d['java']=input('请输入语文成绩：')
                        except:
                            print('您输入的有误，请重新输入！！')
                        else:
                            break
                    wfile.write(str(d)+'\n')
                    print('信息修改完成！')
                else:
                    wfile.write(str(d)+'\n')  #将未修改的信息写入文件
            answer=input('是否继续修改y/n\n')
            if answer=='y'or answer=='Y':
                modify()
def sort():
    show()
    stu_sortlist=[]
    if os.path.exists(file_stu):
        with open(file_stu,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
        for item in students:
            stu_sortlist.append(dict(eval(item)))
        choose1=int(input('请选择（0升序，1降序）：'))
        if choose1==0:
            asc_or_desc_bool=False
        elif choose1 == 1:
            asc_or_desc_bool = True
        else:
            print('你的输入不合法！')
            sort()
        choose2=int(input('请选择排序方式（1按英语成绩排，2按数学成绩排，3按语文成绩排，0按总成绩排）：'))
        if choose2==1:
            stu_sortlist.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool)
        elif choose2==2:
            stu_sortlist.sort(key=lambda x:int(x['math']),reverse=asc_or_desc_bool)
        elif choose2==3:
            stu_sortlist.sort(key=lambda x:int(x['chinese']),reverse=asc_or_desc_bool)
        elif choose2==0:
            stu_sortlist.sort(key=lambda x:(int(x['english'])+int(x['math'])+int(x['chinese'])),reverse=asc_or_desc_bool)
        else:
            print('您输入的不合法！！')
            sort()
        show_student(stu_sortlist)
    else:
        return
def total():
    if os.path.exists(file_stu):
        with open(file_stu,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
            if students!='':
                print('学生目前一共有{}个'.format(len(students)))
            else:
                print('学生信息为空！')
    else:
        print('您还没有录入学生信息！！')
def show():
    stu_list=[]
    if os.path.exists(file_stu):
        with open(file_stu,'r',encoding='utf-8')as rfile:
            r=rfile.readlines()
        for item in r:
            stu_list.append(dict(eval(item)))
        if stu_list:
            show_student(stu_list)
        else:
            print('学生信息为空！！！')
    else:
        print('暂未保存学生数据！！')
if __name__ == '__main__':
    main()
