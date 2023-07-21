import random as rd

cartas = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
    }

naipes = ["Espadas", "Copas", "Ouros", "Paus"]

cartasmao = []
naipesmao = []
pontuacaodacarta = []

cartaspc = []
naipespc = []
pontuacaopc =[]

def inicializamao():
    for _ in range(2):
        carta, ponto = rd.choice(list(cartas.items()))
        naipe = rd.choice(naipes)
        cartasmao.append(carta)
        naipesmao.append(naipe)
        pontuacaodacarta.append(ponto)

def inicializamaopc():
    for _ in range(2):
        carta, ponto = rd.choice(list(cartas.items()))
        naipe = rd.choice(naipes)
        cartaspc.append(carta)
        naipespc.append(naipe)
        pontuacaopc.append(ponto)
    
def mostramao():
    for k in range(0,len(cartasmao)):
        print(cartasmao[k],"de",naipesmao[k])
    pontuacao = sum(pontuacaodacarta)
    print("Pontuação da mão:",pontuacao)

def puxacarta():
    carta, ponto = rd.choice(list(cartas.items()))
    naipe = rd.choice(naipes)
    cartasmao.append(carta)
    naipesmao.append(naipe)
    pontuacaodacarta.append(ponto)

def pcjoga():
    for _ in range(2):
        carta, ponto = rd.choice(list(cartas.items()))
        naipe = rd.choice(naipes)
        cartaspc.append(carta)
        naipespc.append(naipe)
        pontuacaopc.append(ponto)
    pontuacaototalpc = sum(pontuacaopc)

    while (pontuacaototalpc < 17 or len(cartaspc) < 5) and pontuacaototalpc != 21 and pontuacaototalpc <= 21:
        carta, ponto = rd.choice(list(cartas.items()))
        naipe = rd.choice(naipes)
        cartaspc.append(carta)
        naipespc.append(naipe)
        pontuacaopc.append(ponto)
        pontuacaototalpc = sum(pontuacaopc)

        # Verifica se há Ases e ajusta a pontuação do PC caso necessário
        num_ases = cartaspc.count("A")
        while pontuacaototalpc > 21 and num_ases > 0:
            i = cartaspc.index("A")
            pontuacaopc[i] = 1
            pontuacaototalpc = sum(pontuacaopc)
            num_ases -= 1

    # Ajusta a pontuação final do PC após tratar os Ases
    pontuacaopc.clear()
    pontuacaopc.append(pontuacaototalpc)

def testavitoriabj():
    pontuacao = sum(pontuacaodacarta)
    num_ases = cartasmao.count("A")

    if pontuacao > 21:
        while pontuacao > 21 and num_ases > 0:
            i = cartasmao.index("A")
            pontuacaodacarta[i] = 1
            pontuacao = sum(pontuacaodacarta)
            num_ases -= 1

    return pontuacao > 21

def testavitoriapc():
    pontuacaototalpc = sum(pontuacaopc)
    if pontuacaototalpc==21:
        return True
    if pontuacaototalpc>21:
        return False

def testavitoriapontos():
    if testavitoriabj():
        return True
    else:
        pontuacao = sum(pontuacaodacarta)
        pontuacaototalpc = sum(pontuacaopc)
        if pontuacao <= 21 and pontuacao > pontuacaototalpc:
            return True
        else:
            return False