import sqlite3 as sql
import tkinter as tk
import tkinter.font as tkFont


class bookFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        
        self.search_type = tk.StringVar()
        
        l1 = tk.Label(self,text="Choose Books", font=self.titlefont)
        l1.grid(row=0,column=0)
        
        
        
        
        
        author_radiobutton = tk.Radiobutton(self,text="Search By Author", value = "author", variable=self.search_type)
        title_radiobutton = tk.Radiobutton(self,text="Search By Title", value = "title", variable=self.search_type)
        
        author_radiobutton.grid(row=1,column=1)
        title_radiobutton.grid(row=1,column=2)
        
        self.search_box = tk.Entry(self) 
        self.search_box.grid(row=1,column=0)
        
        self.books_listbox = tk.Listbox(self)
        self.books_listbox.grid(row=2,column=0)
        
        self.search_button = tk.Button(self,command=self.update_book_list)
        self.grid(row=1,column=2)
        
    def update_book_list(self):
        
        search_term = self.search_box.get()
        
        search_result_list = self.parent.cursor.execute("SElECT * FROM books WHERE ? LIKE '%||?||%'", (self.search_type,search_term)).fetchall()
        
        
    
    
        
        

    def loadUp(self):
        # put code in here to be run when this frame is displayed
        pass


