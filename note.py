import tkinter
from tkinter import *
import pymysql

root=Tk()
root.title("Note Taking App")


db=pymysql.connect("localhost",'root','keshav@123','keshav')
cursor=db.cursor()


def add():
    add_root=Tk()
    list=[]


    def update():
        for i in list:
            mylist.insert("end",i)


    def save():
        sub = entry.get("1.0", END)
        notes = save_text.get("1.0", END)
        cursor.execute("insert values('" + sub+ "','" + notes + "');")
        db.commit()
        list.append(sub)
        update()


    label = Label(add_root, text="WRITE SOMETHING HERE", font="bold 15")
    label.place(x=20,y=10)
    entry=Text(add_root,height="2",width="45")
    entry.place(x=20,y=45)
    save_text=Text(add_root,height="30",width="60")
    save_text.place(x=20,y=90)
    save_button = Button(add_root, text="Add", font="bold 13", bg="#FF00FF", fg="white", command=save)
    save_button.place(x=390, y=45)
    add_root.minsize(600,600)



def show_all():
    show_root=Tk()
    show_root.minsize(600,600)
    qr=cursor.execute("select subject from keshav;")
    a=cursor.fetchall()
    for i in a:
        for j in i:
           
            print(j)



def search_notes():
    qr=cursor.execute("select subject from keshav")
    get_subject=cursor.fetchall()
    for i in range(len(get_subject)):
        list.append(get_subject[i][0])
    srch=search_entry.get("1.0",END)
    for subs in list:
        if srch==subs:
            fetchdata(notes)
            break


add_button=Button(root,text="Add New Note>>",font="bold 15",bg="red",fg="white",command=add)
add_button.place(x=20,y=20)


list_all_notes_button=Button(root,text="List All Notes>>",font="bold 15",bg="red",fg="white",command=show_all)
list_all_notes_button.place(x=300,y=20)


label=Label(root,text="Search Notes",font="bold 20")
label.place(x=20,y=70)


search_entry = Text(root,width=45,height="2")
search_entry.place(x=20,y=120)


search_button=Button(root,text="Search",font="bold 13",bg="red",fg="white",command=search_notes)
search_button.place(x=400,y=120)


label=Label(root,text="--Notes--",font="bold 20")
label.place(x=20,y=160)


scrollbar=Scrollbar(root,orient="vertical")
scrollbar.place(x=532,y=200,height=370)


mylist=Listbox(root,height="23",width="85",yscrollcommand=scrollbar.set)
mylist.place(x=20,y=200)



scrollbar.config(command=mylist.yview)


root.geometry("550x600")
root.config(bg='#C6E2FF')
root.resizable(False,False)
root.maxsize(600,600)
root.minsize(500,500)
root.mainloop()

