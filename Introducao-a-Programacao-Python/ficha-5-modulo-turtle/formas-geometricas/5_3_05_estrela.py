"""
Ficha 5 · Problema 5.3.5 · Estrela de cinco pontas

Repete 5 vezes: avançar 100 unidades e rodar à direita 144 graus
(pois 5 * 144 = 720 graus = 2 voltas completas).
"""
import turtle as t


def estrela(tamanho=120, cor='gold'):
    """Desenha uma estrela de 5 pontas preenchida."""
    t.color('darkorange', cor)
    t.begin_fill()
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)
    t.end_fill()
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fast')
    estrela(150)
    t.exitonclick()
