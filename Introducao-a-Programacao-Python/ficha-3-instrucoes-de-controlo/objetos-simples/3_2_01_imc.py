"""
Ficha 3 · Problema 3.2.1 · Índice de Massa Corporal (IMC)

IMC = peso (kg) / altura^2 (m^2)
Mantendo a altura fixa, o IMC varia linearmente com o peso.
Mantendo o peso fixo, o IMC varia inversamente com o quadrado da altura.
"""


def calcula_imc(peso, altura):
    """Calcula o Índice de Massa Corporal."""
    return peso / (altura ** 2)


if __name__ == '__main__':
    peso = 70.0    # em kg
    altura = 1.75  # em metros
    imc = calcula_imc(peso, altura)
    print(f"Peso: {peso} kg, Altura: {altura} m -> IMC: {imc:.2f}")
