#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list 


from tkinter import *

def show():
    k = l.get(ACTIVE)
    v = d[k]

    l1.config(text=k)
    l2.config(text=v)

d = {'keshav':1234, 'yash':3214, 'vibhor':3453, 'gurry':1278, 'pagal':7832}
root = Tk()

l = Listbox(root)
l.pack(side=LEFT, fill=Y)


for k in d.keys():
    l.insert(END,k)

s = Scrollbar(root, command = l.yview)
s.pack(side=RIGHT, fill=Y)
l.config( yscrollcommand=s.set)

l1 = Label(root, text='name')
l1.pack()




#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.

from tkinter import *

def show():
    k = l.get(ACTIVE)
    v = d[k]

    l1.config(text=k)
    l2.config(text=v)

def insert():
    k = e1.get()
    v = e2.get()

    d[k] = v

    l.insert(END,k)
    print(d)

d = {'keshav':7123, 'vibhor':5321, 'gurry':3455, 'pagal':1872, 'rana':3762}
root = Tk()

l = Listbox(root)
l.pack(side=LEFT, fill=Y)


for k in d.keys():
    l.insert(END,k)

s = Scrollbar(root, command = l.yview)
s.pack(side=RIGHT, fill=Y)
l.config( yscrollcommand=s.set)

l1 = Label(root, text='name')
l1.pack()
l2 = Label(root, text='number')
l2.pack()

b1 = Button(root, text="show", command=show)
b1.pack()

e1 = Entry(root)
e1.pack()
e2 = Entry(root)
e2.pack()

b2 = Button(root, text="Insert!", command=insert)
b2.pack()
root.mainloop()