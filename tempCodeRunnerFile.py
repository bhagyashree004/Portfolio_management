import sqlite3
from tkinter import*
import os    # for os.system
from tkinter import ttk    
from tkinter import messagebox as ms  # for messagebox
import tkinter

def main():
    root = Tk()
    app = user(root)    
# make database and users (if not exists already) table at programme start up
with sqlite3.connect('Users.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL)')
db.commit()
db.close()

#main Class
class user:
    def __init__(self,master):
    	# Window 
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        #Create Widgets
        self.widgets()

    #Login Function
    def login(self):
    	#Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            # close this window
            self.master.destroy()
            # open new window
            os.system('python ' + 'Portfolio_frontend.py')
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
    	#Establish Connection
        with sqlite3.connect('Users.db') as db:
            c = db.cursor()

        #Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Already Taken!')
        else:
            ms.showinfo('Success!','Account Created!')
            self.log()
        #Create New Account 
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
        db.commit()

        #Frame Packing Methods
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'LOGIN'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'REGISTER'
        self.crf.pack()
        
    #Draw Widgets
    def widgets(self):
        self.head = Label(self.master,text = ' LOGIN  |  REGISTER ', bg="powderblue",font = ('Product Sans',20),pady = 5)
        self.head.pack()
        lab1 = Label(self.master,text = '________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'
                          , bg="DeepSkyBlue4", fg="skyblue4", font = ('Product Sans',1))
        lab1.pack(side = TOP,expand = False)
        
        lab2 = Label(self.master,text = '_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'
                          , bg="steel blue", fg="steelblue", font = ('Product Sans',1))
        lab2.pack()
        lab2.place(x=20,y=47.5)
        lab3 = Label(self.master,text = '____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'
                          , bg="DeepSkyBlue2", fg="skyblue3", font = ('Product Sans',1))
        lab3.pack()
        lab3.place(x=20,y=47.5)
        lab4 = Label(self.master,text = '______________________________________________________________________________________________________________________'
                          , bg="skyblue2", fg="skyblue2", font = ('Product Sans',1))
        lab4.pack()
        lab4.place(x =20,y=47.5)
        self.crf=Frame(self.master, padx=10, pady=50)
        self.logf = Frame(self.master ,padx =50,pady = 50)
        Label(self.logf,text = 'Username: ',font = ('Product Sans',15),pady=15,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 6,font = ('',17)).grid(row=0,column=2)
        Label(self.logf,text = 'Password: ',font = ('Product Sans',15),pady=30,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 6,font = ('',17),show = '*').grid(row=1,column=2)
        Button(self.logf,text = ' LOGIN ',bd = 3 ,font = ('',10),padx=5,pady=5,command=self.login, bg="black", fg="white").grid(column=1)
        Button(self.logf,text = ' REGISTER ',bd = 3 ,font = ('',10),padx=5,pady=5,command=self.cr, bg="black", fg="white").grid(row=2,column=2)
        self.logf.pack()

        
        self.crf = Frame(self.master, padx =60,pady=60)
        Label(self.crf,text = 'Username: ',font = ('Product Sans',15),pady=15,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 6,font = ('',15)).grid(row=0,column=2)
        Label(self.crf,text = 'Password: ',font = ('Product Sans',15),pady=30,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 6,font = ('',15),show = '*').grid(row=1,column=2)
        Button(self.crf,text = 'REGISTER',bd = 3 ,font = ('',10),padx=5,pady=5,command=self.new_user, bg="black", fg="white").grid(column=1)
        Button(self.crf,text = 'GO TO LOGIN',bd = 3 ,font = ('',10),padx=5,pady=5,command=self.log, bg="black", fg="white").grid(row=2,column=2)

if __name__=='__main__':
    root = Tk()
    root.resizable(False,False)
    root.configure(bg='powderblue')
    root.geometry("600x500+1000+300")
    root.title('Login Form')
    application = user(root)
    root.mainloop()