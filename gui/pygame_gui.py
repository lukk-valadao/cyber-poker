import sys
import os
import pygame
from collections import Counter

# ==========================
# AJUSTE DE PATH
# ==========================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from engine.game import TexasHoldemGame
from engine.cards import valor_para_num
from engine.evaluator import melhor_mao

# ==========================
# CONFIGURAÇÕES DO PYGAME
# ==========================
pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Poker – Texas Hold'em")

clock = pygame.time.Clock()
FPS = 30

# ==========================
# CORES
# ==========================
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
YELLOW = (205, 150, 98)
BLACK = (0, 0, 0)

# ==========================
# FONTES
# ==========================
FONT = pygame.font.Font(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32
)
FONT_SMALL = pygame.font.Font(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24
)

# ==========================
# POSIÇÕES DAS CARTAS
# ==========================
CPU_POS = [(300, 60), (380, 60)]
MESA_POS = [(200 + i * 80, 220) for i in range(5)]
PLAYER_POS = [(300, 420), (380, 420)]

# ==========================
# BOTÕES
# ==========================
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect, border_radius=6)
        txt = FONT_SMALL.render(self.text, True, WHITE)
        screen.blit(
            txt,
            (
                self.rect.centerx - txt.get_width() // 2,
                self.rect.centery - txt.get_height() // 2
            )
        )

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(event.pos)
        )

btn_pass = Button(260, 520, 120, 50, "Passar")
btn_bet  = Button(420, 520, 120, 50, "Apostar")
btn_next = Button(300, 520, 200, 50, "Avançar")

# ==========================
# DESENHO DE CARTA
# ==========================
def draw_card(card, pos):
    pygame.draw.rect(screen, WHITE, (*pos, 60, 90), border_radius=6)
    pygame.draw.rect(screen, BLACK, (*pos, 60, 90), 2, border_radius=6)
    txt = FONT.render(card, True, BLACK)
    screen.blit(
        txt,
        (
            pos[0] + 30 - txt.get_width() // 2,
            pos[1] + 45 - txt.get_height() // 2
        )
    )

# ==========================
# INICIALIZA JOGO
# ==========================
game = TexasHoldemGame()
message = ""

# ==========================
# LOOP PRINCIPAL
# ==========================
running = True
while running:
    clock.tick(FPS)
    screen.fill(GREEN)

    # --------------------------
    # EVENTOS
    # --------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game.fase != "showdown":
            if btn_pass.clicked(event):
                game.avancar_fase()

            if btn_bet.clicked(event):
                game.apostar()
                game.avancar_fase()
        else:
            if btn_next.clicked(event):
                game = TexasHoldemGame()

    # --------------------------
    # CPU (cartas fechadas)
    # --------------------------
    for i, card in enumerate(game.cpu):
        draw_card("??" if game.fase != "showdown" else card, CPU_POS[i])

    # --------------------------
    # MESA
    # --------------------------
    for i, card in enumerate(game.mesa):
        draw_card(card, MESA_POS[i])

    # --------------------------
    # JOGADOR
    # --------------------------
    for i, card in enumerate(game.jogador):
        draw_card(card, PLAYER_POS[i])

    # --------------------------
    # POT
    # --------------------------
    screen.blit(
        FONT_SMALL.render(f"Pot: {game.pote} fichas", True, WHITE),
        (20, 20)
    )

    # ==================================================
    # MÃO ATUAL DO JOGADOR (TEMPO REAL)
    # ==================================================
    cartas_visiveis = game.jogador + game.mesa

    if len(cartas_visiveis) < 5:
        valores = [valor_para_num(c) for c in cartas_visiveis]
        cont = Counter(valores)

        if 2 in cont.values():
            mao_atual = "Par"
        else:
            mao_atual = "Carta Alta"
    else:
        _, _, mao_atual = melhor_mao(cartas_visiveis)

    screen.blit(
        FONT_SMALL.render(f"Sua mão: {mao_atual}", True, YELLOW),
        (WIDTH // 2 - 120, 360)
    )

    # ==================================================
    # SHOWDOWN
    # ==================================================
    if game.fase == "showdown":
        resultado = game.showdown()

        mao_j = resultado["jogador"]
        mao_c = resultado["cpu"]
        vencedor = resultado["vencedor"]

        message = f"Você: {mao_j[2]} | CPU: {mao_c[2]}"
        if vencedor != "Empate":
            message += f"  🏆 Venceu: {vencedor}"
        else:
            message += "  🤝 Empate"

        screen.blit(
            FONT_SMALL.render(message, True, YELLOW),
            (WIDTH // 2 - 250, 400)
        )

    # --------------------------
    # BOTÕES
    # --------------------------
    if game.fase != "showdown":
        btn_pass.draw()
        btn_bet.draw()
    else:
        btn_next.draw()

    pygame.display.flip()
