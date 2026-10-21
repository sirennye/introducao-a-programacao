"""
Ficha 5 · Problema 5.3.10 · Pirâmide Invertida de Quadrados

Adapta a pirâmide do exercício 5.3.9 para desenhar uma pirâmide invertida:
a linha de topo tem 'niveis' quadrados e a linha de base tem 1 quadrado.
"""
import turtle as t


def piramide_invertida(niveis=6, lado=40):
    """Desenha uma pirâmide invertida (base larga no topo, vértice em baixo)."""
    topo = niveis * lado / 2
    for i in range(niveis, 0, -1):
        # i quadrados na linha
        # índice da linha do topo (0) até niveis - 1
        linha_idx = niveis - i
        y = topo - linha_idx * lado
        desenha_linha(i, lado, y)
    t.hideturtle()


def desenha_linha(num_quadrados, lado, y):
    """Desenha uma linha horizontal centrada em x = 0."""
    x_inicial = -num_quadrados * lado / 2
    for j in range(num_quadrados):
        x = x_inicial + j * lado
        desenha_quadrado(x, y, lado)


def desenha_quadrado(x, y, lado):
    """Desenha um quadrado a partir do canto superior esquerdo (x, y)."""
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    for _ in range(4):
        t.forward(lado)
        t.right(90)


if __name__ == '__main__':
    t.speed('fastest')
    piramide_invertida(niveis=6, lado=40)
    t.exitonclick()
