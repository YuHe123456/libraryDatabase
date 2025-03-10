import sqlite3 as sql
import tkinter as tk
import tkinter.font as tkFont


class loginFrame(tk.Frame):
    def __init__(self, parent):
        
        
        tk.Frame.__init__(self, parent)

        self.parent = parent
        # The parent is a link to the main App. If you need to remember values "globally",
        # you should store them in self.parent
        # 
        # for example:
        self.parent.loggedInUser = None
        
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")

        l1 = tk.Label(self,text="Welcome to the Library", font=self.titlefont)
        l1.grid(row=0,column=0,columnspan=2)

        # Add code here to display a login screen
        
        username = tk.Label(self,text="Username:", font=self.titlefont)
        username.grid(row=1,column=0,sticky="W")
        password = tk.Label(self,text="Password:", font=self.titlefont)
        password.grid(row=2,column=0,sticky="W")
        
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1,column=1)
        self.password_entry = tk.Entry(self,show="*")
        self.password_entry.grid(row=2,column=1)
        
        self.submit_button = tk.Button(self,text="Submit",command=self.submit)
        self.submit_button.grid(row=3,column=1,columnspan=2,sticky="NEWS")
        
        self.error_label = tk.Label(self,fg="red")
        self.error_label.grid(row=3,column=4)
        
        
        
        
        # Do not run any actual code in __init__
        # Because this will be run as soon as the program loads

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        
        
        self.username_entry.focus()
        self.parent.bind("<Return>", self.submit)


    def submit(self):
        # check the contents of the entry boxes and see if they have logged in correctly
        # if so, set self.parent.loggedInUser
        
        p_username = self.username_entry.get()
        p_password = self.password_entry.get()
        
        print(p_username,p_password)
        
        results = self.parent.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",(p_username,p_password))
        
        results = results.fetchall()
        
        print(results, "result")
        
        if len(results) == 1:
            self.parent.loggedInUser = p_username
            print("frame switched")
            self.parent.switchFrame("books")
        
        else:
            self.error_label.configure(text="Wrong Username or Password")
        
        
        
        

        # Then switch frames
        