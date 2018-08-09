from tkinter import *
import mysql.connector

'''
创建4个标签
创建4个显示框
一个点击执行获取信息的按钮
'''
#初始化界面
w = Tk()
w.geometry("400x400")
w.title('zipcode')

#连接数据库
conn = mysql.connector.connect(user="root",password="111111",database="zipcode",auth_plugin='mysql_native_password')
cursor = conn.cursor()

#按钮工作的函数
def show():
    var1 = v1.get()
    var2 = v2.get()
    var3 = v3.get()
    sql = "select * from zipcode where province="+ "'"+ var1+"'"+ " and city=" +"'"+var2+"'" + " and district=" +"'"+ var3+"'"

    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    label44.config(text=data[0][3])


#定义部件
label1 = Label(w, text='省份:')
label2 = Label(w, text='城市:')
label3 = Label(w, text='区县:')
label4 = Label(w, text='邮编:')
label44 = Label(w,text='',bg='white')
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
#v4 = StringVar()
entry1 = Entry(w, text='', textvariable=v1)
entry2 = Entry(w, text='', textvariable=v2)
entry3 = Entry(w, text='', textvariable=v3)
#entry4 = Entry(w, text='', textvariable=v4)

button1 = Button(w, text='搜索', command=show)

#摆放位置
label1.place(x=20, y=20, width=50, height=20)
label2.place(x=20, y=40, width=50, height=20)
label3.place(x=20, y=60, width=50, height=20)
label4.place(x=20, y=80, width=50, height=20)
label44.place(x=80,y=85,width=80, height=20)
entry1.place(x=80, y=20)
entry2.place(x=80, y=40)
entry3.place(x=80, y=60)
#entry4.place(x=80, y=80)
button1.place(x=80, y=110, width=100, height=40)



w.mainloop()
