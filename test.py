from tkinter import *
from tkinter import messagebox as box
import mysql.connector
# connecting the local database.
conn = mysql.connector.connect(user='root', password='1876', host='localhost')
# prepare a cursor object using cursor() method
mycursor = conn.cursor()

# execute SQL query using execute() method.
#mycursor.execute('''Drop Schema IF Exists Medical_BOT;''')
#mycursor.execute('''Create Schema MEDICAL_BOT;''')
mycursor.execute('''USE MEDICAL_BOT;''')

#mycursor.execute('''CREATE TABLE DEPARTMENT(
#Dept_Name VARCHAR (25) NOT NULL ,
#Department_No INT NOT NULL Primary Key);''')

#mycursor.execute('''CREATE TABLE USER(
#USER_ID INT NOT NULL Auto_increment PRIMARY KEY,
#User_name varchar(40) not null,
#TYPE_o_USER VARCHAR(20),
#ACCESS CHAR(10),
#PASS VARCHAR (15) NOT NULL,
#SEX VARCHAR(5) NOT NULL defaul "U",
#Dept int not null,  
#Constraint `Did` foreign key(Dept) references DEPARTMENT(Department_No));''') 

#mycursor.execute('''CREATE TABLE TASK(
#TASK_ID INT NOT NULL PRIMARY KEY,
#NAME_o_PERSON CHAR(30) NOT NULL,
#JOB_TITLE CHAR(10) NOT NULL,
#REQUESTED_ITEM CHAR(30) NOT NULL,
#TASK_STATUS CHAR(3),
#PRIORITY  INT NOT NULL);''')



def Prd(x):
    x = Tk();
    x.title('Login Screen')
    frame = Frame(x)

def Des(x):
    x.destroy()

def dialog1():
    username=entry1.get()
    password = entry2.get()
    user , pass_w = login(username)

    if (username == user and  password == pass_w):
        box.showinfo('info','Correct Login')
        Des(window)
    else:
        box.showinfo('info','Invalid Login')

def dialog2():
    box.showinfo('SignUp')
    
    username = entry1.get()
    password = entry2.get()
    dept  =entry3.get()
    if (login(username) == None):
        SignUp(username,password,dept)
        box.showinfo('info','SignUp Successful')
    else:
        box.showinfo("info", 'Signup Failed Try a different username')
def login(username):
    sql  = '''Select User_name,PASS from User where User_name  = %s'''
    data  = (username,)
    mycursor.execute(sql,data)
    result = mycursor.fetchall()
    for r in result:
        user  = r[0]
        passw = r[1]
    return user,passw
def SignUp(username, password,dept):
    sqlFormula = "Insert Into User(User_name, Pass,Dept) Value (%s,%s,%s)"
    data = (username, password,dept)
    mycursor.execute(sqlFormula, data)
    conn.commit()

def dept_info(deptname , no):
    sqlFormula = "Insert Into DEPARTMENT(Dept_name,Department_No) Value (%s,%s)"
    data = (deptname, no)
    mycursor.execute(sqlFormula, data)
    conn.commit()


window = Tk()
window.title('Login')

frame = Frame(window)
#5
Label1 = Label(window,text = 'Username:')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)



Label2 = Label(window,text = 'Password: ')
Label2.pack(padx = 15,pady=6)

entry2 = Entry(window, bd=5)
entry2.pack(padx = 15,pady=7)


btn = Button(frame, text = 'Sign In',command = dialog1)

btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)

window.mainloop()



#mycursor.execute("Show tables")

# Fetch a single row using fetchone() method.
#data = mycursor.fetchone()
#for d in data:
#    print(data)
#print ("Database version : %s " % data)


#mycursor.execute("Show tables")
#print(mycursor.fetchall())
#result = mycursor.fetchall()
#for r in result:
#   print(r)
dept_info("cardialogy",1)   
SignUp("asd","123",1)
username,password = login("asd")
print(username,password)

# disconnect from server
conn.close()
