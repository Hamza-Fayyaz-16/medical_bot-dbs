import tkinter as t
from tkinter import messagebox as box
import mysql.connector
# connecting the local database.
#conn = mysql.connector.connect(user='root', password='12345', host='localhost')
# prepare a cursor object using cursor() method
#mycursor = conn.cursor()

#mycursor.execute('''set foreign_key_checks = 0;''')
##execute SQL query using execute() method.
#mycursor.execute('''Drop Schema IF Exists Medical_BOT;''')
#mycursor.execute('''Create Schema MEDICAL_BOT;''')
#mycursor.execute('''USE MEDICAL_BOT;''')
#
#mycursor.execute('''CREATE TABLE DEPARTMENT(
#Dept_Name VARCHAR (25) NOT NULL ,
#Department_No INT NOT NULL Primary Key);''')
#
#mycursor.execute('''CREATE TABLE USER(
#USER_ID INT NOT NULL Auto_increment PRIMARY KEY,
#User_name varchar(40) not null,
#TYPE_o_USER VARCHAR(20),
#ACCESS CHAR(10),
#PASS VARCHAR (15) NOT NULL,
#SEX VARCHAR(5) NOT NULL default "U",
#Dept int not null,  
#Constraint Did foreign key(Dept) references DEPARTMENT(Department_No));''') 
#
#mycursor.execute('''CREATE TABLE TASK(
#TASK_ID INT NOT NULL PRIMARY KEY,
#NAME_o_PERSON CHAR(30) NOT NULL,
#JOB_TITLE CHAR(10) NOT NULL,
#REQUESTED_ITEM CHAR(30) NOT NULL,
#TASK_STATUS CHAR(3),
#PRIORITY  INT NOT NULL);''')



def Prd(x,y):
    x = t.Tk();
    x.title(y)
    f = t.Frame(x)

def Des(x):
    x.destroy()
    
#def Search():
#    sqlFormulaS = "#Enter Query for the Search"
#    data = ()
#    mycursor.execute(sqlFormulaS, data)
#    conn.commit()

#def login(username):
#    sql  = '''Select User_name,PASS from User where User_name  = %s'''
#    data  = (username,)
#    mycursor.execute(sql,data)
#    result = mycursor.fetchall()
#    for r in result:
#        user  = r[0]
#        passw = r[1]
#    return user,passw
    
def Menu():
    m = t.Tk()
    m.title('Menu')
    m1 = t.Frame(m)
    
    Label11 = t.Label(m,text = 'Username:')
    Label11.pack(padx=15,pady= 5)
    
    entry11 = t.Entry(m,bd =5)
    entry11.pack(padx=15, pady=5)
    
    Label22 = t.Label(m,text = 'Password: ')
    Label22.pack(padx = 15,pady=6)
    
    entry22 = t.Entry(m, bd=5)
    entry22.pack(padx = 15,pady=7)
    
    Label33 = t.Label(m,text = 'Department: ')
    Label33.pack(padx = 15,pady=8)
    
    entry33 = t.Entry(m,bd =5)
    entry33.pack(padx=15, pady=9)
    
    Label44 = t.Label(m,text = 'Job Title: ')
    Label44.pack(padx = 15,pady=10)
    
    entry44 = t.Entry(m,bd =5)
    entry44.pack(padx=15, pady=11)
    
    btn8 = t.Button(m1, text = 'Search')
    btn8.pack(side = t.RIGHT , padx =5)
    btn9 = t.Button(m1, text = 'End This',command = m.destroy)
    btn9.pack(side = t.RIGHT , padx =5)
    m1.pack(padx=100,pady = 19)
    m.mainloop()

def dialog1():
    username= entry1.get()
    password = entry2.get()
#    user , pass_w = login(username)
############################# or username == user /// or password == pass_w ####
    if (username == 'default' and  password == '123'):
        box.showinfo('info','Correct Login')
        Des(window)
    else:
        box.showinfo('info','Invalid Login')

#def SignUp(username, password,dept):
#    sqlFormula = "Insert Into User(User_name, Pass,Dept) Value (%s,%s,%s)"
#    data = (username, password,dept)
#    mycursor.execute(sqlFormula, data)
#    conn.commit()

#def dialog2():
#    box.showinfo('SignUp')
#    
#    username = entry1.get()
#    password = entry2.get()
#    dept  = entry3.get()
#    if (login(username) == None):
#        SignUp(username,password,dept)
#        box.showinfo('info','SignUp Successful')
#    else:
#        box.showinfo("info", 'Signup Failed Try a different username')

#def dept_info(deptname , no):
#    sqlFormula = "Insert Into DEPARTMENT(Dept_name,Department_No) Value (%s,%s)"
#    data = (deptname, no)
#    mycursor.execute(sqlFormula, data)
#    conn.commit()
#def Version():
#    mycursor.execute("Show tables")
#    
#    #Fetch a single row using fetchone() method.
#    data = mycursor.fetchone()
#    for d in data:
#        print(data)
#    print ("Database version : %s " % data)

        
        
def S():
    n = t.Tk()
    n.title('Menu')
    n1 = t.Frame(n)
    btn1 = t.Button(n, text = 'Sign In',command = dialog1)
    btn1.pack(side = t.RIGHT , padx =5)    
    btn2 = t.Button(n, text = 'Search',command = Menu)    
    btn2.pack(side = t.RIGHT , padx =5)
    btn3 = t.Button(n, text = 'Sign In',command = dialog1)    
    btn3.pack(side = t.RIGHT , padx =5)    
    btn4 = t.Button(n, text = 'Version')#command = Version)   
    btn4.pack(side = t.RIGHT , padx =5)
    btn5 = t.Button(n, text = 'Sign In',command = dialog1)   
    btn5.pack(side = t.RIGHT , padx =5)   
    btn6 = t.Button(n, text = 'Exit',command = n.destory)
                                               
    btn6.pack(side = t.RIGHT , padx =5)
    n1.pack(padx=100,pady = 19)
    n.mainloop()


window = t.Tk()
window.title('Login')

frame = t.Frame(window)
Label1 = t.Label(window,text = 'Username:')
Label1.pack(padx=15,pady= 5)

entry1 = t.Entry(window,bd =5)
entry1.pack(padx=15, pady=5)

Label2 = t.Label(window,text = 'Password: ')
Label2.pack(padx = 15,pady=6)

entry2 = t.Entry(window, bd=5)
entry2.pack(padx = 15,pady=7)

Label3 = t.Label(window,text = 'Department: ')
Label3.pack(padx = 15,pady=8)

entry3 = t.Entry(window,bd =5)
entry3.pack(padx=15, pady=9)

Label4 = t.Label(window,text = 'Job Title: ')
Label4.pack(padx = 15,pady=10)

entry4 = t.Entry(window,bd =5)
entry4.pack(padx=15, pady=11)


btn1 = t.Button(frame, text = 'Sign In',command = dialog1)

btn1.pack(side = t.RIGHT , padx =5)


btn3 = t.Button(frame, text = 'Sign In',command = dialog1)

btn3.pack(side = t.RIGHT , padx =5)

btn2 = t.Button(frame, text = 'Portal',command = S)

btn2.pack(side = t.RIGHT , padx =5)



frame.pack(padx=100,pady = 19)

window.mainloop()




#mycursor.execute("Show tables")
#print(mycursor.fetchall())
#result = mycursor.fetchall()
#for r in result:
#print(r)
#dept_info("cardialogy",1)   
#SignUp("asd","123",1)
#username,password = login("asd")
#print(username,password)

# disconnect from server
#conn.close()
