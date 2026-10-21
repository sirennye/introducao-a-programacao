"""
Ficha 5 · Problema 5.3.8 · Uma Casa Portuguesa (Desenho Modular)

Desenha uma casa típica de forma modular e reutilizável:
  - corpo principal: retângulo/quadrado
  - telhado: triângulo no topo
  - porta: retângulo
  - janelas: quadrados com cruz no interior
"""
import turtle as t


def desenha_retangulo(x, y, largura, altura, cor_preenchimento=None, cor_linha='black'):
    """Desenha um retângulo alinhado a partir do canto inferior esquerdo (x, y)."""
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.color(cor_linha)
    if cor_preenchimento:
        t.fillcolor(cor_preenchimento)
        t.begin_fill()
    t.down()
    for _ in range(2):
        t.forward(largura)
        t.left(90)
        t.forward(altura)
        t.left(90)
    if cor_preenchimento:
        t.end_fill()


def desenha_telhado(x, y, base, altura, cor='firebrick'):
    """Desenha um telhado triangular sobre a casa."""
    t.up()
    t.goto(x, y)
    t.color('black', cor)
    t.down()
    t.begin_fill()
    t.goto(x + base / 2, y + altura)
    t.goto(x + base, y)
    t.goto(x, y)
    t.end_fill()


def desenha_janela(x, y, lado):
    """Desenha uma janela quadrada com divisórias em cruz."""
    desenha_retangulo(x, y, lado, lado, cor_preenchimento='lightcyan')
    # Divisória vertical
    t.up()
    t.goto(x + lado / 2, y)
    t.down()
    t.goto(x + lado / 2, y + lado)
    # Divisória horizontal
    t.up()
    t.goto(x, y + lado / 2)
    t.down()
    t.goto(x + lado, y + lado / 2)


def casa_portuguesa():
    """Compõe a casa modularmente."""
    # Corpo da casa
    desenha_retangulo(-100, -80, 200, 140, cor_preenchimento='beige')
    # Telhado
    desenha_telhado(-110, 60, 220, 70, cor='brown')
    # Porta
    desenha_retangulo(-25, -80, 50, 80, cor_preenchimento='chocolate')
    # Janelas
    desenha_janela(-80, -10, 40)
    desenha_janela(40, -10, 40)
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fast')
    casa_portuguesa()
    t.exitonclick()
