#GRUPPO: FERRANTE, RUSSO, BARRA
import os.path as path
from haiku import extractor
from tkinter import *

from tkinter.filedialog import askopenfilename, asksaveasfilename

#PERCORSO DEL FILE
running_file = path.basename(__file__)
file_dir = __file__.replace(running_file, '')
data_path = file_dir + 'versi.csv'

#FUNZIONI
def genera(): #FUNZIONE GENERATRICE

    

    estratti = [
        extractor(data_path)[0],
        extractor(data_path)[1],
        extractor(data_path)[2]
        ]

    for i in estratti:
        indice = estratti.index(i)
        if i == None or i == '':
            print(estratti)
            estratti[indice] = extractor(data_path)[indice]

    verso1.config(text=estratti[0])
    verso2.config(text=estratti[1])
    verso3.config(text=estratti[2])

def istruzioni(): #FINESTRA DI ISTRUZIONI
    window = Toplevel(root)
    window.geometry('1000x700')
    window.config(background='#fbebd0')

    titolo = Label(window, text='Istruzioni', font=('Georgia', 36))
    titolo.config(background='#fbebd0')
    titolo.pack()

    testo = Label(window, font=('Verdana', 16),
        text='''Premere il pulsante "Genera" per generare un haiku a caso;

        Premere "Salva" per salvare l\'haiku in un file di testo .txt;
        
        Premere "Carica" per caricare un file .csv dal quale recuperare i versi.
        Di base sarà caricato un file versi.csv nella stessa cartella del file eseguito .py;
        
        Premere "Chiudi per chiudere il generatore."''')

    testo.config(background='#fbebd0')
    testo.pack()
    window.mainloop()

def carica(): #CARICA FILE .CSV ALTERNATIVO
    global data_path
    data_path = askopenfilename(filetypes=[('File CSV', '*.csv')])
    genera()

def salva(): #SALVA HAIKU IN UN FILE .TXT
    directory = asksaveasfilename(filetypes=[('File di testo TXT', '*.txt')], initialfile='text.txt')
    with open(directory, 'w') as f:
        f.write(verso1['text'] + '\n' + verso2['text'] + '\n' + verso3['text'])




#FINESTRA PRINCIPALE



root = Tk()
root.title('Basho: un haiku al giorno')
root.state('zoomed')
root.iconbitmap('icona.ico')
root.geometry('1024x576')

titolo = Label(root, text='Basho: un haiku al giorno', font=('Georgia', 48)) #TITOLO
titolo.config(background='#fbebd0')
titolo.pack(pady=35)

#VERSI
versi = Frame(root)
versi.config(background='#fbebd0')
verso1 = Label(versi, font=('Georgia', 36))
verso1.config(background='#fbebd0')
verso1.pack(pady=15)
verso2 = Label(versi, font=('Georgia', 36))
verso2.config(background='#fbebd0')
verso2.pack(pady=15)
verso3 = Label(versi, font=('Georgia', 36))
verso3.config(background='#fbebd0')
verso3.pack(pady=15)
versi.pack(side=LEFT, padx=70)


#PULSANTI
contenitore_pulsanti = Frame(root)
pulsante_istruzioni = Button(contenitore_pulsanti, command=istruzioni, text='Istruzioni', font=('Georgia', 32), bg='#e6ffe6')
pulsante_istruzioni.pack()
pulsante_generatore = Button(contenitore_pulsanti, command=genera, text='Genera', font=('Georgia', 32), bg='#e6ffe6')
pulsante_generatore.pack(fill=X)
contenitore_pulsanti.pack(side=RIGHT, padx=70)

#BARRA MENU
menubar = Menu(root)
menubar.config(background='#b3ffb3', foreground='#00ff00')
root.config(menu=menubar, background='#fbebd0')

menubar.add_command(label='Salva', command=salva)
menubar.add_command(label='Carica', command=carica)
menubar.add_command(label='Chiudi', command=root.quit)


root.mainloop()
