"""
Ficha 5 · Problema 5.3.9 · Pirâmide de Quadrados (Programação Descendente)

Aplica o princípio de dividir para reinar (top-down / programação descendente):
  - piramide: gere as linhas do topo até à base (i de 1 até niveis)
  - desenha_linha: gere a posição horizontal e desenha os 'linha' quadrados
  - desenha_quadrado: desenha um quadrado individual nas coordenadas dadas
"""
import turtle as t


def piramide(niveis=6, lado=40):
    """Desenha uma pirâmide de quadrados usando programação descendente."""
    topo = niveis * lado / 2  # centra verticalmente
    for i in range(1, niveis + 1):
        y = topo - (i - 1) * lado
        desenha_linha(i, lado, y)
    t.hideturtle()


def desenha_linha(num_quadrados, lado, y):
    """Desenha uma linha centrada em x = 0 com num_quadrados."""
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
    piramide(niveis=6, lado=40)
    t.exitonclick()
