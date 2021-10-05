# step:-1
from tkinter import*
from PIL import Image,ImageTk
import json
from difflib import get_close_matches

#step:-3
data_load=json.load(open(r"C:\Users\dell\Desktop\myproject\ATM\dictionary.json"))
def search_word(word):
    if word in data_load:
      meaning_word.delete(1.0,END)
      meaning_word.config(fg='white')
      meaning_word.insert(END,data_load[word])

    elif len(get_close_matches(word,data_load.keys()))>0:
        meaning_word.config(fg='red')
        meaning_word.delete(1.0,END)
        meaning_word.insert(END,'where you finding{} and meaning is:{}'.format(get_close_matches(word,data_load.keys())[0],
                                                data_load[get_close_matches(word,data_load.keys())[0]]))
        final=get_close_matches(word,data_load.keys())

#step:-2
root=Tk()
root.title("My Dictinary App")

image=Image.open(r"C:\Users\dell\Desktop\myproject\ATM\avengers.jpg")
Image_picture=ImageTk.PhotoImage(image)
dest_pic=Label(root,image=Image_picture)
dest_pic.pack()

a=StringVar()
word_1=Entry(root,textvariable=a,background='blue',fg='white',font=('arial',40,'bold'))
word_1.place(relx=.18,rely=0.70,relheight=0.0750,relwidth=0.60)

button_1=Button(root,text="search the word",command=lambda:search_word(a.get()),background="red",fg="white",font=('arial',40,'bold'))
button_1.place(relx=.18,rely=0.85,relheight=0.0750,relwidth=0.60)

meaning_word=Text(root,background='red',fg='white',font=('arial',15,'bold'))
meaning_word.place(relx=.18,rely=0.100,relheight=0.100,relwidth=0.70)

root.mainloop()