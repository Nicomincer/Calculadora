import tkinter
from tkinter import Tk
global escrever_texto1
global resultado

resultado = ""
programa = Tk()
programa.title("Calculadora")
programa.geometry("320x480")
frame1 = tkinter.Frame(programa, bg='black')
frame1.place(rely=0, relx=0, relwidth=1, relheight=1)
frame2 = tkinter.Frame(programa, bg="white")
frame2.place(rely=0.4, relx=0, relwidth=1, relheight=1)
escrever_texto1 = tkinter.Label(frame1, text="", font=("Arial", 50), background='black', foreground='white')
escrever_texto1.place(relx=0, rely=0.1)

def result():
    a = ''
    b = ''
    tamanho = len(escrever_texto1['text'])
    if '+' in escrever_texto1['text']:
        position = escrever_texto1['text'].index('+')
        for c in range(0, position):
            a += escrever_texto1['text'][c]
        a = int(a)
        for i in range(position, tamanho):
            b += escrever_texto1['text'][i]
        b = int(b)
        x = a + b 
    elif 'x' in escrever_texto1['text']: 
        position = escrever_texto1['text'].index('x')
        for c in range(0, position):
            a += escrever_texto1['text'][c]
        a = int(a)
        for i in range(position+1, tamanho):
            b += escrever_texto1['text'][i]
        b = int(b)
        x = a*b
    
    elif '/' in escrever_texto1['text']:
        position = escrever_texto1['text'].index('x')
        for c in range(0, position):
            a += escrever_texto1['text'][c]
        a = int(a)
        for i in range(position+1, tamanho):
            b += escrever_texto1['text'][i]
        b = int(b)
        x = a/b

    elif '-' in escrever_texto1['text']:
        position = escrever_texto1['text'].index('-')
        for c in range(0, position):
            a += escrever_texto1['text'][c]
        a = int(a)
        for i in range(position+1, tamanho):
            b += escrever_texto1['text'][i]
        b = int(b)
        x = a - b

    escrever_texto1['text'] = str(x)


def sete_number():
    global resultado
    resultado = resultado+"7"
    escrever_texto1.configure(text=resultado)

def oito_number():
    global resultado
    resultado = resultado+"8"
    escrever_texto1.configure(text=resultado)
def nove_number():
    global resultado
    resultado = resultado+"9"
    escrever_texto1.configure(text=resultado)
def seis_number():
    global resultado
    resultado = resultado+"6"
    escrever_texto1.configure(text=resultado)
def cinco_number():
    global resultado
    resultado = resultado+"5"
    escrever_texto1.configure(text=resultado)
def quatro_number():
    global resultado
    resultado = resultado+"4"
    escrever_texto1.configure(text=resultado)
def tres_number():
    global resultado
    resultado = resultado+"3"
    escrever_texto1.configure(text=resultado)
def dois_number():
    global resultado
    resultado = resultado+"2"
    escrever_texto1.configure(text=resultado) 
def um_number():
    global resultado
    resultado = resultado+"1"
    escrever_texto1.configure(text=resultado)
def zero_number():
    global resultado
    resultado = resultado+"0"
    escrever_texto1.configure(text=resultado)

def somar():

    global resultado
    resultado = resultado+"+"
    escrever_texto1.configure(text=resultado)

def menos():
    global resultado
    resultado = resultado+"-"
    escrever_texto1.configure(text=resultado)

def limpar_tela():

    global resultado
    resultado = ""
    escrever_texto1.configure(text=resultado)

def multiplica():
    global resultado
    resultado = resultado+"x"
    escrever_texto1.configure(text=resultado)

def dividi():
    global resultado
    resultado = resultado+"/"
    escrever_texto1.configure(text=resultado)

sete = tkinter.Button(frame2, text="7", command=sete_number)
sete.place(relx=0, rely=0, relwidth=0.2, relheight=0.15)

oito = tkinter.Button(frame2, text="8", command=oito_number)
oito.place(relx=0.2, rely=0, relwidth=0.2, relheight=0.15)

nove = tkinter.Button(frame2, text="9", command=nove_number)
nove.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.15)

seis = tkinter.Button(frame2, text="6", command=seis_number)
seis.place(relx=0.4, rely=0.15, relwidth=0.2, relheight=0.15)

cinco = tkinter.Button(frame2, text="5", command=cinco_number)
cinco.place(relx=0.2, rely=0.15, relwidth=0.2, relheight=0.15)

quatro = tkinter.Button(frame2, text="4", command=quatro_number)
quatro.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.15)

três = tkinter.Button(frame2, text="3", command=tres_number)
três.place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.15)

dois = tkinter.Button(frame2, text="2", command=dois_number)
dois.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15)

um = tkinter.Button(frame2, text="1", command=um_number)
um.place(relx=0, rely=0.3, relwidth=0.2, relheight=0.15)

zero = tkinter.Button(frame2, text="0", command=zero_number)
zero.place(relx=0, rely=0.45, relwidth=0.6, relheight=0.15)

limpar = tkinter.Button(frame2, text="CE", command=limpar_tela)
limpar.place(relx=0.6, rely=0, relwidth=0.2, relheight=0.15)

m = tkinter.Button(frame2, text="M")
m.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.15)

mais = tkinter.Button(frame2, text="+", command=somar)
mais.place(relx=0.6, rely=0.15, relwidth=0.2, relheight=0.15)

menor = tkinter.Button(frame2, text="-", command=menos)
menor.place(relx=0.8, rely=0.15, relwidth=0.2, relheight=0.15)

multiplicar = tkinter.Button(frame2, text="x", command=multiplica)
multiplicar.place(relx=0.6, rely=0.3, relwidth=0.2, relheight=0.15)

dividir = tkinter.Button(frame2, text="/", command=dividi)
dividir.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.15)

igual = tkinter.Button(frame2, text="=", command=result)
igual.place(relx=0.6, rely=0.45, relwidth=0.2, relheight=0.15)

raiz = tkinter.Button(frame2, text="√", command='raiz')
raiz.place(relx=0.8, rely=0.45, relwidth=0.2, relheight=0.15)


programa.mainloop()