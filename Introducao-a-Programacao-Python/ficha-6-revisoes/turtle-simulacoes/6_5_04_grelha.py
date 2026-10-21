"""
Ficha 6 · Problema 6.5.4 · Desenho de uma Grelha Parametrizável

Desenha uma grelha retangular/quadrada onde o número de linhas,
o número de colunas e o tamanho de cada célula são parâmetros.
"""
import turtle as t


def desenha_grelha(linhas=8, colunas=8, tamanho_celula=30, x_inicial=-120, y_inicial=120):
    """Desenha uma grelha de células quadradas alinhadas."""
    t.color('gray')
    largura_total = colunas * tamanho_celula
    altura_total = linhas * tamanho_celula

    # Desenha linhas horizontais
    for i in range(linhas + 1):
        y = y_inicial - i * tamanho_celula
        t.up()
        t.goto(x_inicial, y)
        t.setheading(0)
        t.down()
        t.forward(largura_total)

    # Desenha linhas verticais
    for j in range(colunas + 1):
        x = x_inicial + j * tamanho_celula
        t.up()
        t.goto(x, y_inicial)
        t.setheading(270)
        t.down()
        t.forward(altura_total)

    t.hideturtle()


if __name__ == '__main__':
    t.speed('fastest')
    desenha_grelha(linhas=6, colunas=6, tamanho_celula=40)
    t.exitonclick()
