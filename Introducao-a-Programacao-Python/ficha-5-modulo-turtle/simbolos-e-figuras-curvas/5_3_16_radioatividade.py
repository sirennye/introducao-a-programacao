"""
Ficha 5 · Problema 5.3.16 · Símbolo de Radioatividade (Trevo Radioativo)

Símbolo de perigo de radiação:
  - Fundo amarelo
  - Círculo central preto
  - 3 pás circulares/setores pretos de 60 graus a 120 graus de intervalo
"""
import turtle as t


def desenha_setor(raio, angulo=60):
    """Desenha um setor circular de raio r e abertura angulo."""
    t.begin_fill()
    t.forward(raio)
    t.left(90)
    t.circle(raio, angulo)
    t.left(90)
    t.forward(raio)
    t.end_fill()


def simbolo_radioatividade(raio_pas=120, raio_centro=25):
    """Desenha o símbolo internacional de aviso de radioatividade."""
    # Fundo circular amarelo
    t.up()
    t.goto(0, -(raio_pas + 30))
    t.setheading(0)
    t.color('black', 'gold')
    t.down()
    t.begin_fill()
    t.circle(raio_pas + 30)
    t.end_fill()

    # 3 pás pretas separadas por 60 graus vazios
    t.color('black', 'black')
    for i in range(3):
        t.up()
        t.goto(0, 0)
        t.setheading(i * 120 + 30)
        t.down()
        desenha_setor(raio_pas, 60)

    # Círculo central preto
    t.up()
    t.goto(0, -raio_centro)
    t.setheading(0)
    t.color('black', 'black')
    t.down()
    t.begin_fill()
    t.circle(raio_centro)
    t.end_fill()

    t.hideturtle()


if __name__ == '__main__':
    t.speed('fastest')
    simbolo_radioatividade()
    t.exitonclick()
