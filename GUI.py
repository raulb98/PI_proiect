from tkinter import *
from tkinter import filedialog
import subprocess
from functools import partial
from PIL import Image,ImageTk

root = Tk()
root.geometry("500x500+450+150")

def Crypt_process():
    msg_to_crypt=entry_1.get()
    subprocess.call([r'C:\Users\rbucur\source\repos\Pi_Proiect_Criptare\x64\Debug\Pi_Proiect_Criptare.exe',msg_to_crypt,img_path])

def Decrypt_process():
    entry_2.delete(0,'end')
    msg_to_get = subprocess.run([r'C:\Users\rbucur\source\repos\Pi_Proiect_Decrypt\x64\Debug\Pi_Proiect_Decrypt.exe'],capture_output=True)
    entry_2.insert(0,msg_to_get.stdout)

def Browse_picture():
    root.filename = filedialog.askopenfilename(initialdir="D:/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    global img_path
    img_path = root.filename
    load = Image.open(root.filename)
    load = load.resize((250,250),Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    image = Label(root,image=render)
    image.image = render
    image.grid(row=4,column=0,columnspan=2,rowspan=2)

message_to_crypt=StringVar()
label1 = Label(root, text="Criptare: ")
entry_1 = Entry(root,textvariable=message_to_crypt)


label2 = Label(root, text="Decriptare: ")
entry_2 = Entry(root)

cryptButton = Button(root, text="Crypting", fg="black",command=Crypt_process)
decryptButton = Button(root, text="Decrypting", fg="black",command=Decrypt_process)
pathButton = Button(root,text="Path to file", fg="black",command=Browse_picture)
decryptButton.grid(row=1,sticky=W)
cryptButton.grid(row=0,sticky=W)
pathButton.grid(row=2,sticky=W)
entry_1.grid(row=0, column=1, sticky=W)
entry_2.grid(row=1, column=1, sticky=W)

root.mainloop()
