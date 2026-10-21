"""
Ficha 3 · Problema 3.3.5 · Converter ciclo while para ciclo for

Código original:
    i = 20
    while i >= 0:
        print("i =", i)
        i = i - 2
"""

print("--- Versão while original ---")
i = 20
while i >= 0:
    print("i =", i)
    i = i - 2

print("\n--- Versão for equivalente ---")
# range(start, stop, step): 20 até 0 inclusive com passo -2
for i in range(20, -1, -2):
    print("i =", i)
