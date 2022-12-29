#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import os
import tkinter.messagebox as tmsg
from tkinter.filedialog import asksaveasfilename,askopenfilename

root=Tk()
root.geometry("500x500")
root.title("Untitled -Notepad")
root.iconbitmap("notepad_icon_129398.ico")


def newfile():
    global file
    root.title("Untitled -Notepad")
    file=None
    textarea.delete(1.0,END)
    


def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
        
    else:
        root.title(os.path.basename(file)+" -Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
        
def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" -Notepad")
            
            
    else:
        
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file)+" -Notepad")
        
        
def quit():
    root.destroy()


def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))



def paste():
    textarea.event_generate(("<<Paste>>"))


def about():
    tmsg.showinfo("about...","designed by utsav")



textarea=Text(root,font=("lucida 13"))
textarea.pack(fill=BOTH,expand=True)
scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)


file=None



MenuBar=Menu(root)
filemenu=Menu(MenuBar,tearoff=0)
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="open",command=openfile)
filemenu.add_command(label="save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)
MenuBar.add_cascade(label="file",menu=filemenu)
root.config(menu=MenuBar)



editmenu=Menu(MenuBar,tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
MenuBar.add_cascade(label="Edit",menu=editmenu)


helpmenu=Menu(MenuBar,tearoff=0)
helpmenu.add_command(label="About",command=about)
MenuBar.add_cascade(label="Help",menu=helpmenu)


root.config(menu=MenuBar)


root.mainloop()


# In[ ]:




