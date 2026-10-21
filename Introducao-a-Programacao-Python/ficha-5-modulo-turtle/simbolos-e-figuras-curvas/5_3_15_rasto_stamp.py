"""
Ficha 5 · Problema 5.3.15 · Deixar Rasto com stamp()

O comando turtle.stamp() carimba uma impressão da forma da tartaruga no ecrã.
Desenha um mostrador circular / espiral de impressões da tartaruga.
"""
import turtle as t


def mostrador_relogio_stamp(raio=140, num_marcas=12):
    """Cria um anel com num_marcas usando a primitiva stamp()."""
    t.shape('turtle')
    t.color('darkcyan')
    t.up()
    for i in range(num_marcas):
        t.goto(0, 0)
        t.setheading(i * (360 / num_marcas))
        t.forward(raio)
        t.stamp()
    t.goto(0, 0)
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fast')
    mostrador_relogio_stamp()
    t.exitonclick()
