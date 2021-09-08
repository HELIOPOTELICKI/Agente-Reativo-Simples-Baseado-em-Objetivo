#imports
import numpy as np
import matplotlib.pyplot as plt
import random


def gerar_mapa():
    #Mapa 4x4
    Mapa = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]

    for i in range(0, len(Mapa)):
        for j in range(0, len(Mapa)):
            if Mapa[i][j] == 0:
                Mapa[i][j] = random.choice([0, 2])
    return Mapa


gerar_mapa()

posAPAx = 1
posAPAy = 1


# Função que exibe o ambiente na tela
def exibir(I):
    global posAPAx
    global posAPAy
    # Altera o esquema de cores do ambiente
    plt.imshow(I, 'gray')
    plt.nipy_spectral()
    # Coloca o agente no ambiente
    plt.plot([posAPAx], [posAPAy], marker='o', color='r', ls='')
    plt.show(block=False)
    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(0.5)
    plt.clf()


def agenteReativoSimples():
    global posAPAx
    global posAPAy
    if mapa[posAPAy][posAPAx] == 2:
        return "aspirar"
    else:
        direcoes_possiveis = ["abaixo", "acima", "direita", "esquerda"]
        if mapa[posAPAy][posAPAx + 1] == 1:
            direcoes_possiveis.remove("direita")
        elif mapa[posAPAy][posAPAx + 1] == 2:
            return "direita"
        if mapa[posAPAy][posAPAx - 1] == 1:
            direcoes_possiveis.remove("esquerda")
        elif mapa[posAPAy][posAPAx - 1] == 2:
            return "esquerda"
        if mapa[posAPAy + 1][posAPAx] == 1:
            direcoes_possiveis.remove("abaixo")
        elif mapa[posAPAy + 1][posAPAx] == 2:
            return "abaixo"
        if mapa[posAPAy - 1][posAPAx] == 1:
            direcoes_possiveis.remove("acima")
        elif mapa[posAPAy - 1][posAPAx] == 2:
            return "acima"
        return random.choice(direcoes_possiveis)


def ainda_ha_sujeira(map):
    for i in range(0, len(map)):
        for j in range(0, len(map)):
            if map[i][j] == 2:
                return True
    return False


def agenteObjetivo(percepcao):
    global posAPAx
    global posAPAy
    global mapa
    print(f"Ação escolhida: '{percepcao}'")
    if percepcao == "direita":
        posAPAx += 1
    elif percepcao == "esquerda":
        posAPAx -= 1
    elif percepcao == "acima":
        posAPAy -= 1
    elif percepcao == "abaixo":
        posAPAy += 1
    elif percepcao == "aspirar":
        mapa[posAPAy][posAPAx] = 0
    exibir(mapa)


###########OPERAÇÂO############
mapa = gerar_mapa()
exibir(mapa)
while ainda_ha_sujeira(mapa):
    agenteObjetivo(agenteReativoSimples())

posAPAx = 1
posAPAy = 1
pontos = []


def agenteReativoSimples():
    global posAPAx
    global posAPAy
    if mapa[posAPAy][posAPAx] == 2:
        return "aspirar"
    else:
        direcoes_possiveis = ["abaixo", "acima", "direita", "esquerda"]
        if mapa[posAPAy][posAPAx + 1] == 1:
            direcoes_possiveis.remove("direita")
        elif mapa[posAPAy][posAPAx + 1] == 2:
            return "direita"
        if mapa[posAPAy][posAPAx - 1] == 1:
            direcoes_possiveis.remove("esquerda")
        elif mapa[posAPAy][posAPAx - 1] == 2:
            return "esquerda"
        if mapa[posAPAy + 1][posAPAx] == 1:
            direcoes_possiveis.remove("abaixo")
        elif mapa[posAPAy + 1][posAPAx] == 2:
            return "abaixo"
        if mapa[posAPAy - 1][posAPAx] == 1:
            direcoes_possiveis.remove("acima")
        elif mapa[posAPAy - 1][posAPAx] == 2:
            return "acima"
        if ainda_ha_sujeira(mapa):
            return random.choice(direcoes_possiveis)
        else:
            return "NoOp"


def checkObj(map):
    for i in range(0, len(map)):
        for j in range(0, len(map)):
            if map[i][j] == 2:
                return True
    return False


def agenteObjetivo(percepcao):
    global posAPAx
    global posAPAy
    global mapa

    pontos.append(
        f"Estado da percepcao: {get_sujeira(posAPAx, posAPAy, mapa)} Acao escolhida: {percepcao}"
    )

    if percepcao == "direita":
        posAPAx += 1
    elif percepcao == "esquerda":
        posAPAx -= 1
    elif percepcao == "acima":
        posAPAy -= 1
    elif percepcao == "abaixo":
        posAPAy += 1
    elif percepcao == "aspirar":
        mapa[posAPAy][posAPAx] = 0
    elif percepcao == "NoOp":
        return


def get_sujeira(x, y, mapa):
    if mapa[y][x] == 2:
        return 1
    else:
        return 0


###################OPERAÇÂO############################
mapa = gerar_mapa()
exibir(mapa)
while checkObj(mapa):
    agenteObjetivo(agenteReativoSimples())
    exibir(mapa)