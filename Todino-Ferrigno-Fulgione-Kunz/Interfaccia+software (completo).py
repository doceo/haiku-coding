import json
from json import load
from random import choice
from tkinter import Tk, Label, Button
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
class App:
    
    def __init__(self, master):
        self.master = master
        self.master.geometry("320x250")
        self.master.title("Un Haiku al giorno")
        image2 = Image.open("C:\\Users\\Todino Family\\Desktop\\haiku\\mac.jpg")
        image1 = ImageTk.PhotoImage(image2)
        background_label = Label(master, image=image1, background ="white")
        background_label.image1=image1
        background_label.place(x=0, y=0, height=300, width=340)

        self.haiku_button = Button(self.master, text="Genera", command=self.software, background ="white" )
        self.haiku_button.pack()
        self.haiku_button.config(font=("Algerian", 20), justify="center", width=9)
        self.haiku_button.place(x=80, y=0)
        
        self.haiku1 = Label(self.master, text="")
        self.haiku1.pack()
        self.haiku1.config(font=("Algerian", 7), justify="center", background ="white")
        self.haiku1.place(x=104,y=95)

        self.haiku2 = Label(self.master, text="")
        self.haiku2.pack()
        self.haiku2.config(font=("Algerian", 7), justify="center", background ="white")
        self.haiku2.place(x=104,y=115)

        self.haiku3 = Label(self.master, text="")
        self.haiku3.pack()
        self.haiku3.config(font=("Algerian", 7), justify="center", background ="white")
        self.haiku3.place(x=104,y=135)

    
    def software(self):
        with open("bello.json", "r") as outfile:
            self.haiku1["text"], self.haiku2["text"], self.haiku3["text"] = [str(choice(i)) for i in load(outfile).values()]

if __name__ == "__main__":
    root = Tk()
    my_gui = App(root)
    root.mainloop()
