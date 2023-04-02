
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import os

window = Tk()
window.title('My IDE')
window.geometry("1280x720+150+80")
window.configure(bg="#0E5E6F")
window.resizable(False,False)

file_path=''

def set_file_path(path):
    global file_path
    file_path=path

def openFile():
    path=askopenfilename(filetypes=[('Python files','*.py')])
    with open(path,'r') as file:
        code=file.read()
        input.delete('1.0', END)
        input.insert('1.0', code)
        set_file_path(path)

def save():
    if file_path=='':
        path=asksaveasfilename(filetypes=[('Python files','*.py')])
    else:
        path=file_path

    with open(path, 'w') as file:
        code=input.get('1.0',END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path=='':
        messagebox.showerror("My IDE", "Save your code!")
        return
    command=f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=TRUE)
    output , error = process.communicate()
    codeoutput.insert('1.0', output)
    codeoutput.insert('1.0', error)
#icon of the IDE
icon=PhotoImage(file="logo.png")
window.iconphoto(False,icon)

#code input
input=Text(window,font="consolas 18")
input.place(x=180,y=0,width=680,height=720)

#code output
codeoutput=Text(window,font="consolas 15",bg="#50577A",fg="#DEF5E5")
codeoutput.place(x=860,y=0,width=420,height=720)

#buttons
Open=PhotoImage(file="open.png")
Save=PhotoImage(file="save.png")
Run=PhotoImage(file="run.png")

Button(window, image=Open,bg="#BCEAD5", bd=5,command=openFile).place(x=30,y=30)
Button(window, image=Save,bg="#BCEAD5", bd=5,command=save).place(x=30,y=145)
Button(window, image=Run,bg="#BCEAD5", bd=5,command=run).place(x=30,y=260)


window.mainloop()