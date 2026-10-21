"""
Ficha 4 · Problema 4.3.4 · Gerador de cadeia de ADN (módulo random)

Utiliza o padrão ciclo-acumulador para gerar uma cadeia de ADN de tamanho n.
Inicialização: adn = ""
Acumulação: adn = adn + base_aleatoria
"""
import random

BASES = ('A', 'T', 'C', 'G')


def gera_adn(tamanho):
    """Gera uma cadeia aleatória de ADN com o comprimento especificado."""
    adn = ""  # string vazia inicial
    for _ in range(tamanho):
        base = random.choice(BASES)
        adn = adn + base  # concatenação no acumulador
    return adn


if __name__ == '__main__':
    random.seed(42)
    for tam in (10, 20, 35):
        print(f"Tamanho {tam:2d}: {gera_adn(tam)}")
