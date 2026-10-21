"""
Ficha 5 · Problema 5.3.4 · Hexágono Fatiado

Desenha um hexágono regular composto por 6 fatias triangulares equiláteras
que partem do centro (0, 0).
Baseado no código desenvolvido na aula, com documentação e clareza.
"""
import turtle as t


def hexagono_fatiado(lado):
    """Desenha um hexágono composto por 6 triângulos equiláteros a partir do centro."""
    for i in range(6):
        # Prepara: regressa ao centro e roda para a fatia seguinte (60 graus cada)
        t.up()
        t.goto(0, 0)
        t.setheading(i * 60)
        t.down()
        # Desenha triângulo equilátero (ângulos externos de 120 graus)
        for _ in range(3):
            t.forward(lado)
            t.right(120)
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fast')
    hexagono_fatiado(100)
    t.exitonclick()
