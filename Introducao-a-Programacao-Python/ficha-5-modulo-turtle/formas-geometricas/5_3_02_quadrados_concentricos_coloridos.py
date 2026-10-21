"""
Ficha 5 · Problema 5.3.2 · Quadrados Concêntricos Coloridos (módulo random)

Semelhante ao anterior, mas cada quadrado é desenhado ou preenchido
com uma cor aleatória do módulo random.
"""
import random
import turtle as t

CORES = ['red', 'blue', 'green', 'orange', 'purple', 'yellow', 'cyan', 'magenta', 'brown']


def desenha_quadrado_colorido(lado, cor):
    """Desenha um quadrado preenchido centrado em (0, 0)."""
    t.up()
    t.goto(-lado / 2, lado / 2)
    t.setheading(0)
    t.color('black', cor)
    t.down()
    t.begin_fill()
    for _ in range(4):
        t.forward(lado)
        t.right(90)
    t.end_fill()


def quadrados_concentricos_coloridos(quantidade, lado_max=240, decremento=35):
    """Desenha quadrados do maior para o menor para que as cores fiquem visíveis."""
    lado = lado_max
    for _ in range(quantidade):
        cor = random.choice(CORES)
        desenha_quadrado_colorido(lado, cor)
        lado -= decremento
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fastest')
    quadrados_concentricos_coloridos(quantidade=6)
    t.exitonclick()
