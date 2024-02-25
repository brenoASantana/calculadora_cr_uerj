from tkinter import *
from PIL import Image, ImageTk

def index():
    window = Tk()
    window.title("Calculadora CR UERJ")

    text = Label(window, text="Seja bem-vinde à calculadora de Coeficiente de Rendimento (CR) da UERJ!")
    text.grid(column=1, row=0)

    button = Button(window, text="Iniciar", command=calculateCR)
    button.grid(column=1, row=1)
    button = Button(window, text="Saber mais sobre como é calculado o CR", command=aboutCR)
    button.grid(column=1, row=2)
    button = Button(window, text="Extra", command="")
    button.grid(column=1, row=4)
    
    window.mainloop() 
    
def aboutCR():
    window = Tk()
    window.title("Sobre o CR")

    ## image = Image.open("crscreen.jpg")

    image = ImageTk.PhotoImage(file="crscreen.jpg")
    label_imagem = Label(window, image=image)
    label_imagem.image = image  # Mantenha uma referência à imagem
    label_imagem.pack()

    button = Button(window, text="Voltar", command=index)
    button.grid(column=1,row=1)
    window.mainloop() 

def calculateCR():
    window = Tk()
    window.title("Calculando CR")
    Image(window, )
    text = Label(window, text="Quantas matérias você inscreveu-se nesse semestre?")
    text.grid(column=0, row=0)

    button = Button(window, text="Iniciar", command="")
    button = Button(window, text="Saber mais sobre como é calculado o CR", command="")
    button = Button(window, text="Extra", command="")

    button = Button(window, text="Sair", command="")
    button.grid
    window.mainloop() 

index()