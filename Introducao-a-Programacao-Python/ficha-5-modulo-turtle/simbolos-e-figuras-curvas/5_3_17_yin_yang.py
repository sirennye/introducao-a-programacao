"""
Ficha 5 · Problema 5.3.17 · Yin-Yang (Serenidade e Equilíbrio)

Desenha o símbolo taoista Yin-Yang através da combinação modular
de semicírculos e círculos internos preenchidos a preto e branco.
"""
import turtle as t


def yin_yang(raio=140):
    """Desenha o símbolo Yin-Yang clássico."""
    t.width(2)
    t.color('black')

    # Lado direito (preto)
    t.up()
    t.goto(0, -raio)
    t.setheading(0)
    t.down()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(raio, 180)        # semicírculo exterior grande
    t.circle(raio / 2, 180)    # semicírculo médio interior
    t.circle(-raio / 2, 180)   # semicírculo médio inferior invertido
    t.end_fill()

    # Contorno exterior completo (lado branco)
    t.up()
    t.goto(0, -raio)
    t.setheading(0)
    t.down()
    t.circle(raio)

    # Ponto pequeno branco no lado preto (superior)
    t.up()
    t.goto(0, raio / 2 - raio * 0.12)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(raio * 0.12)
    t.end_fill()

    # Ponto pequeno preto no lado branco (inferior)
    t.up()
    t.goto(0, -raio / 2 - raio * 0.12)
    t.fillcolor('black')
    t.begin_fill()
    t.circle(raio * 0.12)
    t.end_fill()

    t.hideturtle()


if __name__ == '__main__':
    t.speed('fast')
    yin_yang(140)
    t.exitonclick()
