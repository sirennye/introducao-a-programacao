"""
Ficha 3 · Problema 3.3.2 · Custo de viagem Porto - Coimbra (120 km)

Estradas:
  - A1:  0.15 EUR/km combustível + 6.52 EUR portagem
  - A20: 0.12 EUR/km combustível + 15.20 EUR portagem
  - A21: 0.10 EUR/km combustível + 5.75 EUR portagem
"""

DISTANCIA_KM = 120

TABELA_CUSTOS = {
    'A1': {'combustivel': 0.15, 'portagem': 6.52},
    'A20': {'combustivel': 0.12, 'portagem': 15.20},
    'A21': {'combustivel': 0.10, 'portagem': 5.75},
}


def custo_viagem(estrada):
    """Calcula o custo total da viagem (120 km) dada a designação da estrada."""
    estrada_normalizada = estrada.strip().upper()
    if estrada_normalizada not in TABELA_CUSTOS:
        raise ValueError(f"Estrada desconhecida: {estrada}")

    dados = TABELA_CUSTOS[estrada_normalizada]
    custo_comb = DISTANCIA_KM * dados['combustivel']
    return custo_comb + dados['portagem']


if __name__ == '__main__':
    for est in ('A1', 'A20', 'A21'):
        total = custo_viagem(est)
        print(f"Estrada {est}: {total:.2f} EUR")
