"""
Ficha 3 · Problema 3.3.4 · Avaliação na Cadeira

Nota = 0.075 * (t1 + t2 + t3 + t4) + 0.70 * exame
Classificação:
  - nota >= 14: "Aprovado"
  - 7 <= nota < 14: "Oral"
  - nota < 7: "Reprovado"
"""


def avalia_aluno(t1, t2, t3, t4, exame):
    """Calcula a nota final ponderada e a situação académica."""
    nota_final = 0.075 * (t1 + t2 + t3 + t4) + 0.70 * exame
    if nota_final >= 14.0:
        situacao = "Aprovado"
    elif nota_final >= 7.0:
        situacao = "Oral"
    else:
        situacao = "Reprovado"
    return nota_final, situacao


if __name__ == '__main__':
    casos = [
        (15, 16, 14, 15, 16),
        (10, 12, 8, 10, 10),
        (5, 6, 4, 5, 6),
    ]
    for caso in casos:
        nota, sit = avalia_aluno(*caso)
        print(f"Testes {caso[:4]} + Exame {caso[4]} -> Nota: {nota:.2f} ({sit})")
