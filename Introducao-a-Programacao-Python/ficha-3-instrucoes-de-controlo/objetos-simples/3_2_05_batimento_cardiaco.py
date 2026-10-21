"""
Ficha 3 · Problema 3.2.5 · Batimento Cardíaco Máximo Médio

Fórmula empírica: 163 + 1.16 * idade - 0.018 * idade^2
"""


def batimento_cardiaco_maximo(idade):
    """Calcula o valor médio do batimento cardíaco máximo dada a idade."""
    return 163 + 1.16 * idade - 0.018 * (idade ** 2)


if __name__ == '__main__':
    for idade in (20, 30, 45, 60):
        fc_max = batimento_cardiaco_maximo(idade)
        print(f"Idade: {idade} anos -> FC Máxima estimada: {fc_max:.1f} bpm")
