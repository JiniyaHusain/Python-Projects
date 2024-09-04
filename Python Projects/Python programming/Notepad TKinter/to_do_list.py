from tkinter import *
from PIL import Image,ImageTk
root =Tk()

#root
root.geometry("400x600")
root.title("To Do List")
root.resizable(False,False)

task_list=[]

def addtask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt","a")as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task) 

def deletetask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
    with open("tasklist.txt","w")as taskfile:
        for task in task_list:
            taskfile.write(task+"\n")
    listbox.delete(ANCHOR)                 

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r")as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task!='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt',"w")
        file.close()

#icon
image_icon=PhotoImage(file="icon_todo.png")
root.iconphoto(False,image_icon)

#TOP BAR:

#bar
topimage=PhotoImage(file="topbarr.png")
Label(root,image=topimage).pack()

#icon
noteimage=Image.open("icon_todo.png")
newnoteimage=noteimage.resize((45,45),Image.Resampling.LANCZOS)
notephoto=ImageTk.PhotoImage(newnoteimage)
Label(root,image=notephoto,bg="#32405b").place(x=30,y=20)

#heading
Label(root,text="TO DO LIST",fg="white",bg="#32405b",font="arial 20 bold").place(x=120,y=25)

#MAIN:

#frame
f1=Frame(root,bg="white",width=400,height=50,relief="sunken")
f1.place(x=0,y=180)

#frame entry
task=StringVar()
task_entry=Entry(f1,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

#add
b1=Button(f1,text="Add",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addtask)
b1.place(x="300",y="0")

#list box & scrollbar
f2=Frame(root,bd=3,width=700,height=280,bg="#32405b")
f2.pack(pady=(160,0))

listbox=Listbox(f2,font="arial 12",width=40,height=16,bg="#32405b",fg="#fff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar=Scrollbar(f2)
scrollbar.pack(side=LEFT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
deleteimage=Image.open("delete_todo.png")
newdeleteimage=deleteimage.resize((45,45),Image.Resampling.LANCZOS)
deletephoto=ImageTk.PhotoImage(newdeleteimage)
Button(root,image=deletephoto,bg="#32405b",command=deletetask).pack(side=BOTTOM,pady=1)

root.mainloop()