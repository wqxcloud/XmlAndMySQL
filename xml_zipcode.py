from xml.dom.minidom import parse
import xml.dom.minidom
import mysql.connector

#连接数据库
conn = mysql.connector.connect(user="root",password="111111",database="zipcode",auth_plugin='mysql_native_password')
cursor = conn.cursor()

#使用Minidom解析器打开xml文档
DOMTree = xml.dom.minidom.parse("最新的省市区数据.xml")
#取根目录数据
root = DOMTree.documentElement


#取各省信息
provinces = root.getElementsByTagName("province")
for province in provinces:
    if province.hasAttribute("name"):
        print("Province: %s \n" % province.getAttribute("name"))

    # 取各城市信息
    citys = province.getElementsByTagName("city")
    for city in citys:
        if city.hasAttribute("name"):
            print("\t city: %s " % city.getAttribute("name"))

        #取各区信息
        districts = city.getElementsByTagName("district")
        for district in districts:
            if district.hasAttribute("name"):
                print("\t \t district: %s \t zipcode: %s" % (district.getAttribute("name"),district.getAttribute("zipcode")))


        #插入数据
        cursor.execute("insert into zipcode(province,city,district,zipcode) values(%s,%s,%s,%s)",
                       (province.getAttribute("name"),city.getAttribute("name"),district.getAttribute("name"),district.getAttribute("zipcode")))
#提交数据
conn.commit()
#关掉数据库
cursor.close()
conn.close()





