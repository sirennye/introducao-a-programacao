"""
Ficha 5 · Problema 5.3.13 · Cara Sorridente (Smiley)

Utiliza o método circle para desenhar:
  - Rosto circular amarelo
  - Olhos circulares
  - Sorriso em arco
"""
import turtle as t


def desenha_circulo_cheio(x, y, raio, cor_linha, cor_fundo):
    """Desenha um círculo preenchido centrado na base (x, y)."""
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.color(cor_linha, cor_fundo)
    t.down()
    t.begin_fill()
    t.circle(raio)
    t.end_fill()


def smiley(raio=100):
    """Desenha um emoji sorridente clássico."""
    # Rosto
    desenha_circulo_cheio(0, -raio, raio, 'gold', 'yellow')

    # Olho esquerdo
    desenha_circulo_cheio(-raio * 0.35, raio * 0.20, raio * 0.12, 'black', 'black')

    # Olho direito
    desenha_circulo_cheio(raio * 0.35, raio * 0.20, raio * 0.12, 'black', 'black')

    # Sorriso: semicírculo
    t.up()
    t.goto(-raio * 0.55, -raio * 0.10)
    t.setheading(-60)
    t.width(4)
    t.color('black')
    t.down()
    t.circle(raio * 0.65, 120)

    t.hideturtle()


if __name__ == '__main__':
    t.speed('fast')
    smiley(120)
    t.exitonclick()
