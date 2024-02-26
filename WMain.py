from tkinter import *
from PIL import ImageTk

class WMain:
    #! Processo realizado por interface gráfica!
    window = Tk()
    numSubjects = None

    def cr(numSubjects, credits, averages):

        numerator = 0.0
        denominator = 0.0

        for i in range(numSubjects):
            credit = subCredits[i]
            average = averages[i]
            numerator += credit * average
            denominator += credit

        cr = numerator / denominator

        return cr

    def skipLine(col, line):
        return Label(window, text="").grid(column=col, row=line)


    def index():
        global window
        window.destroy()
        window = Tk()
        window.title("Calculadora CR UERJ")

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
        Button(window, text="Extra", command="").grid(column=1, row=5)

        skipLine(1, 6)
        window.mainloop()


    def aboutCR():
        global window
        window.destroy()
        window = Tk()
        window.title("Sobre o CR")

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
        numSubjects = numSubjects.get()
        
        subjectNames = [""] * numSubjects
        subjectCredits = [0] * numSubjects
        subjectAverages = [0.0] * numSubjects
        
        global window
        window.destroy()
        window = Tk()
        window.title("Calculando CR")
        skipLine(1, 0)
        Label(window, text="a").grid(column=1, row=1)
        
        iError = -1
        i = 0
        # TODO: Converter algoritmo para o tkinter
        # TODO: Planejar se informa os dados em janelas separadas ou tudo na mesma janela
        ## Um while no lugar de um for para poder retornar o valor do indice caso o usuário queira corrigir os dados
        while i < numSubjects:
                nameSubject = str(input(f"Qual o nome da {i+1}º matéria?\n"))

                credit = int(
                        input(f"Quantos créditos a matéria de {nomeMateria} possuí?\n")
                    )

                average = float(
                        input(f"Qual foi sua média na matéria de {nomeMateria}?\n")
                    )

                isConfirm = int(
                        input("Todas as informações acima estão corretas? 1-Sim 2-Não\n")
                    )

                ## Primeiro confirma se os dados estão certo antes de adicioná-los no vetor
                if isConfirm == 1:
                    nomesMaterias[i] = nomeMateria
                    creditos[i] = credito
                    medias[i] = media

                else:
                    print("OK. Vamos tentar novamente...")
                    ## Volta uma posição para sobrescrever os dados
                    i -= 1
                i += 1

        cr = cr(quantMat, creditos, medias)
        ## Perguntar se desejar gerar um arquivo com os dados
        print(f"Seu CR este semestre é: {cr:.2f}")
                

                ## ou continue?
                
        # * Ordem para calcular CR:
        # * 1. Nº de Disciplinas
        # * 2. Nome, Crédito e Média na Disciplina
        # * 3. Resultado do CR


    # chamada de procedimento que inicia o processo
    index()
