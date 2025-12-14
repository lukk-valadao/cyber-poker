from collections import Counter
from itertools import combinations
from engine.cards import valor_para_num

def avaliar_5(cartas):
    """
    Avalia exatamente 5 cartas.
    Retorna:
    (
        forca,        # int (1–10)
        desempate,    # lista de valores para comparação
        descricao     # string (ex: "Par", "Full House")
    )
    """

    valores = sorted([valor_para_num(c) for c in cartas], reverse=True)
    naipes = [c[-1] for c in cartas]
    cont = Counter(valores)

    is_flush = len(set(naipes)) == 1
    is_straight = valores == list(range(valores[0], valores[0] - 5, -1))

    # Caso especial: A-2-3-4-5 (wheel)
    if valores == [14, 5, 4, 3, 2]:
        is_straight = True
        valores = [5, 4, 3, 2, 1]

    grupos = sorted(cont.items(), key=lambda x: (-x[1], -x[0]))
    contagens = sorted(cont.values(), reverse=True)

    # ==========================
    # STRAIGHT / FLUSH
    # ==========================
    if is_straight and is_flush:
        if valores[0] == 14:
            return (10, valores, "Royal Flush")
        return (9, valores, "Straight Flush")

    # ==========================
    # GRUPOS
    # ==========================
    if contagens == [4, 1]:
        quad = grupos[0][0]
        kicker = grupos[1][0]
        return (8, [quad, kicker], "Quadra")

    if contagens == [3, 2]:
        return (7, [grupos[0][0], grupos[1][0]], "Full House")

    if is_flush:
        return (6, valores, "Flush")

    if is_straight:
        return (5, valores, "Sequência")

    if contagens == [3, 1, 1]:
        return (
            4,
            [grupos[0][0]] +
            sorted([g[0] for g in grupos[1:]], reverse=True),
            "Trinca"
        )

    if contagens == [2, 2, 1]:
        pares = sorted([g[0] for g in grupos if g[1] == 2], reverse=True)
        kicker = [g[0] for g in grupos if g[1] == 1]
        return (3, pares + kicker, "Dois Pares")

    if contagens == [2, 1, 1, 1]:
        return (
            2,
            [grupos[0][0]] +
            sorted([g[0] for g in grupos[1:]], reverse=True),
            "Par"
        )

    # ==========================
    # CARTA ALTA
    # ==========================
    return (1, valores, "Carta Alta")


def melhor_mao(cartas):
    """
    Retorna a melhor mão possível entre 7 cartas.
    """
    return max(
        (avaliar_5(list(c)) for c in combinations(cartas, 5)),
        key=lambda x: (x[0], x[1])
    )

def comparar_maos(mao_j, mao_c):
    """
    Compara duas mãos já avaliadas.
    """
    forca_j, desemp_j, _ = mao_j
    forca_c, desemp_c, _ = mao_c

    if forca_j > forca_c:
        return "Jogador"
    if forca_j < forca_c:
        return "CPU"

    if desemp_j > desemp_c:
        return "Jogador"
    if desemp_j < desemp_c:
        return "CPU"

    return "Empate"
