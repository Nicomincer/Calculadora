import tkinter
from tkinter import Tk

programa = Tk()
programa.title("Calculadora")
programa.geometry("320x480")

frame1 = tkinter.Frame(programa, bg='black')
frame1.place(rely=0, relx=0, relwidth=1, relheight=0.4)

frame2 = tkinter.Frame(programa, bg="white")
frame2.place(rely=0.4, relx=0, relwidth=1, relheight=1)

sete = tkinter.Button(frame2, text="7")
sete.place(relx=0, rely=0, relwidth=0.2, relheight=0.15)

oito = tkinter.Button(frame2, text="8")
oito.place(relx=0.2, rely=0, relwidth=0.2, relheight=0.15)

nove = tkinter.Button(frame2, text="9")
nove.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.15)

seis = tkinter.Button(frame2, text="6")
seis.place(relx=0.4, rely=0.15, relwidth=0.2, relheight=0.15)

cinco = tkinter.Button(frame2, text="5")
cinco.place(relx=0.2, rely=0.15, relwidth=0.2, relheight=0.15)

quatro = tkinter.Button(frame2, text="4")
quatro.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.15)

três = tkinter.Button(frame2, text="3")
três.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.15)

dois = tkinter.Button(frame2, text="2")
dois.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15)

um = tkinter.Button(frame2, text="1")
um.place(relx=0, rely=0.3, relwidth=0.2, relheight=0.15)

zero = tkinter.Button(frame2, text="0")
zero.place(relx=0, rely=0.45, relwidth=0.6, relheight=0.15)

limpar = tkinter.Button(frame2, text="CE")
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