from tkinter import *
from PIL import ImageTk

global window
window = Tk()


# Função para a tela inicial
def iniciar():
    global num_disciplinas, window, creditos, medias

    window.destroy()
    window = Tk()
    window.title("Calculadora CR UERJ")
    window.resizable(False, False)

    Label(
        window,
        text="Seja bem-vinde à calculadora de Coeficiente de Rendimento (CR) da UERJ!",
    ).pack()
    Button(window, text="Iniciar", command=obter_num_disciplinas).pack()
    Button(window, text="Como é calculado o CR da UERJ?", command=sobre_cr).pack()
    Button(window, text="Extra", command=extra).pack()

    window.mainloop()


# Função para calcular o CR
def calcular_cr(num_disciplinas, creditos, medias):
    numerator = 0.0
    denominator = 0.0

    for i in range(num_disciplinas):
        credit = float(creditos[i].get())
        average = float(medias[i].get())
        numerator += credit * average
        denominator += credit

    cr = numerator / denominator

    # Destruir a janela atual e mostrar o resultado
    window.destroy()
    resultado_window = Tk()
    resultado_window.title("")
    resultado_window.resizable(False, False)
    Label(resultado_window, text=f"Seu CR este semestre é: {cr:.2f}").pack()
    resultado_window.mainloop()


# Função para obter o número de disciplinas
def obter_num_disciplinas():
    global window, num_disciplinas

    window.destroy()
    window = Tk()
    window.title("Calculando CR")
    window.resizable(False, False)

    Label(window, text="Quantas matérias você inscreveu-se nesse semestre?").pack()
    num_disciplinas_entry = Entry(window)
    num_disciplinas_entry.pack()

    def proximo():
        num_disciplinas = int(num_disciplinas_entry.get())
        creditos = [None] * num_disciplinas
        medias = [None] * num_disciplinas

        window.destroy()
        configurar_disciplinas(num_disciplinas, creditos, medias)

    Button(window, text="Avançar", command=proximo).pack()
    window.mainloop()


# Função para configurar as disciplinas
def configurar_disciplinas(num_disciplinas, creditos, medias):
    global window

    window = Tk()
    window.title("")
    window.resizable(False, False)

    for i in range(num_disciplinas):
        Label(window, text=f"Quantos créditos a {i+1}ª matéria possui?").pack()
        creditos[i] = Entry(window)
        creditos[i].pack()

        Label(window, text=f"Qual foi sua média na {i+1}ª matéria?").pack()
        medias[i] = Entry(window)
        medias[i].pack()

    Button(
        window,
        text="Calcular CR",
        command=lambda: calcular_cr(num_disciplinas, creditos, medias),
    ).pack()
    window.mainloop()


# Função para a tela "Extra"
def extra():
    global window
    window.destroy()
    window = Tk()
    window.title("")
    window.resizable(False, False)

    Label(
        window, text="Feito com muito carinho por \n Breno Alexandre Santana Silva \n ❤"
    ).pack()

    Button(window, text="Voltar", command=iniciar).pack()
    window.mainloop()


# Função para mostrar informações sobre o CR
def sobre_cr():
    global window
    window.destroy()
    window = Tk()
    window.title("Sobre o CR")
    window.resizable(False, False)

    cr_screen_image = ImageTk.PhotoImage(file="crscreen.jpg")

    Label(window, image=cr_screen_image).pack()
    Button(window, text="Voltar", command=iniciar).pack()

    window.mainloop()


iniciar()
