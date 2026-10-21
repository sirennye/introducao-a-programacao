"""
Ficha 6 · Problema 6.5.5 · Passeio Aleatório numa Grelha 2D Finita

Um agente move-se num mundo discreto delimitado por uma grelha finita.
A cada passo, escolhe aleatoriamente uma de 4 direções:
  - Norte (y + 1)
  - Sul   (y - 1)
  - Este  (x + 1)
  - Oeste (x - 1)
O agente permanece dentro dos limites da grelha (fronteira rígida).
O ponto inicial é assinalado com um círculo e o final com uma seta.
"""
import random
import turtle as t

DIRECOES = {
    'N': (0, 1, 90),
    'S': (0, -1, 270),
    'E': (1, 0, 0),
    'O': (-1, 0, 180),
}


def desenha_grelha_fundo(n_celulas=10, tam_celula=25):
    """Desenha a grelha de fundo centrada na origem."""
    t.color('lightgray')
    t.width(1)
    metade = n_celulas * tam_celula / 2

    for i in range(n_celulas + 1):
        pos = -metade + i * tam_celula
        # Linha horizontal
        t.up()
        t.goto(-metade, pos)
        t.down()
        t.goto(metade, pos)
        # Linha vertical
        t.up()
        t.goto(pos, -metade)
        t.down()
        t.goto(pos, metade)


def passeio_aleatorio_grelha(passos=80, n_celulas=10, tam_celula=25):
    """Simula o passeio discreto 2D dentro da grelha."""
    desenha_grelha_fundo(n_celulas, tam_celula)

    limite = n_celulas // 2
    # Posição em coordenadas discretas da grelha
    gx, gy = 0, 0

    # Ponto de início (círculo vermelho)
    t.up()
    t.goto(gx * tam_celula, gy * tam_celula)
    t.color('red')
    t.dot(10)

    # Rasto do passeio
    t.down()
    t.color('blue')
    t.width(3)

    for _ in range(passos):
        d_nome, (dx, dy, ang) = random.choice(list(DIRECOES.items()))
        novo_gx = gx + dx
        novo_gy = gy + dy

        # Limite da grelha finita
        if -limite <= novo_gx <= limite and -limite <= novo_gy <= limite:
            gx, gy = novo_gx, novo_gy
            t.setheading(ang)
            t.goto(gx * tam_celula, gy * tam_celula)

    # Ponto final assinalado com forma de tartaruga/seta
    t.color('darkgreen')
    t.shape('classic')
    t.showturtle()


if __name__ == '__main__':
    t.speed('fastest')
    passeio_aleatorio_grelha()
    t.exitonclick()
