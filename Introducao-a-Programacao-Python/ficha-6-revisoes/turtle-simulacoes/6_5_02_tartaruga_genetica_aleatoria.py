"""
Ficha 6 · Problema 6.5.2 · Tartaruga Genética com Variações Aleatórias

Semelhante ao anterior, mas o comprimento de cada avanço/recuo e o valor
de cada rotação variam aleatoriamente dentro de um intervalo razoável.
"""
import random
import turtle as t


def executa_adn_aleatorio(adn):
    """Executa o código genético com amplitudes aleatórias para movimento e rotação."""
    t.width(2)
    t.color('darkmagenta')
    for gene in adn.lower():
        passo = random.randint(15, 60)
        angulo = random.randint(30, 120)
        if gene == 'f':
            t.forward(passo)
        elif gene == 't':
            t.backward(passo)
        elif gene == 'd':
            t.right(angulo)
        elif gene == 'e':
            t.left(angulo)
    t.hideturtle()


if __name__ == '__main__':
    t.speed('fast')
    codigo_adn = 'fdfefftedfeffdffeted'
    executa_adn_aleatorio(codigo_adn)
    t.exitonclick()
