"""
Ficha 6 · Problema 6.5.3 · Tartaruga com ADN e Movimento Aleatórios

O código genético da tartaruga é gerado aleatoriamente a partir do alfabeto
{'f', 't', 'd', 'e'} com base no comprimento pretendido, e depois executado.
"""
import random
import turtle as t

GENES = ('f', 't', 'd', 'e')


def gera_adn_aleatorio(comprimento):
    """Gera uma cadeia de ADN aleatória de tamanho n."""
    return "".join(random.choice(GENES) for _ in range(comprimento))


def simula_tartaruga_adn(comprimento_adn=50):
    """Gera o ADN e executa a simulação."""
    adn = gera_adn_aleatorio(comprimento_adn)
    print("ADN gerado:", adn)

    t.width(2)
    t.color('navy')
    for gene in adn:
        passo = random.randint(15, 45)
        angulo = random.choice([45, 90, 135])
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
    t.speed('fastest')
    simula_tartaruga_adn(60)
    t.exitonclick()
