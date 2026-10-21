"""
Ficha 5 · Problema 5.3.6 · Espiral de Estrelas

Desenha uma espiral composta por estrelas com tamanho crescente
ou posições rotacionadas progressivamente em redor do centro.
"""
import turtle as t


def desenha_estrela_em(x, y, tamanho, angulo):
    """Desenha uma estrela numa dada posição e rotação."""
    t.up()
    t.goto(x, y)
    t.setheading(angulo)
    t.down()
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)


def espiral_estrelas(quantidade=18, tamanho_inicial=20, passo_tamanho=4, passo_angulo=20):
    """Desenha várias estrelas ao longo de uma espiral."""
    tamanho = tamanho_inicial
    for i in range(quantidade):
        t.up()
        t.goto(0, 0)
        t.setheading(i * passo_angulo)
        t.forward(i * 10)  # afasta do centro
        t.down()
        for _ in range(5):
            t.forward(tamanho)
            t.right(144)
        tamanho += passo_tamanho
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fastest')
    espiral_estrelas()
    t.exitonclick()
