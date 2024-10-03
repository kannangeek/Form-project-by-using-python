from tkinter import *
from tkinter import messagebox
import pymysql


def Login():
    username=entry2.get()
    password = entry3.get()
    if username == '' or password == '':
        messagebox.showerror('login','Entering any character is must.')
    else:
        try:
            connect = pymysql.connect(
                host = 'localhost',
                user = 'username',
                password = 'password',
                database = 'user_db'
            )
            cursor = connect.cursor()
            #checking password exist
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",
                           (username,password))
            result = cursor.fetchone()
            if result:
                messagebox.showinfo('login','Login is successful')
                root.destroy()
                top = Tk()
                top.configure(bg='white')
                label4 = Label(top,text='Welcome to the New Page',font=('arial',30),bg='white')
                label4.place(x=600,y=300)
            else:
                messagebox.showerror('login','incorrect username or password')
        except pymysql.MySQLError as err:
              messagebox.showerror('Error','Error occurs')
        finally:
            if connect:
              connect.close()

                  
root = Tk()
root.configure(bg="cyan4")
global entry2
global entry3

label1 = Label(root,text="Login page", bg="cyan4",fg='cyan',font=('areal',50))
label1.place(x=650,y=50)

label2 = Label(root,text="User Name:",bg='cyan4',fg='white',font=('arial',20))
label2.place(x=500,y=150)
entry2 = Entry(root,font=('arial',18))
entry2.place(x=680,y=150)

label3 = Label(root,text="Password:",bg='cyan4',fg='white',font=('arial',20))
label3.place(x=500,y=200)
entry3 = Entry(root,font=('arial',18))
entry3.place(x=680,y=200)


submit_button =Button(root,text='Login',bg='cyan3',font=('arial',15),bd=5,command=Login)
submit_button.place(x=750,y=300)

root.mainloop()
