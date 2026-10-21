"""
Ficha 5 · Problema 5.3.7 · Passeio Aleatório (Random Walk)

A tartaruga dá passos de comprimento fixo ou variável com ângulos aleatórios,
mudando a cor da caneta a cada passo de forma aleatória.
"""
import random
import turtle as t

CORES = ['red', 'blue', 'green', 'orange', 'purple', 'magenta', 'turquoise', 'brown']


def passeio_aleatorio(passos=120, distancia=25):
    """Simula um passeio aleatório (random walk) da tartaruga."""
    t.width(2)
    for _ in range(passos):
        t.color(random.choice(CORES))
        angulo = random.choice([0, 45, 90, 135, 180, 225, 270, 315])
        t.right(angulo)
        t.forward(distancia)
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fastest')
    passeio_aleatorio()
    t.exitonclick()
