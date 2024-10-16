import tkinter as tk
from tkinter import messagebox
import pymysql

class HotelManagementSystem:
    def __init__(self, root):
        self.window = root
        root.configure(bg="lightblue")
        root.title("Hotel Management System")
        root.geometry("600x400")  # Set the window size

        #mysql database
        self.connect = pymysql.connect(
            host = "localhost",
            user="root",
            password = "Infosecured@$#321",
            database = "hotel_management"
        )

        self.cursor = self.connect.cursor()

        # main menu frame
        self.main_menu_frame = tk.Frame(root, bg="lightblue", width=300, height=200)
        self.main_menu_frame.place(x=100, y=100)

        # creating label for header
        self.header = tk.Label(root,text="Welcome To The Hotel",font=('arial',20),bg='lightblue')
        self.header.place(x=100,y=100)
        # login button
        self.login_button = tk.Button(self.main_menu_frame, text="Login", command=self.open_login, font=('arial', 15), bg='cyan4')
        self.login_button.place(x=50, y=50)

        # sign up button
        self.signup_button = tk.Button(self.main_menu_frame, text='Sign Up', command=self.open_signup, font=('arial', 15), bg='cyan4')
        self.signup_button.place(x=50, y=100)

    
    def clearscreen(self):
        # Clear the main menu frame and header
        for widget in self.main_menu_frame.winfo_children():
            widget.place_forget()
        self.header.place_forget()
    

    def open_login(self):
        messagebox.showinfo("LOGIN", "Login window opened")

        self.clearscreen()
        # Create and pack the login label
        self.header_label1 = tk.Label(root, text="Login Here", bg="cyan4", font=('arial', 20, 'bold'))
        self.header_label1.place(x=600, y=10)  # Adjusted position for the header


        # Create and pack the username label and entry
        self.username_label1 = tk.Label(root, text="Username", bg="cyan4")
        self.username_label1.place(x=520,y=60)

        self.username_entry1 = tk.Entry(root,bg="black",fg="white",font=('arial',13))
        self.username_entry1.place(x=600,y=60,width=200)

        # create the password block
        self.password_label1 = tk.Label(root,text="Password",bg="cyan4")
        self.password_label1.place(x=520,y=90)

        self.password_entry1 = tk.Entry(root,fg="White",bg="black",font=('arial',13))
        self.password_entry1.place(x=600,y=90,width=200)

        self.login_submit_button = tk.Button(self.window, text="Submit",command = self.login_submit, font=('arial', 15), bg='cyan4')
        self.login_submit_button.place(x=600, y=130)

    def open_signup(self):
        messagebox.showinfo("Sign Up", "Sign Up window opened")
        self.clearscreen()

         #sign up label
        self.header_label2 = tk.Label(root,text="SignUp Page",bg="cyan4",font=('arial',20,'bold'))
        self.header_label2.place(x=600,y=180)

        
        # Create and pack the username label 2 and entry 2
        self.username_label2 = tk.Label(root, text="Username", bg="cyan4")
        self.username_label2.place(x=520,y=240)

        self.username_entry2 = tk.Entry(root,bg="black",fg="white",font=('arial',13))
        self.username_entry2.place(x=600,y=240,width=200)

        # create the password block 2
        self.password_label2 = tk.Label(root,text="Password",bg="cyan4")
        self.password_label2.place(x=520,y=280)

        self.password_entry2 = tk.Entry(root,fg="White",bg="black",font=('arial',13))
        self.password_entry2.place(x=600,y=280,width=200)

        self.signup_submit_button = tk.Button(self.window, text="Submit",command = self.signup_submit, font=('arial', 15), bg='cyan4')
        self.signup_submit_button.place(x=630, y=320)

    def login_submit(self):
        username_details = self.username_entry1.get()
        password_details = self.password_entry1.get()

        sql = "SELECT * FROM USERS WHERE username = %s AND password = %s"
        self.cursor.execute(sql,(username_details,password_details))
        result = self.cursor.fetchone()

        #showing info
        if result:
            messagebox.showinfo("success","Login is success")
        else:
            messagebox.showerror("Failed","Sorry,Invalid username or password")
        

    def signup_submit(self):
        username_details = self.username_entry2.get()
        password_details = self.password_entry2.get()

        #inserting data into the database
        try:
            sql = "INSERT INTO users (username,password) values (%s,%s)"
            self.cursor.execute(sql,(username_details,password_details))
            self.connect.commit()
            messagebox.showinfo('Success','Username and password registered successfully')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to register user: {str(e)}")
        finally:
            self.username_entry2.delete(0, tk.END)
            self.password_entry2.delete(0, tk.END)
    
    def on_closing(self):
        self.connect.close()  # Close the database connection
        self.window.destroy()        

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()