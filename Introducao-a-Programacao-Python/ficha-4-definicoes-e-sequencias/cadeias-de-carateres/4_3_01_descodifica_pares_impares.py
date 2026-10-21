"""
Ficha 4 · Problema 4.3.1 · Descodificar separação de pares e ímpares

Codificação:
  Original: "EXEMPLO" (índices 0..6)
  Pares: E (0), E (2), P (4), O (6)
  Ímpares: X (1), M (3), L (5)
  Codificado = Ímpares + Pares = "XMLEEPO"

Descodificação:
  Se tamanho for N:
    n_impares = N // 2
    impares = codificado[:n_impares]
    pares = codificado[n_impares:]
  Reconstrução alternada: par[0], impar[0], par[1], impar[1], ...
"""


def codifica_pares_impares(texto):
    """Separa caracteres em posições ímpares e pares e junta-os."""
    pares = texto[0::2]
    impares = texto[1::2]
    return impares + pares


def descodifica_pares_impares(codificado):
    """Reconstrói o texto original a partir da cadeia codificada."""
    n = len(codificado)
    n_impares = n // 2
    impares = codificado[:n_impares]
    pares = codificado[n_impares:]

    original = []
    for i in range(len(pares)):
        original.append(pares[i])
        if i < len(impares):
            original.append(impares[i])
    return "".join(original)


if __name__ == '__main__':
    msg = "EXEMPLO"
    cod = codifica_pares_impares(msg)
    des = descodifica_pares_impares(cod)
    print(f"Original: '{msg}' -> Codificado: '{cod}' -> Descodificado: '{des}'")
