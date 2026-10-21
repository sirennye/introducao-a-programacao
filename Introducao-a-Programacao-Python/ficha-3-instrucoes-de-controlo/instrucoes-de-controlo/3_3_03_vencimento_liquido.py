"""
Ficha 3 · Problema 3.3.3 · Vencimento Líquido

Descontos sobre o vencimento bruto:
  - IRS: 25%
  - Segurança Social: 5%
  - Caixa Geral de Aposentações (CGA): 10%
Total de descontos: 40%
Vencimento líquido = Bruto * (1 - 0.40)
"""


def calcula_vencimento_liquido(bruto):
    """Calcula o vencimento líquido a partir do vencimento bruto."""
    desconto_irs = bruto * 0.25
    desconto_ss = bruto * 0.05
    desconto_cga = bruto * 0.10
    total_descontos = desconto_irs + desconto_ss + desconto_cga
    liquido = bruto - total_descontos
    return liquido, total_descontos


if __name__ == '__main__':
    salario_bruto = 2000.0
    liquido, descontos = calcula_vencimento_liquido(salario_bruto)
    print(f"Bruto: {salario_bruto:.2f} EUR")
    print(f"Descontos: {descontos:.2f} EUR")
    print(f"Líquido: {liquido:.2f} EUR")
