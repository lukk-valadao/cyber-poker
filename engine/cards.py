import random

# Naipes e valores disponíveis
NAIPES = ['♠','♥','♦','♣']
VALORES = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

def criar_baralho():
    """
    Cria um baralho padrão de 52 cartas.
    Ex: 'A♠', '10♥'
    """
    return [v+n for v in VALORES for n in NAIPES]

def embaralhar(baralho):
    """
    Embaralha o baralho in-place e retorna.
    """
    random.shuffle(baralho)
    return baralho

def valor_para_num(carta):
    """
    Converte carta para valor numérico seguro:
    J=11, Q=12, K=13, A=14
    """
    valor = carta[:-1]
    mapa = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    if valor in mapa:
        return mapa[valor]

    return int(valor)
