import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",passwd="")


mycursor=mydb.cursor()

mycursor.execute("create database Library")
mycursor.execute("use Library")
mycursor.execute("CREATE TABLE `STOCK` (""`ID` INTEGER(10)," "`Book_name` VARCHAR(250)," "`Book_author` VARCHAR(250)," "`Published_Year` VARCHAR(30)," "`Number_of_books` INTEGER(15)," "`Price` INTEGER(15)"")")

mycursor.execute("CREATE TABLE `Customer` (""`ID` INTEGER(10)," "`Name_of_Book_Buyed` VARCHAR(150)," "`phone_no` VARCHAR(250)," "`total` INTEGER(20)"")")

print("Stock table Created")
print("Customer table Created")
insert1 = "INSERT INTO `STOCK`(`ID`,`Book_name`,`Book_author`,`Published_Year`,`Number_of_books`,`Price`) VALUES(%s, %s, %s, %s, %s, %s)"

value1=[(1,"The Theory of Everything","Stephen Hawking",'2007',20,400),
        (2,"Fast Track Objective Arithmetic","Rajesh Verma",'2018',15,425),
        (3,"Objective Computer Awareness","Arihant Experts",'2016',30,135),
        (4,"Organic Chemistry: Second Edition","Jonathan Clayden",'2014',5,2000),
         (5,"Handbook of Biology","Arihant Experts",'2019',20,500)]

mycursor.executemany(insert1,value1)



insert2 = "INSERT INTO Customer(`ID`,`Name_of_Book_Buyed`,`phone_no`,`total`) VALUES(%s, %s, %s, %s)"

value2=[(1,"Fast Track Objective Arithmetic",'1234567898',425),
        (2,"Organic Chemistry: Second Edition",'4325678965',2000),
        (3,"Handbook of Biology",'2134532134',500),
        (4,"Fast Track Objective Arithmetic",'1232453212',425)]


mycursor.executemany(insert2,value2)


mydb.commit()


class Books:  
    
    def view(self):
        sql="select * from Customer"
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        for result in myresult:
            print(result)


    def view_stock(self):
        mycursor.execute("select * from Stock")
        myresult=mycursor.fetchall()
        for result in myresult:
            print(result)


    def add(self):
        sqlformula = "INSERT INTO Customer(ID,Name_of_Book_Buyed,phone_no,total) VALUES(%s, %s, %s, %s)"
        print("Enter the details to be added in table")
        id0=input("ID : ")
        name_of_book_buyed=input("Name of Book Buyed: ")
        phone_number=input("Phone Number of customer : ")
        total=input("Total Price : ")
        value=[(id0,name_of_nook_buyed,phone_number,total)]
        mycursor.executemany(sqlformula, value)
        mydb.commit()


    def add_stock(self):
        sqlformula = "INSERT INTO STOCK(ID,Book_name,Book_author,Published_Year,Number_of_books,Price) VALUES(%s, %s, %s, %s, %s, %s)"
        print("Enter the details to be added in table")
        id0=input("ID : ")
        name=input("Book Name : ")
        author=input("Author Name : ")
        year=input("Published Year : ")
        totalbooks=input("Number of Books : ")
        price=input("Price : ")
        value=[(id0,name,author,year,totalbooks,price)]
        mycursor.executemany(sqlformula, value)
        mydb.commit()


    def delete(self):
        id0=input("Enter the ID be deleted : ")
        mycursor.execute("delete from Customer where ID="+id0)
        mydb.commit()


    def delete_stock(self):
        id0=input("Enter the ID be deleted : ")
        mycursor.execute("delete from STOCK where ID="+id0)
        mydb.commit()


    def update(self):
        id0=input("Enter the ID to be updated : ")
        updatething=input("Enter the column to update : ")
        value=input("Enter the value of column to updated : ")
        mycursor.execute("update `Customer` set %s=%s where ID ='%s' "%(updatething,value,id0))
        mydb.commit()


    def update_stock(self):
        id0=input("Enter the ID to be updated : ")
        updatething=input("Enter the column to update : ")
        value=input("Enter the value of column to updated : ")
        mycursor.execute("update `STOCK` set %s=%s where ID ='%s' "%(updatething,value,id0))
        mydb.commit()






print("Press : ")
print("1 - Customer Table")
print("2 - Stock Table")
press=int(input())


if(press==1):
    obj=Books()
    print("Press :")
    print("1 - To view the table customer")
    print("2 - To add new row to table customer")
    print("3 - To delete any row of table customer")
    print("4 - To update the table customer")
    press1=int(input())
    if(press1==1):
        obj.view()
    if(press1==2):
        obj.add()
    if(press1==3):
        obj.delete()
    if(press1==4):
        obj.update()


elif(press==2):
    obj1=Books()
    print("1 - To view the table stock")
    print("2 - To add new row to table stock")
    print("3 - To delete any row of table stock")
    print("4 - To update the table stock")
    press2=int(input())
    if(press2==1):
        obj1.view_stock()
    if(press2==2):
        obj1.add_stock()
    if(press2==3):
        obj1.delete_stock()
    if(press2==4):
        obj1.update_stock()
