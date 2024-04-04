from genericpath import exists
from http import server
from smtplib import SMTP
import socket
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as ttk

#collegamento con server e Funzione per la connessione e la ricezione del feed
def datafeed():
    sfeed = ""
    porta = 10002 #TRADING DIRECTA 
    buffersize = 256
    nfeed = 100
    comando = "SUBPRZ UCG\n"
    host = socket.gethostname()
    
    # Socket
    try:
        sfeed = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        errore(f"errore nel creare il socket: {err}")

    # Connessione al socket
    try:
        sfeed.connect((host, porta))
    except socket.error as err:
        errore(f"errore di connessione: {err}")  
    
    # Invio comando
    try:
        sfeed.sendall(comando.encode('utf-8')) 
    except socket.error as err:
        errore(f"errore di invio del comando: {err}")
    
    # Ricezione
    try:
        response = sfeed.recv(buffersize)    
        print(response.decode('utf-8'))
    except socket.error as err:
        errore(f"errore di ricezione del datafeed: {err}")
    
    for i in range (1,nfeed):
        try:
            response = sfeed.recv(buffersize)
            print(f"Messaggio numero: {i} dal server: {response.decode('utf-8')}")
        except socket.error as err:
            errore(f"Errore di ricezione della risposta: {err}")
        
    # Chiusura della connessione
    print("Chiusura Connessione")
    sfeed.close()



  
    #finestra
window_menu = ttk.Tk()
window_menu.geometry("600x600")
window_menu.title("lazyportafolio")
window_menu.iconbitmap() #icona a destra

    
def login():
    
    Window = ttk.Toplevel()
    label_username=Label(Window,text="username")
    label_username.pack(padx=5,pady=5)
    username=StringVar()
    username_entry= ttk.Entry(Window,textvariable=username)
    username_entry.pack(padx=5,pady=5)

    label_password=Label(Window,text="password")
    label_password.pack(padx=5,pady=5)
    password=StringVar()
    password_entry= ttk.Entry(Window,textvariable=password, show="*")
    password_entry.pack(padx=5,pady=5)

    submit= ttk.Button(Window, text="login", command=datafeed)
    submit.pack()
    


#np
#prende i ticker degli etf 
etfGold=["PPFB"]
etfBond=["VGEA"]
etfStock=["MEUD"]
etfCommodity=[""]
etfReit=[""]


def Gestione_etf():
    #pause api
    #verifico la connessione
    newWindow = ttk.Toplevel()
    print("fai vedere etf")

    cmd= "infostock"

    button_add=ttk.button(newWindow,text="aggiungi", command=add)
    button_add.pack(padx=5,pady=5)
    button_remove=ttk.button(newWindow,text="rimuovi")
    button_remove.pack(padx=5,pady=5)
    button_change=ttk.button(newWindow,text="cambia")
    button_change.pack(padx=5,pady=5)

        #trovare alternativa da rimozione etf 

def add():      #aggiungi un etf (quindi espando la lista in cui voglio mettere un etf) CONTROLLARE
    newWindow = ttk.Toplevel()
    print("inserisci Ticker")
    label_Add_Etf=Label(newWindow,text="nome etf")
    label_Add_Etf.pack(padx=5,pady=5)
    Add_etf=StringVar()
    Add_etf_entry= ttk.Entry(newWindow,textvariable=Add_etf)
    Add_etf_entry.pack(padx=5,pady=5)
    #button sumbit
    for x in range(1,len.etfStock):
        if etfStock ==  Add_etf_entry:
            print("esiste già")
        else:
            etfStock.append(Add_etf_entry)

def remove():   #rimuovi un etf
    newWindow = ttk.Toplevel()
    print("rimuovi ticker")
    label_Remove_Etf=Label(newWindow,text="nome etf")
    label_Remove_Etf.pack(padx=5,pady=5)
    Remove_etf=StringVar()
    Remove_etf_entry= ttk.Entry(newWindow,textvariable=Remove_etf)
    Remove_etf_entry.pack(padx=5,pady=5)
    #button sumbit
    if etfStock !=  Remove_etf_entry:
        print("non esiste")
    else:
        etfStock.remove(Remove_etf_entry)


def change_etf():
    newWindow = ttk.Toplevel()
    print("inserisci ticker")
    
    label_change_Etf=Label(newWindow,text="nome etf da cambiare")
    label_change_Etf.pack(padx=5,pady=5)
    change_etf=StringVar()
    change_etf_entry= ttk.Entry(newWindow,textvariable=change_etf)
    change_etf_entry.pack(padx=5,pady=5)
    #buttonSumbit
    if etfStock == change_etf_entry:
        print("esiste")
        return change_etf
    else :
        etfStock.append(change_etf_entry)

def rules():
    print("passo di interesse minimo richiesto")
    global interestRate
    interestRate=int(input())
    #immagine interattiva grafico a torta
    print("etf divisione in percentuale")


    print("vuoi fare un ribilanciamento?")
    ribilancimento=input() #checkbox yes or no
    if ribilancimento=="yes":
        print ("specifica")
        #global
    else :
        print("non verrà effettuato nessun ribilanciamento")



#inizia qui

cmd= "STOCK"
serverData=cmd
takeData = serverData.split(",", 4)       #prende quantità directa e negozazione
inNegoziate   =   serverData.split(",", 5)
#bisogna leggerlo all'interno poi fare il calcolo
quantity=takeData
if inNegoziate > 0:
    print("già in vendita")
vendita="venmarket "+ ord + "," + change_etf + "," + quantity 
cmd = vendita
etfStock.remove(change_etf)
buy = "acqmarket "+ ord + "," + Add_etf_entry + "," + quantity   
cmd = buy
etfStock.insert(Add_etf_entry)



    


""" TrackError
#track error da controllare
def trackErrorGold (): #errori sull'oro INCOMPLETO
trackGold = yf.ticker("COMEX")
if etfGold<trackGold:
    cmd="venmarket"
    cmd="acqmarket"

def trackErrorBond():  #errori sui bond INCOMPLETO
print("")   

def trackErrorStock(): #errori sulle azioni INCOMPLETO
print("")

def errore(messaggio):
print(messaggio)
exit(0)

"""


"""
ord=0

sumList= len(etfGold)+len(etfStock)+len(etfBond)+len(etfCommodity)+len(etfReit)
for x in range(1,sumList):  #somma degli array
    etfGold
    etfStock
    etfBond
#controlloTassi di interesse
#interestRate = yf.ticker("")
#if interestRate < RequestInterestRate:


#controllo inefficenze di mercato
#trackErrorGold
#trackErrorBond
#trackErrorStock

"""

#bottoni

buttonlogin= ttk.Button(window_menu,text="login",command=login)
buttonModificaEtf= ttk.Button(window_menu,text="modity etf",command=Gestione_etf)
buttonRebalance= ttk.Button(window_menu,text="rules",command=rules)
buttonlogin.grid(row=0, column=0), buttonModificaEtf.grid(row=1, column=0),buttonRebalance.grid(row=2, column=0)

if __name__ == "__main__":
    window_menu.mainloop()



