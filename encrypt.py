from cryptography import fernet
from tkinter import *
import json

def makekey():
   # set_text(fernet.Fernet.generate_key())
    set_text(fernet.Fernet.generate_key(), inkey)

def decrypt():
    key= inkey.get()
    f= fernet.Fernet(key)
    with open("/Users/ericwang/Desktop/shit/PasswordMonkey/testpasswords.txt", "rb") as file:
        file_data = file.read()
        data=f.decrypt(file_data)
    j=json.loads(data)
    set_text(j[inwebsite.get()], inpassword)

def decryptencrypt():
    key= inkey.get()
    f= fernet.Fernet(key)
    with open("/Users/ericwang/Desktop/shit/PasswordMonkey/testpasswords.txt", "rb") as file:
        file_data = file.read() 
    if file_data == b'': 
        data={inwebsite.get():inpassword.get()} 
    else: 
        data = json.loads(f.decrypt(file_data))
        data[inwebsite.get()]= inpassword.get()
    encrypted= f.encrypt(json.dumps(data).encode())
    with open('/Users/ericwang/Desktop/shit/PasswordMonkey/testpasswords.txt','wb') as f:
        f.write(encrypted)

def set_text(text, entry):
    entry.delete(0,END)
    entry.insert(0,text)
    return

win=Tk()
Label(win, text="Key").grid(row=0)
Label(win, text="Website link").grid(row=1)
Label(win, text="Password").grid(row=2)


inwebsite= Entry(win, width= 40)
inpassword= Entry(win, width = 40)
inkey= Entry(win, width = 40)

inwebsite.grid(row=1, column=1)
inpassword.grid(row=2, column=1)
inkey.grid(row=0, column=1)

getKey= Button(win, text="Get a random key", command=makekey)
newinput= Button(win, text="Encrypt New Login", command=decryptencrypt)
getPassword= Button(win, text="Get Password", command=decrypt)
getPassword.grid(row=3, column=1)
newinput.grid(row=4, column=1)
getKey.grid(row=5, column=1)

win.minsize(400, 400)
win.title("Password Monke")
win.mainloop()
