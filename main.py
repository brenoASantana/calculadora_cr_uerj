def telaInicial():
    print(
        """
        Seja bem-vind à calculadora 
        """
    )


def cr():
    return None


quantMat = int(input("Quantas matérias você inscreveu-se nesse semestre?\n"))

nomeMat = str(input("Quantas matérias você inscreveu-se nesse semestre?\n"))

credMat = int(input(f"Quantas créditos a matéria de {nomeMat} possuí?\n"))

notaMat = int(input(f"Qual foi sua nota na matéria de {nomeMat}?\n"))

mediaMat = int(input(f"Qual média da matéria de {nomeMat}?\n"))

isConfirm = bool(input("Todas as informações acima estão corretas?\n"))

if confirm == True:
    cr(credMat, mediaMat)
else:
    mediaMat = int(input("Qual dado você deseja alterar?"))

## O cálculo do Coeficiente de Rendimento (CR) é feito para os estudantes do Regime de Crédito com o objetivo de classificá-los dentro do curso. Essa classificação estabelece prioridades no preenchimento das vagas nas disciplinas/turmas escolhidas. Para calcular o CR, utiliza-se a seguinte fórmula:
## CR = Somatório (n° de créditos  X nota) / Somatório (nº de créditos)
## NUMERADOR: Somatório dos produtos dos créditos de cada disciplina pela respectiva nota, tanto na aprovação como na reprovação por nota ou frequência.
## DENOMINADOR: Cálculo do somatório dos créditos.
## No cálculo do CR não são consideradas as disciplinas com situação de isenção, aprovação sem nota e inscrição cancelada.