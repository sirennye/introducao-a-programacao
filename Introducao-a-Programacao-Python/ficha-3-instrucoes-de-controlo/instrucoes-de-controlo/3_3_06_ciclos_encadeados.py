"""
Ficha 3 · Problema 3.3.6 · Ciclos encadeados

Código:
    for i in range(3):
        for j in range(1, 3):
            print(i / j)

Justificação:
  - i assume os valores: 0, 1, 2
  - j assume os valores: 1, 2
  - Para i = 0: 0/1 = 0.0, 0/2 = 0.0
  - Para i = 1: 1/1 = 1.0, 1/2 = 0.5
  - Para i = 2: 2/1 = 2.0, 2/2 = 1.0
"""

print("Execução do código de ciclos encadeados:")
for i in range(3):
    for j in range(1, 3):
        print(f"i={i}, j={j} -> i/j = {i / j}")
