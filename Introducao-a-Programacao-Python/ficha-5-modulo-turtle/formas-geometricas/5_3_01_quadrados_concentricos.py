"""
Ficha 5 · Problema 5.3.1 · Quadrados Concêntricos

Desenha n quadrados concêntricos centrados na origem (0, 0).
A cada novo quadrado o lado aumenta e a posição inicial (canto superior esquerdo)
recua metade do aumento em x e avança metade em y para manter o centro.
"""
import turtle as t


def desenha_quadrado_centrado(lado):
    """Desenha um quadrado centrado em (0, 0)."""
    t.up()
    t.goto(-lado / 2, lado / 2)  # canto superior esquerdo
    t.setheading(0)
    t.down()
    for _ in range(4):
        t.forward(lado)
        t.right(90)


def quadrados_concentricos(quantidade, lado_inicial=40, incremento=30):
    """Desenha uma sequência de quadrados concêntricos."""
    lado = lado_inicial
    for _ in range(quantidade):
        desenha_quadrado_centrado(lado)
        lado += incremento
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fastest')
    quadrados_concentricos(quantidade=6, lado_inicial=40, incremento=30)
    t.exitonclick()
