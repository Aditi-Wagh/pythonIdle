# pythonIdle
Problem Statement: 
To create a python IDLE (Integrated Development and Learning Environment) which is used to create, modify, and run python programs. 
Keyword: 
IDLE stands for Integrated Development and Learning Environment.It provides a comprehensive text editor for creating a python script and running it. 
Abstract:
In ‘My IDLE’ one can create a new python project and write the code producing appropriate output. The created code can be saved on chosen location.A previously created project can also be opened and run, irrespective of any operating system. 
Module used: 
1) TKINTER MODULE 
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. 
2) MESSAGE BOX MODULE 
tkMessageBox 
The tkMessageBox module is used to display message boxes in your applications. This module provides a number of functions that you can use to display an appropriate message. 
Syntax: 
tkMessageBox.FunctionName(title, message [, options]) 
The following functions are available with the dialogue box − 
● showinfo() 
● showwarning() 
● showerror () 
● askquestion() 
● askokcancel() 
● askyesno () 
● askretrycancel ()
Parameters: 
FunctionName − This is the name of the appropriate message box function. 
● title − This is the text to be displayed in the title bar of a message box. ● message − This is the text to be displayed as a message. 
● options − options are alternative choices that you may use to tailor a standard message box. Some of the options that you can use are default and parent. The default option is used to specify the default button, such as ABORT, RETRY, or IGNORE in the message box. The parent option is used to specify the window on top of which the message box is to be displayed. 
3)FILEDIALOG MODULE 
The Python Tkinter filedialog module offers you a set of unique dialogs to be used when dealing with files,specifically designed for file selection. This module is similar to “file handling in a real operating system”. 
● parent – The Window on to which the dialog is to be placed 
● title – The name that appears on the dialog 
● initialdir – The directory the dialog first opens up in. 
● initialfile – The file that the dialog has selected when it is opened. 
● filetypes – Determines that type of the files to be loaded/saved in the dialogs. Passed as a tuple in a (Label, Filetype) format. You may also use the * wild card which applies to all file types. You can pass multiple tuples as well for multiple options. 
● defaultextension – Default extension to be applied to files when appending to them. (Only applies to save dialogs) 
● multiple – When true, it allows the selection of multiple items 
Opening a File:
askopenfilename(s) - Once you select a file, it’s file path will be returned back into your python program for you to use. 
Saving a File: 
The asksaveasfile function is used to save a file in a specified location. 
Selecting a Directory: 
This function is just like the askopenfilename function, except that it’s not used to select files, rather it selects directories (folders) and returns their file path. 
4) SUBPROCESS MODULE 
The subprocess module present in Python(both 2.x and 3.x) is used to run new applications or programs through Python code by creating new processes. It also helps to obtain the input/output/error pipes as well as the exit codes of various commands. 
In other words, you can start applications and pass arguments to them using the subprocess module. 
5)OPERATING MODULE 
The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system. 
It is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
Technology Selected and Technology features covered 
Tkinter is a standard library in python used for creating Graphical User Interface (GUI) for Desktop Applications. 
Generally, an IDLE, is a very simple and sophisticated IDE developed primarily for beginners, and because of its simplicity, it is highly considered and recommended for educational purposes. It offers a variety of features that you will look in detail along with examples later in this tutorial.Some of the key features it offers are: 
● GUI development portability and flexibility of Tk makes it the right tool which can be used to design and implement a wide variety of commercial-quality GUI applications. ● Python with Tkinter provides us a faster and efficient way in order to build useful applications 
1. Error Checking 
2. Providing Runtime Environment 
3. Saving the write program 
4. Opening and running an already saved program 
Salient Feature:- 
1. Open Button:On clicking this button we can open our previous python files on location chosen on our computer with help of filedialog module . 
Save Button:On clicking this button we can save our current python file on location chosen on our computer with help of filedialog module .If we try to run the program without saving it,then a dialog box appears prompting the user to save it.It is possible with the help of tkMessageBox. 
Run Button:On clicking this button we can run our python program.It is implemented with the help of subprocess module.
References : 
1. Murach's Python Programming - Murach J. ; Urban M. 2. Python GUI Programming Cookbook - Meier B.A.
