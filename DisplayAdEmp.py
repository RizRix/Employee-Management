from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from subprocess import call
from tkinter import ttk

import pymysql

x = pymysql.connect(host='localhost',
                    user='root',
                    password='dream2021',
                    db='avodha')
cr = x.cursor()

t = Tk()
t.title("R!Z Employee")
t.geometry("1000x500")

p = Image.open("/Users/rizwanaabdulsalam/Downloads/emp.jpeg")
p = p.resize((1000, 1500))
p = ImageTk.PhotoImage(p)
pic = Label(t, image=p)
pic.place(x=0, y=0)

def r():
    tree_frame = Frame(t)
    tree_frame.place(x=380, y=120, width=600, height=350)
    trv = ttk.Treeview(tree_frame)
# trv.place(x=380, y=120, width=600, height=350)

    trv.grid(row=1, column=1, padx=8, pady=8)
# number of columns

    trv["columns"] = ("1", "2", "3", "4", "5", "6", "7")

# Defining heading
    trv['show'] = 'headings'

# width of columns and alignment
    trv.column("1", width=90, anchor='c')
    trv.column("2", width=80, anchor='c')
    trv.column("3", width=80, anchor='c')
    trv.column("4", width=80, anchor='c')
    trv.column("5", width=80, anchor='c')
    trv.column("6", width=80, anchor='c')



# Headings
# respective columns
    trv.heading("1", text="Name")
    trv.heading("2", text="Age")
    trv.heading("3", text="D.O.B")
    trv.heading("4", text="Email")
    trv.heading("5", text="Gender")
    trv.heading("6", text="Address")
    trv.heading("7", text="Contact")



# getting data from MySQL student table
    cr.execute('select * from eemp')
    for dt in cr:
        trv.insert("", 'end',text=dt[0],values=(dt[0], dt[1], dt[2], dt[3], dt[4], dt[5], dt[6]))

r()
Label(text='Riz Employee', bg="black", fg="white").place(x=380, y=20)

Label(text='Name:', bg="black", fg="white").place(x=40, y=120)
nm = Entry()
nm.place(x=100, y=120)

Label(text='Age:', bg="black", fg="white").place(x=40, y=160)
ag = Entry()
ag.place(x=100, y=160)

Label(text='DOB:', bg="black", fg="white").place(x=40, y=200)
db = Entry()
db.place(x=100, y=200)

Label(text='Email:', bg="black", fg="white").place(x=40, y=240)
em = Entry()
em.place(x=100, y=240)

Label(text='Gender:', bg="black", fg="white").place(x=40, y=280)
cb = ttk.Combobox()
cb['values'] = ("Male", "Female")
cb.current()
cb.place(x=100, y=280)

Label(text='Address:', bg="black", fg="white").place(x=40, y=320)
sd = Entry()
sd.place(x=100, y=320)

Label(text='Contact:', bg="black", fg="white").place(x=40, y=380)
ct = Entry()
ct.place(x=100, y=380)


def abcd():
    n = nm.get()
    a = ag.get()
    d = db.get()
    e = em.get()
    c = cb.get()
    s = sd.get()
    t = ct.get()

    cr.execute("insert into eemp values(%s,%s,%s,%s,%s,%s,%s)", (n, a, d, e, c, s, t))

    x.commit()
    tkinter.messagebox.showinfo("SUCCESSFULL!", "INSERTED")

    # call(['python', 'nxt.py'])


Button(text="Submit", command=abcd, bg="black", fg="black").place(x=120, y=440)




Button(text="Refresh", command=r, bg="black", fg="black").place(x=180, y=440)

t.mainloop()
