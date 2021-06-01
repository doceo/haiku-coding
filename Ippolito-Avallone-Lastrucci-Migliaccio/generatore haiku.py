#Lavoro a cura di: Avallone Enrico, Ippolito Gabriele, Lastrucci Davide.


#Per utilizzare il codice è necessario che tutti gli elementi scaricati siano presenti nella cartella "Downloads".
#("cinq1.txt"; "cinq2.txt"; "sette.txt"; "sfondo.jpg")


#librerie utilizzate

from random import randint as rd
import os
import csv
import tkinter as tk
from tkinter import *
from tkinter import font , messagebox
from PIL import Image, ImageTk
import time


#estraggo i versi dai file .txt

a = open("Downloads\cinq1.txt")
line = csv.reader(a)
v1 = list(line)

b = open("Downloads\sette.txt")
line = csv.reader(b)
v2 = list(line)

c = open("Downloads\cinq2.txt")
line = csv.reader(c)
v3 = list(line)


#configuro l'interfaccia

root = Tk()
riquadro = tk.Canvas(root, width = 600, height = 300, bg="dark sea green")
root.title("UN HAIKU AL GIORNO")
riquadro.pack()

load = Image.open("Downloads\sfondo.jpg")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
riquadro.create_window(300,150, window=img)   

riquadro2 = tk.Canvas(root, width = 250, height = 150, bg="antique white", highlightbackground="#1c1c1c", highlightthickness=4)
riquadro2.pack()
riquadro.create_window(300,140, window=riquadro2)


scritta1 = riquadro2.create_text(125,35, font= ("times", 14, "italic"))
scritta2 = riquadro2.create_text(125,75, font= ("times", 14, "italic"))
scritta3 = riquadro2.create_text(125,115, font= ("times", 14, "italic"))

lunghezza1 = len(v1)
lunghezza2 = len(v2)
lunghezza3 = len(v3)


#definisco le funzioni

def genera_haiku():
    
    verso1 = v1[rd(0,lunghezza1-1)]
    verso2 = v2[rd(0,lunghezza2-1)]
    verso3 = v3[rd(0,lunghezza3-1)]


    riquadro2.itemconfig(scritta1, text=str(*verso1))
    riquadro2.itemconfig(scritta2, text=str(*verso2))
    riquadro2.itemconfig(scritta3, text=str(*verso3))


def cambia_rigo1():
    verso1 = v1[rd(0,15)]
    riquadro2.itemconfig(scritta1, text=str(*verso1))


def cambia_rigo2():
    verso2 = v2[rd(0,16)]
    riquadro2.itemconfig(scritta2, text=str(*verso2))
    

def cambia_rigo3():
    verso3 = v3[rd(0,17)]
    riquadro2.itemconfig(scritta3, text=str(*verso3))


def cancella_haiku():
    riquadro2.itemconfig(scritta1, text="")
    riquadro2.itemconfig(scritta2, text="")
    riquadro2.itemconfig(scritta3, text="")


def istruzioni():
 messagebox.showinfo("Guida all'uso","Per generare un haiku casuale cliccare il bottone 'Genera Haiku'. Se si desidera sostituire solo un verso dell'Haiku cliccare il pulsante 'cambia' posto sulla sua sinistra.")

def autori():
 messagebox.showinfo("Autori","Avallone Enrico, Ippolito Gabriele, Lastrucci Davide")

def definizione():
 messagebox.showinfo("Definizione","L'Haiku è un breve componimento a carattere lirico, composto da 17 sillabe disposte in tre gruppi rispettivamente di 5, 7 e 5, tipico della tradizione poetica giapponese.")


#configuro i bottoni

button1 = tk.Button(root, text="  X  ", command=root.destroy, bg="gray64")
riquadro.create_window(580, 15, window=button1)

button2 = tk.Button(root, text="Genera Haiku", command=genera_haiku, font= ("monospace", 12, "bold"), bg= "azure3")
riquadro.create_window(300, 30, window=button2)


buttonr1 = tk.Button(root, text="cambia", command=cambia_rigo1, font= ("NavajoWhite2", 7), bg="azure3")
riquadro2.create_window(10, 35, window=buttonr1)

buttonr2 = tk.Button(root, text="cambia", command=cambia_rigo2, font= ("NavajoWhite2", 7), bg="azure3")
riquadro2.create_window(10, 75, window=buttonr2)

buttonr3 = tk.Button(root, text="cambia", command=cambia_rigo3, font= ("NavajoWhite2", 7), bg="azure3")
riquadro2.create_window(10, 115, window=buttonr3)


#configuro il menù a tendina

barrasuperiore= Menu(root)

tendina_info= Menu(barrasuperiore)
tendina_info.add_command(label="Guida all'uso", command=istruzioni)
tendina_info.add_command(label="Cos'è un Haiku?", command=definizione)
tendina_info.add_command(label="Autori", command=autori)


tendina_file= Menu(barrasuperiore)
tendina_file.add_command(label="genera", command=genera_haiku)
tendina_file.add_command(label="cancella", command=cancella_haiku)

barrasuperiore.add_cascade(label="Info", menu=tendina_info)
barrasuperiore.add_cascade(label="Edit", menu=tendina_file)

for x in range(33):
    barrasuperiore.add_separator() #separo la data dal resto (menù a tendina)

barrasuperiore.add_cascade(label= time.strftime("%x"))

root.config(menu=barrasuperiore)


#creo l'interfaccia

root.mainloop()