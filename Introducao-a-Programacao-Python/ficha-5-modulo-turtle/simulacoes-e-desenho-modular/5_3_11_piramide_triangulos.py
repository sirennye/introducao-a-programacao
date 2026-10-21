"""
Ficha 5 · Problema 5.3.11 · Pirâmide de Triângulos / Polígonos

Generaliza a pirâmide para suportar polígonos regulares de n_lados
(com triângulos equiláteros: n_lados = 3, ângulo externo = 120 graus).
"""
import turtle as t


def desenha_poligono(x, y, lados, lado):
    """Desenha um polígono regular de n lados a partir de (x, y)."""
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    angulo = 360 / lados
    for _ in range(lados):
        t.forward(lado)
        t.left(angulo)


def piramide_poligonos(niveis=5, lados=3, lado=50):
    """Desenha uma pirâmide com polígonos regulares."""
    altura_linha = lado * 0.866 if lados == 3 else lado  # altura de triângulo equilátero = lado * sqrt(3)/2
    topo = niveis * altura_linha / 2

    for i in range(1, niveis + 1):
        y = topo - (i - 1) * altura_linha
        x_inicial = -i * lado / 2
        for j in range(i):
            x = x_inicial + j * lado
            desenha_poligono(x, y, lados, lado)
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fastest')
    # Pirâmide de triângulos
    piramide_poligonos(niveis=5, lados=3, lado=50)
    t.exitonclick()
