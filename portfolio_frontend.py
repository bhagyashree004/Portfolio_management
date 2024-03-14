from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
import portfolio_backend


class Portfolio:

    def __init__(self, root):
        self.root = root
        self.root.title('Manage your Portfolio')
        self.root.geometry('1331x560+10+10')
        self.root.config(bg='powder blue')

        self.Mtype = StringVar()
        self.refno = StringVar()
        self.fname = StringVar()
        self.surname = StringVar()
        self.address = StringVar()
        self.post = StringVar()
        self.mobno = StringVar()
        self.ID = StringVar()
        self.title = StringVar()
        self.Company = StringVar()
        self.borrow = StringVar()
        self.due = StringVar()
        self.loan = StringVar()
        self.yop = StringVar()
        self.edsn = StringVar()

        def Rec(event):
            try:
                global selected_tuple
                index = self.Listbox_2.curselection()[0]
                selected_tuple = self.Listbox_2.get(index)

                self.Entry_0.delete(0, END)
                self.Entry_0.insert(END, selected_tuple[1])
                self.Entry_1.delete(0, END)
                self.Entry_1.insert(END, selected_tuple[2])
                self.Entry_2.delete(0, END)
                self.Entry_2.insert(END, selected_tuple[3])
                self.Entry_3.delete(0, END)
                self.Entry_3.insert(END, selected_tuple[4])
                self.Entry_4.delete(0, END)
                self.Entry_4.insert(END, selected_tuple[5])
                self.Entry_5.delete(0, END)
                self.Entry_5.insert(END, selected_tuple[6])
                self.Entry_6.delete(0, END)
                self.Entry_6.insert(END, selected_tuple[7])
                self.Entry_7.delete(0, END)
                self.Entry_7.insert(END, selected_tuple[8])
                self.Entry_8.delete(0, END)
                self.Entry_8.insert(END, selected_tuple[9])
                self.Entry_9.delete(0, END)
                self.Entry_9.insert(END, selected_tuple[10])
                self.Entry_10.delete(0, END)
                self.Entry_10.insert(END, selected_tuple[11])
                self.Entry_11.delete(0, END)
                self.Entry_11.insert(END, selected_tuple[12])
                self.Entry_12.delete(0, END)
                self.Entry_12.insert(END, selected_tuple[13])

            except IndexError:
                pass

        def Insert():
            if (len(self.refno.get()) != 0):
                portfolio_backend.insert(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get(), self.address.get(), self.post.get(
                ), self.mobno.get(), self.ID.get(), self.title.get(), self.Company.get(), self.borrow.get(), self.due.get(), self.loan.get())
                self.Listbox_2.delete(0, END)
                self.Listbox_2.insert(END, (self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get(), self.address.get(), self.post.get(
                ), self.mobno.get(), self.ID.get(), self.title.get(), self.Company.get(), self.borrow.get(), self.due.get(), self.loan.get()))

        def Display():
            self.Listbox_2.delete(0, END)
            for row in portfolio_backend.view():
                self.Listbox_2.insert(END, row, str(' '))

        def Exit():
            root.destroy()
            return

        def Reset():
            self.Mtype.set('')
            self.refno.set('')
            self.fname.set('')
            self.surname.set('')
            self.address.set('')
            self.post.set('')
            self.mobno.set('')
            self.ID.set('')
            self.title.set('')
            self.Company.set('')
            self.borrow.set('')
            self.due.set('')
            self.loan.set('')
            self.Display.delete('1.0', END)
            self.Listbox_2.delete('0', END)

        def Delete():
            portfolio_backend.delete(selected_tuple[0])
            Reset()
            Display()

        def Update():
            portfolio_backend.delete(selected_tuple[0])
            portfolio_backend.insert(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get(), self.address.get(), self.post.get(
            ), self.mobno.get(), self.ID.get(), self.title.get(), self.Company.get(), self.borrow.get(), self.due.get(), self.loan.get())
            self.Listbox_2.delete(0, END)
            self.Listbox_2.insert(END, (self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get(), self.address.get(), self.post.get(
            ), self.mobno.get(), self.ID.get(), self.title.get(), self.Company.get(), self.borrow.get(), self.due.get(), self.loan.get()))

        def Details():
            self.Display.delete('1.0', END)
            self.Display.insert(END, 'ID: ' + self.ID.get() + '\n')
            self.Display.insert(END, 'Title: ' + self.title.get() + '\n')
            self.Display.insert(END, 'Company:  ' + self.Company.get() + '\n')
            self.Display.insert(END, 'Min qty: ' + self.edsn.get() + '\n')
            self.Display.insert(
                END, 'Year: \t' + self.yop.get() + '\n')
            self.Display.insert(END, 'Issued Date: ' +
                                self.borrow.get() + '\n')
            self.Display.insert(END, 'Due Date:' + self.due.get() + '\n')
            self.Display.insert(END, 'Annualized Return(%): ' +
                                self.loan.get() + '%' + '\n')

        Main_Frame = Frame(self.root, bg='powder blue')
        Main_Frame.grid()
        Title_Frame_1 = Frame(Main_Frame, width=100)
        Title_Frame_1.pack(side=TOP)
        Title_Frame_1.place(x=0)
        Title_Frame_3 = Frame(Main_Frame, width=100)
        Title_Frame_3.pack(side=TOP)
        Title_Frame_3.place(x=200)
        Title_Frame_2 = Frame(Main_Frame, width=100,bg='deep sky blue3',relief=RIDGE,bd=3)
        Title_Frame_2.pack(side=TOP)
        Title_Frame_2.place()

        self.lblTitle1 = Label(Title_Frame_3, font=('arial', 19, 'bold'), text='\t\t\t\t\t\t\t_______',
                              bg='DeepSkyblue2',fg='DeepSkyblue2', padx=13)
        self.lblTitle1.grid()
        self.lblTitle2 = Label(Title_Frame_1, font=('arial', 19, 'bold'), text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',
                              bg='Skyblue2',fg='Skyblue2', padx=13)
        self.lblTitle2.grid()
        self.lblTitle4 = Label(Title_Frame_2, font=('Product Sans', 15, 'bold'), justify='center', text='\tPORTFOLIO MANAGEMENT:\t\t',
                              bg='deep sky blue3', padx=13)
        self.lblTitle4.grid()

        Button_Frame = Frame(Main_Frame, width=1350, height=50,
                             relief=RIDGE,padx=100, bd=5, bg='powder blue')
        Button_Frame.pack(side=BOTTOM)

        Detail_Frame = Frame(Main_Frame, width=1350,
                             height=100, relief=RIDGE, bd=5, bg='powder blue')
        Detail_Frame.pack(side=BOTTOM)

        Data_Frame = Frame(Main_Frame, width=1350, height=400,
                           relief=RIDGE, bd=5, bg='powder blue')
        Data_Frame.pack(side=LEFT)

        Data_Frame1 = Frame(Main_Frame, width=130, height=400,
                           relief=RIDGE, bd=5, bg='powder blue')
        Data_Frame1.pack(side=RIGHT)
        
        Frame_1 = LabelFrame(Data_Frame, width=800, height=400, relief=FLAT, bd=5, bg='light blue',
                             text="Membership Info:", padx=20, pady=20, font=('Product sans', 10, 'bold'))
        Frame_1.pack(side=LEFT, padx=3)

        Frame_2 = LabelFrame(Data_Frame1, width=550, height=400, relief=FLAT, bd=5, bg='skyblue',
                             text="Stocks Availabe:", padx=0,pady=5, font=('Product Sans', 10, 'bold'))
        Frame_2.pack(side=RIGHT)

        self.Label_1 = Label(Frame_1, text='Member type', font=('Product Sans', 13, 'bold'), pady=2,
                             bg='light blue')
        self.Label_1.grid(row=0, column=0, sticky=W)
        self.Label_2 = Label(Frame_1, text='Reference No.', font=('Product Sans', 13, 'bold'), pady=2,
                             bg='light blue')
        self.Label_2.grid(row=1, column=0, sticky=W)
        self.Label_3 = Label(Frame_1, text='First Name', font=('Product Sans', 13, 'bold'), pady=2,
                             bg='light blue')
        self.Label_3.grid(row=2, column=0, sticky=W)
        self.Label_4 = Label(Frame_1, text='Surname', font=('Product Sans', 13, 'bold'), pady=2,
                             bg='light blue')
        self.Label_4.grid(row=3, column=0, sticky=W)
        self.Label_5 = Label(Frame_1, text='Address', font=('Product Sans', 13, 'bold'), pady=2,
                             bg='light blue')
        self.Label_5.grid(row=4, column=0, sticky=W)
        self.Label_6 = Label(Frame_1, text='Post Code', font=('Product Sans', 13, 'bold'), pady=2,
                             bg='light blue')
        self.Label_6.grid(row=5, column=0, sticky=W)
        self.Label_7 = Label(Frame_1, text='Mobile No.', font=('Product Sans', 13, 'bold'), pady=2,
                             bg='light blue')
        self.Label_7.grid(row=6, column=0, sticky=W)
        self.Label_8 = Label(Frame_1, text='ID', font=('Product Sans', 13, 'bold'), pady=2,
                             bg='light blue')
        self.Label_8.grid(row=0, column=2, sticky=W)
        self.Label_9 = Label(Frame_1, text='Title', font=('Product Sans', 13, 'bold'), pady=2,
                             bg='light blue')
        self.Label_9.grid(row=1, column=2, sticky=W)
        self.Label_10 = Label(Frame_1, text='Company', font=('Product Sans', 13, 'bold'), pady=2,
                              bg='light blue')
        self.Label_10.grid(row=2, column=2, sticky=W)
        self.Label_11 = Label(Frame_1, text='Issued Date', font=('Product Sans', 13, 'bold'), pady=2,
                              bg='light blue')
        self.Label_11.grid(row=3, column=2, sticky=W)
        self.Label_13 = Label(Frame_1, text='Due Date', font=('Product Sans', 13, 'bold'), pady=2,
                              bg='light blue')
        self.Label_13.grid(row=4, column=2, sticky=W)
        self.Label_13 = Label(Frame_1, text='Annualized Return(%)', font=('Product Sans', 13, 'bold'), pady=2,
                              bg='light blue')
        self.Label_13.grid(row=5, column=2, sticky=W)

        self.Entry_0 = ttk.Combobox(Frame_1, values=(' ', 'Individual', 'Group', 'Hybrid'),
                                    font=('Product Sans', 13, 'bold'), width=18, textvariable=self.Mtype)
        self.Entry_0.grid(row=0, column=1)
        self.Entry_1 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.refno)
        self.Entry_1.grid(row=1, column=1, padx=15)
        self.Entry_2 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.fname)
        self.Entry_2.grid(row=2, column=1, padx=15)
        self.Entry_3 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.surname)
        self.Entry_3.grid(row=3, column=1, padx=15)
        self.Entry_4 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.address)
        self.Entry_4.grid(row=4, column=1, padx=15)
        self.Entry_5 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.post)
        self.Entry_5.grid(row=5, column=1, padx=15)
        self.Entry_6 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.mobno)
        self.Entry_6.grid(row=6, column=1, padx=15)
        self.Entry_7 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.ID)
        self.Entry_7.grid(row=0, column=4, padx=15)
        self.Entry_8 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.title)
        self.Entry_8.grid(row=1, column=4, padx=15)
        self.Entry_9 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.Company)
        self.Entry_9.grid(row=2, column=4, padx=15)
        self.Entry_10 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.borrow)
        self.Entry_10.grid(row=3, column=4, padx=15)
        self.Entry_11 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.due)
        self.Entry_11.grid(row=4, column=4, padx=15)
        self.Entry_12 = Entry(Frame_1, font=(
            'Product Sans', 13, 'bold'), width=20, textvariable=self.loan)
        self.Entry_12.grid(row=5, column=4, padx=15)

        self.Display = Text(Frame_2, font=(
            'arial', 13, 'bold'), width=28, height=11.5)
        self.Display.grid(row=0, column=2)

        List_of_Books = [' DOLLEX', ' KFINTECH', ' UMA', ' ELIN', ' ALAN']


        def SelectedBook(event):
            value = str(self.Listbox_1.get(self.Listbox_1.curselection()))
            v = value

            if (v == ' DOLLEX'):
                self.ID.set('ISBN 525341')
                self.title.set('DOLLEX')
                self.Company.set('Dollex Argotech Ltd')
                self.yop.set('2022')
                self.edsn.set('4000')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=14)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('14')
                self.due.set(d3)
                Details()
            elif (v == ' KFINTECH'):
                self.ID.set('ISBN 345687')
                self.title.set('KFINTECH')
                self.Company.set('KFinTech Solutions Ltd')
                self.yop.set('2019')
                self.edsn.set('40')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=10)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('10')
                self.due.set(d3)
                Details()
            elif (v == ' UMA'):
                self.ID.set('ISBN 643842')
                self.title.set('UMA')
                self.Company.set('UMA Solutions Ltd')
                self.yop.set('2017')
                self.edsn.set('2000')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=13)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('13')
                self.due.set(d3)
                Details()
            elif (v == ' ELIN'):
                self.ID.set('ISBN 564524')
                self.title.set('ELIN')
                self.Company.set('ELIN Electronics Ltd')
                self.yop.set('2018')
                self.edsn.set('60')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=13)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('13')
                self.due.set(d3)
                Details()
            elif (v == ' ALAN'):
                self.ID.set('ISBN 735893')
                self.title.set('ALAN')
                self.Company.set('Alan Solutions Ltd')
                self.yop.set('2021')
                self.edsn.set('1200')

                import datetime

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = (d1 + d2)
                self.borrow.set(d1)
                self.loan.set('15')
                self.due.set(d3)
                Details()

        self.Listbox_1 = Listbox(Frame_2, font=(
            'arial', 13, 'bold'), width=20, height=11)
        self.Listbox_1.bind('<<ListboxSelect>>', SelectedBook)
        self.Listbox_1.grid(row=0, column=0)

        self.Listbox_2 = Listbox(Detail_Frame, font=(
            'arial', 13, 'bold'), width=144, height=8)
        self.Listbox_2.bind('<<ListboxSelect>>', Rec)
        self.Listbox_2.grid(row=1, column=0)

        for items in List_of_Books:
            self.Listbox_1.insert(END, items)

        Button_1 = Button(Button_Frame, text='ADD', font=(
            'Product Sans', 10, 'bold'), bg='deep sky blue2',fg='black', width=10, command=Insert)
        Button_1.grid(row=0, column=0, padx=40, pady=10)
        Button_2 = Button(Button_Frame, text='DISPLAY', font=(
            'Product Sans', 10, 'bold'), bg='deep sky blue2', fg='black',width=10, command=Display)
        Button_2.grid(row=0, column=1, padx=40)
        Button_3 = Button(Button_Frame, text='RESET', font=(
            'Product Sans', 10, 'bold'), bg='deep sky blue2',fg='black', width=10, command=Reset)
        Button_3.grid(row=0, column=2, padx=40)
        Button_4 = Button(Button_Frame, text='UPDATE', font=(
            'Product Sans', 10, 'bold'), bg='deep sky blue2',fg='black', width=10, command=Update)
        Button_4.grid(row=0, column=3, padx=40)
        Button_6 = Button(Button_Frame, text='DELETE', font=(
            'Product Sans', 10, 'bold'), bg='deep sky blue2',fg='black', width=10, command=Delete)
        Button_6.grid(row=0, column=5, padx=40)
        Button_7 = Button(Button_Frame, text='EXIT', font=(
            'Product Sans', 10, 'bold'), bg='deep sky blue2',fg='black',width=10, command=Exit)
        Button_7.grid(row=0, column=6, padx=40)


if __name__ == '__main__':
    root = Tk()
   # root.resizable(False,False)
    root.configure(bg='powderblue')
    root.title('Login Form')
    application = Portfolio(root)
    root.mainloop()