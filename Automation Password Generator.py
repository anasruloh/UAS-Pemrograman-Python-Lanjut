#mengimpor data perpustakaan yang diperlukan
from msilib.schema import CheckBox
import random
from tkinter import *
import string
import tkinter

#Source Code Untuk Tampilan Window
window = Tk()
window.title('Automation Password Generator')#Judul Window
window.geometry('500x300')#Ukuran Window

Label(window,font=('bold',10),text='PASSWORD GENERATOR').pack()#Label pada window

#function pada password  generator
def password_generate(leng):
    valid_char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_'#karakter pada password
    password=''.join(random.sample(valid_char,leng))#random generator pada password
    l =Label(window, text = password, font=('bold', 20)) #tampilan password
    l.place(x=190,y=50)
    Checkbutton(text='4 character',onvalue=4, offvalue=0,variable=len1).place(x=200,y=150)#tampilan untuk checkbox
    Checkbutton(text='6 character',onvalue=6, offvalue=0,variable=len2).place(x=200,y=170)#tampilan untuk checkbox
    Checkbutton(text='8 character',onvalue=8, offvalue=0,variable=len3).place(x=200,y=190)#tampilan untuk checkbox

#Mengubah input string menjadi integer
len1=tkinter.IntVar()
len2=tkinter.IntVar()
len3=tkinter.IntVar()

#function untuk tanda ceklist pada checkbox
def get_len():
  if len1.get() == 4:
     password_generate(4)
  elif len2.get() == 6:
     password_generate(6)
  elif len3.get() == 8:
     password_generate(8)
  else:
     password_generate(6)

Button(window,text='Generate',font=('normal',10), bg='yellow',command=get_len).place(x=200,y=100)

window.mainloop()#run aplikasi window