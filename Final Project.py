from tkinter import *
from tkinter import filedialog
from random import *
from tkinter import messagebox
import os
from PIL import Image,ImageTk


p=0
q=0
path0=""
path1=""
path2=""
public=0


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = e
    ob = phi
    while phi != 0:
        q = e // phi
        (e, phi) = (phi, e % phi)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob
    if ly < 0:
        ly += oa
    return lx


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = randint(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e , n), (d , n))


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)


def ran():
    p = randint(0, 1000)
    q =  randint(0, 1000)
    if ((is_prime(p) and is_prime(q)) and  p!=q):
        return p,q
    else:
        return ran()


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def performencryption():

    if(path0==""):
        messagebox.showinfo("Note", "Please Load Your File")
    else:
        global p, q, public
        p, q = ran()
        file = open(path0)
        data = file.read()
        file.close()

        public,private=generate_keypair(p,q)

        d=[]
        for i in public:
            d.append(str(i))

        key ="|".join(map(lambda x: str(x), d))

        encrypted_message=encrypt(private,data)

        strmesage="|".join(map(lambda x: str(x), encrypted_message))

        file=open(path0,"w+")
        file.write(strmesage)
        file.close()

        p=path0
        name1=p.split("/")
        name2=name1[-1]
        fullname="Key Of File "+name2

        file1=open((fullname),"w+")
        file1.write(key)
        file1.close()

        messagebox.showinfo("Key", "Your Key For Decryption Is Stored\n In File Name \" "+fullname+" \"")
        messagebox.showinfo("Note","    Congratulations\nYour File Is Encrypted")
        os.startfile(path0)


def performdecryption():
    if (path1 == "" or path2==""):
        messagebox.showinfo("Note", "Please Load Your File And Key")
    else:
        file=open(path1)
        message=file.read()
        file.close()

        file1=open(path2)
        key=file1.read()
        file1.close()

        lkey=key.split("|")
        d=[]
        for i in range(0,len(lkey)):
            d.append(int(lkey[i]))

        tkey=tuple(d)

        lmesage=message.split("|")
        d1=[]
        for i in range(0,len(lmesage)):
            d1.append(int(lmesage[i]))

        decrypted_message=decrypt(tkey, d1)

        file2=open(path1,"w+")
        file2.write(decrypted_message)
        file2.close()

        messagebox.showinfo("Note", "    Congratulations\nYour File Is Decrypted")
        os.remove(path2)
        os.startfile(path1)



def dialogboxappear1():
    filename=filedialog.askopenfilename(filetypes=(("File","*.txt"),("All Files","*.txt*")))
    global path0
    if(filename!=""):
        path0 = filename
        os.startfile(filename)

def dialogboxappear2():
    filename=filedialog.askopenfilename(filetypes=(("File","*.txt"),("All Files","*.txt*")))
    global path1
    if (filename != ""):
        path1 = filename
        messagebox.showinfo("Note", " Your File Is Loded")

def dialogboxappear3():
    filename=filedialog.askopenfilename(filetypes=(("File","*.txt"),("All Files","*.txt*")))
    global path2
    if(filename!=""):
        path2 = filename
        messagebox.showinfo("Note", " Your Key Is Loded")


def encryption():
    global frame
    frame=Frame(frame1,width=260,height=350,bg="black")
    frame.pack()
    back=Button(frame,text="Back",width=10,font="none 13 bold",bg="Black",fg="orange",command=backmenu)
    back.place(x=80,y=150)
    b1=Button(frame,text="Open File",width=15,font="none 13 bold",bg="Black",fg="orange",command=dialogboxappear1)
    b1.pack()
    b1.place(x=50,y=200)
    b2=Button(frame,text="Encrypt File",width=18,font="none 14 bold",bg="Black",fg="orange",command=performencryption)
    b2.pack()
    b2.place(x=19,y=250)
    l=Label(frame,text="Encryption",font="none 28 bold",bg="black",fg="orange")
    l.pack()
    l.place(x=30,y=60)




def decryption():
    global frame
    frame= Frame(frame1,width=260,height=350,bg="black")
    frame.pack()
    back=Button(frame,text="Back",width=10,font="none 13 bold",bg="Black",fg="orange",command=backmenu)
    back.place(x=19,y=130)
    b1=Button(frame,text="Open File",width=15,font="none 13 bold",bg="Black",fg="orange",command=dialogboxappear2)
    b1.pack()
    b1.place(x=80,y=170)
    b2 = Button(frame, text="Load Key", width=15, font="none 13 bold", bg="Black", fg="orange",command=dialogboxappear3)
    b2.pack()
    b2.place(x=19, y=210)
    b3 = Button(frame, text="Decrypt File", width=18, font="none 14 bold", bg="Black", fg="orange",command=performdecryption)
    b3.pack()
    b3.place(x=19, y=260)
    l = Label(frame, text="Decryption", font="none 28 bold", bg="black", fg="orange")
    l.pack()
    l.place(x=30, y=50)


def backmenu():
    global path0
    global path1
    global path2
    path0=""
    path1=""
    path2=""
    global frame1
    frame1 = Frame(frame, width=260, height=350, bg="black")
    frame1.pack()
    label1 = Label(frame1, text="Welcome", font="none 24 bold", bg="black", fg="orange")
    label1.pack()
    label1.place(x=55, y=60)
    label2 = Label(frame1, text="To", font="none 24 bold", bg="black", fg="orange")
    label2.pack()
    label2.place(x=110, y=105)
    label3 = Label(frame1, text="Cryptography", font="none 24 bold", bg="black", fg="orange")
    label3.pack()
    label3.place(x=22, y=145)
    button1 = Button(frame1, text="Encryption", width=18, font="none 14 bold", bg="Black", fg="orange",
                     command=encryption)
    button1.pack()
    button1.place(x=19, y=230)
    button2 = Button(frame1, text="Decryption", width=18, font="none 14 bold", bg="Black", fg="orange",
                     command=decryption)
    button2.pack()
    button2.place(x=19, y=285)



root=Tk()
root.title("Cryptography")

root.maxsize(width=700,height=390)
root.minsize(width=700,height=390)
root.configure(bg="Black")

photo=ImageTk.PhotoImage(file="1.jpg")
label=Label(image=photo)
label.pack()

frame1=Frame(label,width=260,height=350,bg="Black")
frame1.pack()
frame1.place(x=20,y=20)

label1=Label(frame1,text="Welcome",font="none 24 bold",bg="black",fg="orange")
label1.pack()
label1.place(x=55,y=60)
label2=Label(frame1,text="To",font="none 24 bold",bg="black",fg="orange")
label2.pack()
label2.place(x=110,y=105)
label3=Label(frame1,text="Cryptography",font="none 24 bold",bg="black",fg="orange")
label3.pack()
label3.place(x=22,y=145)
button1=Button(frame1,text="Encryption",width=18,font="none 14 bold",bg="Black",fg="orange",command=encryption)
button1.pack()
button1.place(x=19,y=230)
button2=Button(frame1,text="Decryption",width=18,font="none 14 bold",bg="Black",fg="orange",command=decryption)
button2.pack()
button2.place(x=19,y=285)
root.mainloop()