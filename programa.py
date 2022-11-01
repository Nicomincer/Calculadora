import tkinter
from tkinter import Tk


programa = Tk()
programa.title("Calculadora")
programa.geometry("320x480")

def zero():
    escrever_texto1 = tkinter.Label(frame1, text="0", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)
def um():
    escrever_texto1 = tkinter.Label(frame1, text="1", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)
def dois():
    escrever_texto1 = tkinter.Label(frame1, text="2", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)
def três():
    escrever_texto1 = tkinter.Label(frame1, text="3", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)
def quatro():
    escrever_texto1 = tkinter.Label(frame1, text="4", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)
def cinco():
    escrever_texto1 = tkinter.Label(frame1, text="5", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)
def seis():
    escrever_texto1 = tkinter.Label(frame1, text="6", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)
def sete():
    escrever_texto1 = tkinter.Label(frame1, text="7", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)
def oito():
    escrever_texto1 = tkinter.Label(frame1, text="8", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)
def nove():
    escrever_texto1 = tkinter.Label(frame1, text="9", font=("Arial", 50), background='black', foreground='white')
    escrever_texto1.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)

frame1 = tkinter.Frame(programa, bg='black')
frame1.place(rely=0, relx=0, relwidth=1, relheight=0.4)

frame2 = tkinter.Frame(programa, bg="white")
frame2.place(rely=0.4, relx=0, relwidth=1, relheight=1)

sete = tkinter.Button(frame2, text="7", command=sete)
sete.place(relx=0, rely=0, relwidth=0.2, relheight=0.15)

oito = tkinter.Button(frame2, text="8", command=oito)
oito.place(relx=0.2, rely=0, relwidth=0.2, relheight=0.15)

nove = tkinter.Button(frame2, text="9", command=nove)
nove.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.15)

seis = tkinter.Button(frame2, text="6", command=seis)
seis.place(relx=0.4, rely=0.15, relwidth=0.2, relheight=0.15)

cinco = tkinter.Button(frame2, text="5", command=cinco)
cinco.place(relx=0.2, rely=0.15, relwidth=0.2, relheight=0.15)

quatro = tkinter.Button(frame2, text="4", command=quatro)
quatro.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.15)

três = tkinter.Button(frame2, text="3", command=três)
três.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.15)

dois = tkinter.Button(frame2, text="2", command=dois)
dois.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15)

um = tkinter.Button(frame2, text="1", command=um)
um.place(relx=0, rely=0.3, relwidth=0.2, relheight=0.15)

zero = tkinter.Button(frame2, text="0", command=zero)
zero.place(relx=0, rely=0.45, relwidth=0.6, relheight=0.15)

def clear():
    limpar_tela = tkinter.Label(frame1, text='', font=("Arial", 50), background='black', foreground='white')
    limpar_tela.place(relx=0, rely=0.45, relwidth=0.3, relheight=0.3)

limpar = tkinter.Button(frame2, text="CE", command=clear)
limpar.place(relx=0.6, rely=0, relwidth=0.2, relheight=0.15)

m = tkinter.Button(frame2, text="M")
m.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.15)

mais = tkinter.Button(frame2, text="+")
mais.place(relx=0.6, rely=0.15, relwidth=0.2, relheight=0.15)

menos = tkinter.Button(frame2, text="-")
menos.place(relx=0.8, rely=0.15, relwidth=0.2, relheight=0.15)

multiplicar = tkinter.Button(frame2, text="x")
multiplicar.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.15)

dividir = tkinter.Button(frame2, text="/")
dividir.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.15)

raiz = tkinter.Button(frame2, text="sqrt")
raiz.place(relx=0.6, rely=0.45, relwidth=0.2, relheight=0.15)

fatorial = tkinter.Button(frame2, text="!")
fatorial.place(relx=0.8, rely=0.45, relwidth=0.2, relheight=0.15)

programa.mainloop()