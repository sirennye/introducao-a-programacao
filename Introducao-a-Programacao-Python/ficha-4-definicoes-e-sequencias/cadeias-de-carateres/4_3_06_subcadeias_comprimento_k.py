"""
Ficha 4 · Problema 4.3.6 · Sub-cadeias de comprimento k

Dada uma cadeia de caracteres e um número k, imprime todas as sub-cadeias
contíguas de comprimento k (janela deslizante).
Exemplo: 'Monty Python' e k = 3 -> 'Mon', 'ont', 'nty', ...
"""


def subcadeias(texto, k):
    """Gera todas as sub-cadeias de comprimento k de um texto."""
    resultado = []
    for i in range(len(texto) - k + 1):
        resultado.append(texto[i:i + k])
    return resultado


if __name__ == '__main__':
    frase = "Monty Python"
    tamanho = 3
    subs = subcadeias(frase, tamanho)
    print(f"Sub-cadeias de '{frase}' com comprimento {tamanho}:")
    for s in subs:
        print(s)
