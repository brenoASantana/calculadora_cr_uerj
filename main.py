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