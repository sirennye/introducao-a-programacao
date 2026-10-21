"""
Ficha 3 · Problema 3.2.3 · Conversão de Moeda (Euros para Dólares)

Converte um montante em euros para dólares dada a taxa de câmbio.
A solução genérica é parametrizar quer o montante quer a taxa numa função.
"""


def euros_para_dolares(euros, taxa_cambio=1.08):
    """Converte euros para dólares com base numa taxa de câmbio."""
    return euros * taxa_cambio


if __name__ == '__main__':
    quantia_eur = 150.0
    taxa = 1.085
    quantia_usd = euros_para_dolares(quantia_eur, taxa)
    print(f"{quantia_eur:.2f} EUR com taxa {taxa} = {quantia_usd:.2f} USD")
