from tkinter import *


def cr(quantMat, creditos, medias):
    ## O cálculo do Coeficiente de Rendimento (CR) é feito para os estudantes do Regime de Crédito com o objetivo de classificá-los dentro do curso. Essa classificação estabelece prioridades no preenchimento das vagas nas disciplinas/turmas escolhidas. Para calcular o CR, utiliza-se a seguinte fórmula:
    ## CR = Somatório (n° de créditos  X nota) / Somatório (nº de créditos)
    ## NUMERADOR: Somatório dos produtos dos créditos de cada disciplina pela respectiva nota, tanto na aprovação como na reprovação por nota ou frequência.
    ## DENOMINADOR: Cálculo do somatório dos créditos.
    ## No cálculo do CR não são consideradas as disciplinas com situação de isenção, aprovação sem nota e inscrição cancelada.

    numerador = 0.0
    denominador = 0.0

    for i in range(quantMat):
        credito = creditos[i]
        media = medias[i]
        numerador += credito * media
        denominador += credito

    cr = numerador / denominador

    return cr


quantMat = 0
isGerarArqRes = False


while True:

    match op:
        ## Iniciar
        case 1:
            GerarArqRes = int(
                input("Você deseja gerar um arquivo de texto com os dados e o resultado? 1-Sim 2-Não\n")
            )
            if GerarArqRes == 1:
                file = open("Resultado_CR.txt","w")
                isGerarArqRes = True

            quantMat = int(
                input("Quantas matérias você inscreveu-se nesse semestre?\n")
            )

            nomesMaterias = [""] * quantMat
            creditos = [0] * quantMat
            medias = [0.0] * quantMat

            iError = -1
            i = 0

            ## Um while no lugar de um for para poder retornar o valor do indice caso o usuário queira corrigir os dados
            while i < quantMat:
                nomeMateria = str(input(f"Qual o nome da {i+1}º matéria?\n"))

                credito = int(
                    input(f"Quantos créditos a matéria de {nomeMateria} possuí?\n")
                )

                media = float(
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
            
            if isGerarArqRes == True:
                file.closed
            ## ou continue?
            break
        ## Sobre
        case 2:
            print("sobre")
            continue
        ## mostra a imagem crscreen

        ## Extra
        case 3:
            print("extra")
            continue

        ## Sair
        case 0:
            print("Saindo do programa...")
            break

        case _:
            print("Por favor, selecione uma das opções disponíveis.")
            continue

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
    ## Pular uma linha
    button = Button(window, text="Sair", command="")
    button.grid(column=1, row=6)
    
    window.mainloop() 
    
def aboutCR():
    window = Tk()
    window.title("Sobre o CR")
    Image(window, )
    text = Label(window, text="Seja bem-vinde à calculadora de Coeficiente de Rendimento (CR) da UERJ!")
    text.grid(column=0, row=0)

    button = Button(window, text="Iniciar", command=calculateCR)
    button = Button(window, text="Saber mais sobre como é calculado o CR", command="")
    # button = Button(window, text="Extra", command=)

    # Pular uma linha
    #button = Button(window, text="Sair", command="")
    button.grid
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
    ## Pular uma linha
    button = Button(window, text="Sair", command="")
    button.grid
    window.mainloop() 