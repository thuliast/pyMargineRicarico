"""
Un semplice calcolatore di margine e ricarico
in Python.
Autore: Francesco Tattoli
Data di Creazione: 29-12-2022
"""
from tkinter import *



#Definisco le variabili
aliq_iva = 0.00
costo_impon = 0.00
costo_ivato = 0.00
prezzo_ivato = 0.00
margine = 0.00
ricarico = 0.00


def on_exit():
    #Esco dall'applicazione
    mainWindow.quit()

    
def calcola_marginericarico():
    #Azzero le textbox con i risultati
    txtPercMargine.delete(0,END)
    txtPercRicarico.delete(0,END)
    
    #Ricevo in input i dati necessari per i calcoli
    costo_impon=float(txtCostoImpon.get())
    aliq_iva=float(txtAliqIva.get())
    prezzo_ivato=float(txtPrezzoIvato.get())

    #Calcolo il costo ivato, utile per il calcolo successivo
    #di margine e ricarico
    costo_ivato = costo_impon * (aliq_iva/100) + costo_impon

    #Calcolo il margine di guadagno
    margine = (prezzo_ivato - costo_ivato) / prezzo_ivato
    #Calcolo il margine di ricarico
    ricarico = (prezzo_ivato - costo_ivato) / costo_ivato

    #Stampo a video i risultati
    txtPercMargine.insert(END, round(margine * 100,2))
    txtPercRicarico.insert(END, round(ricarico * 100,2))
    

#PARTE GRAFICA
mainWindow = Tk()
mainWindow.title("CALCOLO MARGINE E RICARICO")
mainWindow.geometry("350x350")

lblCostoImpon = Label(mainWindow, text="Costo Imponibile", width=16)
lblCostoImpon.pack(side=TOP, padx=5)
txtCostoImpon = Entry(mainWindow, width=74)
txtCostoImpon.pack(side=TOP, padx=5)

lblAliqIva = Label(mainWindow, text="Aliquota Iva", width=16)
lblAliqIva.pack(side=TOP, padx=5)
txtAliqIva = Entry(mainWindow, width=74)
txtAliqIva.pack(side=TOP, padx=5)

lblPrezzoIvato = Label(mainWindow, text="Prezzo Ivato", width=16)
lblPrezzoIvato.pack(side=TOP, padx=5)
txtPrezzoIvato = Entry(mainWindow, width=74)
txtPrezzoIvato.pack(side=TOP, padx=5)

btnCalcola = Button(mainWindow, text="Calcola Margine e Ricarico", command=calcola_marginericarico, width=20)
btnCalcola.pack(side=TOP, padx=5)

lblPercMargine = Label(mainWindow, text="MARGINE %", width=120)
lblPercMargine.pack(side=TOP, padx=5)
txtPercMargine = Entry(mainWindow, width = 74)
txtPercMargine.pack(side=TOP, padx=5)

lblPercRicarico = Label(mainWindow, text="RICARICO %", width=120)
lblPercRicarico.pack(side=TOP, padx=5)
txtPercRicarico = Entry(mainWindow, width = 74)
txtPercRicarico.pack(side=TOP, padx=5)


def main():
    mainWindow.mainloop()


if __name__=="__main__":
    main()
