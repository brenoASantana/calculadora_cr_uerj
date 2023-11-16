import tkinter

def telaInicial():
    print(
        """
        Seja bem-vinde à calculadora de Coeficiente de Rendimento (CR) da UERJ!
        1 - Iniciar
        2 - Saber mais sobre como é calculado o CR
        3 - Extra
        0 - Sair
        """        
    )
    return int(input())


def cr():
    return None

op = telaInicial()

match op:
    case 1:
        quantMat = int(input("Quantas matérias você inscreveu-se nesse semestre?\n"))

        materias = [""]*quantMat

        notas = [0.0]*quantMat
        medias = [0.0]*quantMat
        creditos  = [0]*quantMat

        ## matriz para os dados?

        for i in range(quantMat):
            materias[i] = str(input(f"Qual o nome da {i}º matéria?\n"))
            ## Talvez fazer um banco de dados com os nomes das materias e dos institutos?
            creditos = int(input(f"Quantas créditos a matéria de {nomeMat} possuí?\n"))
            notas = int(input(f"Qual foi sua nota na matéria de {nomeMat}?\n"))
            medias = int(input(f"Qual média da matéria de {nomeMat}?\n"))
            isConfirm = bool(input("Todas as informações acima estão corretas?\n"))

        if isConfirm == True:
            cr(credMat, mediaMat)
        else:
            mediaMat = int(input("Qual dado você deseja alterar?"))


    case 2:
        print()
## mostra a imagem crscreen

## O cálculo do Coeficiente de Rendimento (CR) é feito para os estudantes do Regime de Crédito com o objetivo de classificá-los dentro do curso. Essa classificação estabelece prioridades no preenchimento das vagas nas disciplinas/turmas escolhidas. Para calcular o CR, utiliza-se a seguinte fórmula:
## CR = Somatório (n° de créditos  X nota) / Somatório (nº de créditos)
## NUMERADOR: Somatório dos produtos dos créditos de cada disciplina pela respectiva nota, tanto na aprovação como na reprovação por nota ou frequência.
## DENOMINADOR: Cálculo do somatório dos créditos.
## No cálculo do CR não são consideradas as disciplinas com situação de isenção, aprovação sem nota e inscrição cancelada.