from tkinter import *
from PIL import ImageTk

#! Processo realizado por interface gráfica!
global window
window = Tk()
numSubjects = None

global subjectIndex
subjectIndex = 0


def cr():
    global numSubjects
    global subjectCredits
    global subjectAverages

    numerator = 0.0
    denominator = 0.0

    for i in range(numSubjects):
        credit = subjectCredits[i]
        average = subjectAverages[i]
        numerator += credit * average
        denominator += credit

    cr = numerator / denominator

    global window
    window.destroy()
    window.resizable(False, False)  # Impede redimensionamento
    window = Tk()
    window.title("CR Calculado")
    skipLine(1, 0)
    Label(window, text=f"Seu CR este semestre é: {cr}").grid(column=1, row=1)


def skipLine(col, line):
    return Label(window, text="").grid(column=col, row=line)


def index():
    global window
    window.destroy()
    window = Tk()
    window.title("Calculadora CR UERJ")
    window.resizable(False, False)  # Impede redimensionamento

    skipLine(1, 0)

    Label(
        window,
        text="Seja bem-vinde à calculadora de Coeficiente de Rendimento (CR) da UERJ!",
    ).grid(column=1, row=1)

    skipLine(1, 2)
    Button(window, text="Iniciar", command=numSubjects).grid(column=1, row=3)
    Button(window, text="Como é calculado o CR da UERJ?", command=aboutCR).grid(
        column=1, row=4
    )
    Button(window, text="Extra", command=extra).grid(column=1, row=5)

    skipLine(1, 6)
    window.mainloop()


def extra():
    global window
    window.destroy()
    window = Tk()
    window.resizable(False, False)  # Impede redimensionamento

    skipLine(1, 0)
    Label(
        window,
        text="Feito com muito carinho por \n Breno Alexandre Santana Silva \n ❤",
    ).grid(column=1, row=1)

    skipLine(1, 2)
    Button(window, text="Voltar", command=index).grid(column=1, row=4)

    skipLine(1, 5)

    window.mainloop()


def aboutCR():
    global window
    window.destroy()
    window = Tk()
    window.title("Sobre o CR")
    window.resizable(False, False)  # Impede redimensionamento

    crScreenImage = ImageTk.PhotoImage(file="crscreen.jpg")

    Label(window, image=crScreenImage).grid(column=1, row=0)

    skipLine(1, 1)
    Button(window, text="Voltar", command=index).grid(column=1, row=2)

    skipLine(1, 3)

    window.mainloop()


def numSubjects():
    global window
    window.destroy()
    window = Tk()
    window.title("Calculando CR")
    window.resizable(False, False)  # Impede redimensionamento
    skipLine(1, 0)
    Label(window, text="Quantas matérias você inscreveu-se nesse semestre?").grid(
        column=1, row=1
    )
    global numSubjects
    numSubjects = Entry(window)
    numSubjects.grid(column=1, row=3)
    skipLine(1, 4)
    Button(window, text="Avançar", command=subjects).grid(column=1, row=5)
    skipLine(1, 6)
    window.mainloop()


def subjects():
    global numSubjects
    global subjectCredits
    global subjectAverages
    numSubjects = int(numSubjects.get())

    subjectCredits = [0] * numSubjects
    subjectAverages = [0.0] * numSubjects

    global window

    window.destroy()
    window = Tk()
    window.title("Calculando CR")
    window.resizable(False, False)  # Impede redimensionamento
    skipLine(1, 0)

    i = 0

    for i in range(numSubjects):

        Label(window, text=f"Quantos créditos a {i+1}ª matéria possuí?").grid(
            column=1, row=(i + 1)
        )
        subjectCredit = Entry(window)
        subjectCredit.grid(column=1, row=(i + 2))
        skipLine(1, (i + 3))

        Label(window, text=f"Qual foi sua média na {i+1}ª matéria?").grid(
            column=1, row=(i + 4)
        )
        subjectAverage = Entry(window)
        subjectAverage.grid(column=1, row=(i + 5))
        skipLine(1, (i + 6))

    subjectCredits[i] = subjectCredit
    subjectAverages[i] = subjectAverage

    Button(window, text="Avançar", command=cr).grid(column=1, row=numSubjects)
    skipLine(1, (numSubjects+1))

    window.mainloop()


index()
