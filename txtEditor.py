from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

filename = None
#sets up blank txt file
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

#saves the files current status
def saveFile():
    global filename
    if filename is None:
        saveAs()
    else:
        t = text.get(0.0, END) #stores the text
        try:
            with open(filename, 'w') as f:#opens the file with the filename stored in the global variable
                f.write(t)
        except Exception as e:
            showerror(title="Error", message=f"Unable to save file: {e}")

#allows the user to save the file to any destination and set its name
def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t= text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Nu Uh", message="Unable to save file... uh oh")

#opens file explorer and allows user to open any
def openFile():
    try:
        global filename
        file = askopenfile(mode='r')
        if file:
            filename = file.name  # Set the global filename variable
            t = file.read()
            text.delete(0.0, END)
            text.insert(0.0, t)
    except:
        showerror(title="Unable to read file", message="Unable to read file, must be plain text file.")
        return

 


#creates text window, max and min are set like that to stop users from minimising and increasing window size    
root = Tk()
root.title("Text Editor")
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)

text = Text(root, width=400, height=400)
text.pack()

#this section adds all the methods to the top of the screen
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()


