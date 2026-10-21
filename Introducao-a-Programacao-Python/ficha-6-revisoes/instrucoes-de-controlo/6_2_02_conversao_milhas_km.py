"""
Ficha 6 · Problema 6.2.2 · Tabela de conversão de Milhas para Quilómetros

Fator: 1 milha = 1.609 km
Gera uma tabela formatada entre dois valores de referência.
"""

KM_POR_MILHA = 1.609


def tabela_milhas_km(inicio=10, fim=20):
    """Imprime uma tabela de conversão formatada de milhas para quilómetros."""
    print("Milhas      Quilómetros")
    print("------------------------")
    for milha in range(inicio, fim + 1):
        km = milha * KM_POR_MILHA
        print(f"{milha:5.2f}       {km:6.2f}")


if __name__ == '__main__':
    tabela_milhas_km(10, 20)
