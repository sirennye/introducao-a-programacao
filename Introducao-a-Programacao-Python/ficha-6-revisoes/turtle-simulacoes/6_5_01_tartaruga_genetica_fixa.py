"""
Ficha 6 · Problema 6.5.1 · Tartaruga Genética (Valores Constantes)

Código genético baseado num alfabeto de 4 letras:
  - 'f': avança em frente (passo constante)
  - 't': recua para trás (passo constante)
  - 'd': roda à direita (ângulo constante)
  - 'e': roda à esquerda (ângulo constante)

Exemplo: ADN 'feftd'
"""
import turtle as t


def executa_adn(adn, passo=40, angulo=90):
    """Executa o código genético da tartaruga com passos e ângulos fixos."""
    t.width(2)
    t.color('teal')
    for gene in adn.lower():
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
    codigo_adn = 'feftdffffdffeedffff'
    executa_adn(codigo_adn, passo=30, angulo=90)
    t.exitonclick()
