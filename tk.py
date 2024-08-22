import tkinter as tk
from tkinter import *
from tkinter import ttk

root=tk.Tk()
root.configure(background="#41175F")
root.title("To-Do-List")
root.geometry("700x500")


#Logic
def addTaskFun():
    nt=new_task.get()
    if nt:
        list.insert(tk.END,nt)
        new_task.set("")

def deleteTaskFun():
    selected_index=list.curselection()
    list.delete(selected_index)
    list.selection_clear(0, tk.END)

def finishedTask():
    selected_index=list.curselection()
    item=list.get(selected_index) 
    list.delete(selected_index)       
    list.insert(selected_index, item+"  ✓" ) 
 


new_task= tk.StringVar()

# Elements
listLabel=tk.Label(root,text="Your Tasks",fg="#41175F",font=("Helvetica", 16))
listLabel.place(x=100,y=10)
list=tk.Listbox(root,bg="white",height=15,width=30,bd=5,font=("Helvetica", 12))
list.place(x=15,y=55)

addtaskLabel=tk.Label(root,text="Add Task :",bg="#41175F",fg="white",font=("Helvetica", 15)).place(x=420,y=20)
add_task=tk.Entry(root,textvariable=new_task,bd=3,font=("Helvetica",12)).place(x=400,y=60)
addButton=tk.Button(root,text="Add",width=15,command=addTaskFun).place(x=420,y=100)

deletetaskLabel=tk.Label(root,text="Delete Task :",bg="#41175F",fg="white",font=("Helvetica", 15)).place(x=420,y=180)
deleteButton=tk.Button(root,text="Delete",width=15,command=deleteTaskFun).place(x=420,y=220)

finishButton=tk.Button(root,text="Mark as finished",width=20,command=finishedTask).place(x=420,y=300)


root.mainloop()

