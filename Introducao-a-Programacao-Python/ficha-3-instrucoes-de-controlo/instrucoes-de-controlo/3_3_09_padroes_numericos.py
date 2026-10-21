"""
Ficha 3 · Problema 3.3.9 · Padrões numéricos (A, B e C)

Padrão A:
  1
  1 2
  1 2 3
  ...

Padrão B:
  1 2 3 4 5
  1 2 3 4
  1 2 3
  ...

Padrão C:
  1
  2 1
  3 2 1
  ...
"""


def padrao_a(n=5):
    """Imprime o Padrão A até n."""
    print(f"--- Padrão A (n = {n}) ---")
    for i in range(1, n + 1):
        linha = " ".join(str(x) for x in range(1, i + 1))
        print(linha)


def padrao_b(n=5):
    """Imprime o Padrão B até n."""
    print(f"--- Padrão B (n = {n}) ---")
    for i in range(n, 0, -1):
        linha = " ".join(str(x) for x in range(1, i + 1))
        print(linha)


def padrao_c(n=5):
    """Imprime o Padrão C até n."""
    print(f"--- Padrão C (n = {n}) ---")
    for i in range(1, n + 1):
        linha = " ".join(str(x) for x in range(i, 0, -1))
        print(linha)


if __name__ == '__main__':
    padrao_a(5)
    print()
    padrao_b(5)
    print()
    padrao_c(5)
