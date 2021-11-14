from tkinter import * 

def resultado():
    a = ''
    b = ''
    tamanho = len(resposta['text'])
    if '+' in resposta['text']:
        position = resposta['text'].index('+')
        for c in range(0, position):
            a += resposta['text'][c]
        a = int(a)
        for i in range(position, tamanho):
            b += resposta['text'][i]
        b = int(b)
        x = a + b 
    else:
        position = resposta['text'].index('-')
        for c in range(0, position):
            a += resposta['text'][c]
        a = int(a)
        for i in range(position+1, tamanho):
            b += resposta['text'][i]
        b = int(b)
        x = a - b
    if '-' in resposta['text']:
        x = a - b
    elif '+' in resposta['text']:
        x = a + b
    resposta['text'] = ''
    resposta2['text'] = str(x)
    return 

def one():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'1'

def two():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'2'

def three():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'3'

def four():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'4'

def five():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'5'

def six():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'6'

def seven():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'7'

def eight():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'8'

def nine():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'9'

def zero():
    resposta2['text'] = ''
    resposta['text'] = resposta['text']+'0'

def plus():
    if '+' in resposta['text']:
        return 
    elif '-' in resposta['text']:
        return
    elif resposta['text'] == '':
        return 
    else:
        resposta['text'] = resposta['text']+'+'

def minus():
    if '+'  in resposta['text']:
        return
    elif '-' in resposta['text']:
        return
    elif resposta['text'] == '':
        return 
    else:
        resposta['text'] = resposta['text']+'-'



programa = Tk()
foto_icone = PhotoImage(file='calculator2.PNG')
programa.iconphoto(programa, foto_icone)
programa.geometry('250x300')
programa.title('Calculadora')

frame1 = Frame(programa, bg='black', width=500, height=120)
frame1.place(x=0, y=0)

one = Button(programa, text='1', width=5, height=3, command=one)
one.place(x=0, y=120)

two = Button(programa, text='2', width=5, height=3, command=two)
two.place(x=47, y=120)

three = Button(programa, text='3', width=5, height=3, command=three)
three.place(x=94, y=120)

four = Button(programa, text='4', width=5, height=3, command=four)
four.place(x=141, y=120)

five = Button(programa, text='5', width=5, height=3, command=five)
five.place(x=0, y=175)

six = Button(programa, text='6', width=5, height=3, command=six)
six.place(x=47, y=175)

seven = Button(programa, text='7', width=5, height=3, command=seven)
seven.place(x=94, y=175)

eight = Button(programa, text='8', width=5, height=3, command=eight)
eight.place(x=141, y=175)

nine = Button(programa, text='9', width=5, height=3, command=nine)
nine.place(x=0, y=230)

zero = Button(programa, text='0', width=19, height=3, command=zero)
zero.place(x=43, y=230)

plus = Button(programa, text='+', width=8, height=3, command=plus)
plus.place(x=185, y=120)

minus = Button(programa, text='-', width=8, height=3, command=minus)
minus.place(x=185, y=175)

result = Button(programa, text='=', width=8, height=3, command=resultado)
result.place(x=185, y=230)

resposta = Label(frame1, text='', fg='white', bg='black')
resposta.configure(font=('', 50))
resposta.place(x=0, y=50)

resposta2 = Label(frame1, text='', fg='white', bg='black')
resposta2.configure(font=('', 50))
resposta2.place(x=0, y=50)

programa.mainloop()