"""
Ficha 5 · Problema 5.3.14 · Símbolo dos Jogos Olímpicos

Desenha os 5 anéis entrelaçados nas cores oficiais:
  - Superior: Azul, Preto, Vermelho
  - Inferior: Amarelo, Verde
Construção modular com função desenha_anel.
"""
import turtle as t

ANEIS = [
    # (x, y, cor)
    (-110, 20, 'blue'),
    (0, 20, 'black'),
    (110, 20, 'red'),
    (-55, -30, 'gold'),
    (55, -30, 'forestgreen'),
]


def desenha_anel(x, y, raio, cor, espessura=5):
    """Desenha uma circunferência na posição (x, y)."""
    t.up()
    t.goto(x, y - raio)  # goto posiciona a base inferior do círculo
    t.setheading(0)
    t.color(cor)
    t.width(espessura)
    t.down()
    t.circle(raio)


def aneis_olimpicos(raio=45):
    """Desenha o símbolo oficial dos Jogos Olímpicos."""
    for x, y, cor in ANEIS:
        desenha_anel(x, y, raio, cor)
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fast')
    aneis_olimpicos(45)
    t.exitonclick()
