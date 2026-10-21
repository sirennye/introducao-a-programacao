"""
Ficha 6 · Problema 6.1.2 · Comprimento mínimo da pista de descolagem

Fórmula física: c = v^2 / (2 * a)
onde v é a velocidade de descolagem (m/s) e a é a aceleração (m/s^2).
Exemplo: v = 50 m/s, a = 4.5 m/s^2 -> c = 277.78 m
"""


def comprimento_pista(velocidade, aceleracao):
    """Calcula o comprimento mínimo da pista de descolagem em metros."""
    if aceleracao <= 0:
        raise ValueError("A aceleração deve ser positiva.")
    return (velocidade ** 2) / (2 * aceleracao)


if __name__ == '__main__':
    v = 50.0
    a = 4.5
    comp = comprimento_pista(v, a)
    print(f"Para a velocidade {v:.2f} m/s e aceleração {a:.2f} m/s² "
          f"o comprimento mínimo da pista é: {comp:.2f} metros.")
