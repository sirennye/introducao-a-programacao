"""
Ficha 5 · Problema 5.3.12 · Esse Deitado (Curvas com circle)

Desenha uma curva ondulante ("esse deitado") através da junção
de arcos circulares alternados (raio positivo vs raio negativo).
"""
import turtle as t


def esse_deitado(raio=80, arcos=3):
    """Desenha uma forma de 'S' deitado através de arcos de semicircunferência."""
    t.width(3)
    t.color('navy')
    for _ in range(arcos):
        # Semicírculo no sentido anti-horário
        t.circle(raio, 180)
        # Semicírculo no sentido horário (raio negativo)
        t.circle(-raio, 180)
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fast')
    t.up()
    t.goto(-200, 0)
    t.setheading(0)
    t.down()
    esse_deitado(raio=60, arcos=2)
    t.exitonclick()
