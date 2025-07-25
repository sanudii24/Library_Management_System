import mysql.connector as a
con=a.connect(host="localhost",user="root",password="S3r$7Lp!wB#2xQz4",database="library")

def addbook():
    bn=input("Enter BOOK Name : ")
    c=input("Enter BOOK code : ")
    t=input("Enter Total Books : ")
    s=input("Enter Subject : ")
    data=(bn,c,t,s)
    sql="insert into books values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("")
    print("Data Entered Successfully")
    main()

def issueb():
    n=input("Enter Name : ")
    r=input("Enter Reg : ")
    co=input("Enter Book code : ")
    d=input("Enter Date : ")
    a="Insert into issue values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("")
    print("Book issued to : ",n)
    bookup(co,-1)

def submitb():
    n=input("Enter Name : ")
    r=input("Enter  Reg NO : ")
    co=input("Enter Book code : ")
    d=input("Enter Data : ")
    a="Insert into submit values(%s,%s,%s,%s)"
    data=(n,r,co,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print("")
    print("Data Submitted from : ",n)
    bookup(co,1)

def bookup(co,u):
    a="Select Total from books where Bcode=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set total=%s where bcode=%s"
    d=(t,co)
    c.execute(sql,d)
    con.commit()
    main()

def dbook():
    ac=input("Enter Book Code : ")
    a="delete from books where bcode=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()

def dispbook():
    a="Select * from books"
    c =con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name : ",i[0])
        print("Book Code : ",i[1])
        print("Totall : ",i[2])
    main()

def main():
    print("""  

                LIBRARY MANAGER
          1.ADD BOOK
          2.ISSUE BOOK
          3.SUBMIT BOOK
          4.DELETE BOOK
          5.DISPLAY BOOKS
          6.EXIT
""")
    choice=input("Enter Task No : ")
    if(choice=='1'):
        addbook()
    elif(choice=='2'):
        issueb()
    elif(choice=='3'):
        submitb()
    elif(choice=='4'):
        dbook()
    elif(choice=='5'):
        dispbook()
    elif(choice=='6'):
        exit()
    else:
        print("Wrong choice....")
        main()
def pswd():
    ps=input("Enter Password : ")
    if ps=="lib24":
        main()
    else:
        print("Wrong Password")
        pswd()
pswd()
