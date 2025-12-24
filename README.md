# cyber-poker
Texas Hold'em Poker em Python com Pygame e engine própria

# 🂡 Cyber Poker — Texas Hold’em (Python + Pygame)

![OS](https://img.shields.io/badge/OS-Linux-blueviolet.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Build](https://img.shields.io/badge/build-tested%20locally-informational.svg)
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)


Cyber Poker é uma implementação em Python do jogo **Texas Hold’em**, desenvolvida com foco em **arquitetura limpa**, **lógica realista de poker** e **base sólida para evolução futura**, incluindo versão **mobile**.

O projeto separa claramente **engine de jogo**, **avaliação de mãos** e **interface gráfica**, permitindo fácil manutenção, testes e expansão.

Autor: Luciano Valadão

---

## 🎮 Funcionalidades Atuais

- Texas Hold’em Player vs CPU
- Distribuição correta de cartas
- Fases completas do jogo:
  - Pre-Flop
  - Flop
  - Turn
  - River
  - Showdown
#- Sistema de **blinds (small / big blind)** - implementar
#- Sistema de **apostas simples** - implementar
#- Controle de **pote** - implementar
- Avaliação realista das mãos:
  - Carta Alta
  - Par
  - Dois Pares
  - Trinca
  - Sequência
  - Flush
  - Full House
  - Quadra
  - Straight Flush
  - Royal Flush
- **Reconhecimento da mão do jogador em tempo real**, atualizado a cada carta revelada
- Exibição visual clara do vencedor no showdown
- Interface gráfica feita com **Pygame**

---

## 🧠 Arquitetura do Projeto

```

Poker/
├── engine/ │ ├── init.py
│ │
│ ├── cards.py # Baralho, valores e utilidades
│ ├── evaluator.py # Avaliação e comparação de mãos
│ └── game.py # Regras, fases, blinds e apostas
│
├── gui/
│ └── pygame_gui.py # Interface gráfica (Pygame)
│
├── Docs/
│ │
│ ├── LICENSE
│ │
│ └── Docs dos módulos
│
├── mobile/
│
├── venv/
│
├── README.md
│
└── .gitignore

```


### Separação de responsabilidades

- **cards.py**
  Criação e embaralhamento do baralho, conversão de valores.

- **evaluator.py**
  Avaliação precisa de mãos de poker (5 cartas) e comparação entre jogadores.

- **game.py**
  Controle das regras do Texas Hold’em:
  - fases
  - blinds
  - apostas
  - pote
  - showdown

- **pygame_gui.py**
  Interface gráfica, interação do usuário e renderização do jogo.

---

## 🖥️ Requisitos

- Python 3.10+
- pygame

Instalação do pygame:
```
bash
pip install pygame
```
▶️ Como Executar
A partir da pasta raiz do projeto:
```
bash
Copiar código
python3 gui/pygame_gui.py
```
---

🚧 Próximos Passos Planejados
IA básica para decisões da CPU

Sistema completo de fichas (win / lose / rebuy)

Botões de ação:

Check

Call

Raise

Fold

Histórico da mão (hand history)

Animações de cartas

Interface responsiva

Port para mobile (Android / iOS)

Multiplayer local ou online (futuro)
---

🎯 Objetivo do Projeto

Este projeto não é apenas um jogo, mas uma base técnica sólida para:

estudo de lógica de poker

arquitetura de jogos em Python

futuras versões desktop e mobile

expansão para multiplayer

📜 Licença
Apache License 2.0

