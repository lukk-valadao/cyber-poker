from engine.cards import criar_baralho, embaralhar
from engine.evaluator import melhor_mao, comparar_maos

class TexasHoldemGame:
    def __init__(self):
        # Economia
        self.buyin = 100
        self.small_blind = 5
        self.big_blind = 10

        self.jogador_fichas = self.buyin
        self.cpu_fichas = self.buyin

        self.nova_rodada()

    def nova_rodada(self):
        """Reseta tudo para uma nova mão"""
        self.baralho = embaralhar(criar_baralho())
        self.jogador = [self.baralho.pop(), self.baralho.pop()]
        self.cpu = [self.baralho.pop(), self.baralho.pop()]
        self.mesa = []

        self.fase = "preflop"
        self.pote = 0

        self.aplicar_blinds()

    def aplicar_blinds(self):
        self.jogador_fichas -= self.small_blind
        self.cpu_fichas -= self.big_blind
        self.pote = self.small_blind + self.big_blind

    def apostar(self, valor=10):
        self.jogador_fichas -= valor
        self.pote += valor

    def avancar_fase(self):
        if self.fase == "preflop":
            self.mesa += [self.baralho.pop() for _ in range(3)]
            self.fase = "flop"

        elif self.fase == "flop":
            self.mesa.append(self.baralho.pop())
            self.fase = "turn"

        elif self.fase == "turn":
            self.mesa.append(self.baralho.pop())
            self.fase = "river"

        elif self.fase == "river":
            self.fase = "showdown"

    def showdown(self):
        mao_j = melhor_mao(self.jogador + self.mesa)
        mao_c = melhor_mao(self.cpu + self.mesa)

        vencedor = comparar_maos(mao_j, mao_c)

        return {
            "jogador": mao_j,
            "cpu": mao_c,
            "vencedor": vencedor
        }
