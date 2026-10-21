"""
Ficha 2 · Problema 2.2.12 · Prémio de um seguro automóvel

Prémio base de 1000 euros com agravamentos, descontos e regras de recusa.
Exemplo: 22 anos, 1 ano de carta, utilitário, 0 acidentes -> 1560.00 euros.
"""

PREMIO_BASE = 1000


def calcula_premio(idade, anos_carta, tipo_veiculo, acidentes):
    """Devolve o prémio a pagar, ou None se o seguro for recusado.

    tipo_veiculo: 1 - Utilitário, 2 - Desportivo, 3 - Luxo
    """
    # Regras de recusa
    if acidentes >= 2:
        return None
    if tipo_veiculo == 2 and idade < 25 and acidentes > 0:
        return None
    if tipo_veiculo == 3 and anos_carta < 5:
        return None

    # Agravamentos (acumulam)
    premio = PREMIO_BASE
    if idade < 25:
        premio = premio * 1.30
    if anos_carta < 2:
        premio = premio * 1.20
    if tipo_veiculo == 2:
        premio = premio * 1.50
    elif tipo_veiculo == 3:
        premio = premio * 1.40
    if acidentes == 1:
        premio = premio * 1.25

    # Desconto para condutores experientes e sem acidentes
    if idade > 30 and acidentes == 0 and anos_carta > 10:
        premio = premio * 0.85

    return premio


if __name__ == '__main__':
    idade = int(input('Idade do condutor: '))
    anos_carta = int(input('Anos com carta: '))
    tipo_veiculo = int(input('Tipo de veículo (1 - Utilitário, 2 - Desportivo, 3 - Luxo): '))
    acidentes = int(input('Número de acidentes: '))

    premio = calcula_premio(idade, anos_carta, tipo_veiculo, acidentes)
    if premio is None:
        print('Seguro Recusado')
    else:
        print(f'Prémio a pagar: {premio:.2f} euros')
