import tkinter
from tkinter import *
def display():
	root=Tk()
	b=Button(root,text='keshav',width=34,height=30,bg='green')
	b.place(x=23,y=67)
		
root=Tk()
b=Button(root,text='ADD NEW NOTES>>',fg='white',bg='red',width=30,height=2,command=display)
b.place(x=23,y=30)

b1=Button(root,text='LIST ALL NOTES',fg='white',bg='red',width=30,height=2)
b1.place(x=260,y=30)

label=Label(root,text='SEARCH NOTES',width=25,height=2,bg='#C6E2FF')
label.place(x=23,y=100)

entry=Entry(root,text='ggrtg',width=52)
entry.place(x=23,y=140)

b2=Button(root,text='search',width=15)
b2.place(x=340,y=137)

keshav=Label(root,text='---NOTES---',width=25,height=2,bg='#C6E2FF')
keshav.place(x=80,y=165)

listbox=Listbox(root,width=82,height=18)
listbox.place(x=0,y=200)
s=Scrollbar(root)
s.pack(side='right',fill='y')



root.title("keshav app")
root.config(bg='#C6E2FF')
root.geometry("500x500")
root.resizable(TRUE,TRUE)
root.mainloop()