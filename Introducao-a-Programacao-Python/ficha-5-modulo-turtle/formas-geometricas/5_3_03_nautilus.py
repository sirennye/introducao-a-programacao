"""
Ficha 5 · Problema 5.3.3 · Nautilus de Quadrados

Desenha um efeito de concha nautilus: uma sequência de quadrados com lados
progressivamente maiores e rotações angulares cumulativas a partir do centro (0, 0).
Baseado no código desenvolvido na aula, com documentação limpa.
"""
import turtle as t


def nautilus(quantidade, lado_inicial, aumento, angulo):
    """Desenha uma espiral de quadrados estilo Nautilus."""
    lado = lado_inicial
    for i in range(quantidade):
        t.up()
        t.goto(0, 0)
        t.setheading(i * angulo)
        t.down()
        for _ in range(4):
            t.forward(lado)
            t.right(90)
        lado += aumento
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fastest')
    nautilus(quantidade=20, lado_inicial=20, aumento=8, angulo=10)
    t.exitonclick()
