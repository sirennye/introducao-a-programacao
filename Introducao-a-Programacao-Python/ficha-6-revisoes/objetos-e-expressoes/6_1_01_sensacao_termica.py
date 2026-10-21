"""
Ficha 6 · Problema 6.1.1 · Sensação Térmica (Wind Chill)

Fórmula do Wind Chill index:
  tv = 35.4 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
com t em Fahrenheit [-58, 41] e v em milhas/hora.
Exemplo: v = 5, t = 10 -> tv = 1.24
"""


def calcula_sensacao_termica(velocidade_vento, temperatura_f):
    """Calcula a sensação térmica em Fahrenheit."""
    v = velocidade_vento
    t = temperatura_f
    v_fator = v ** 0.16
    tv = 35.4 + 0.6215 * t - 35.75 * v_fator + 0.4275 * t * v_fator
    return tv


if __name__ == '__main__':
    v = 5.0
    t = 10.0
    st = calcula_sensacao_termica(v, t)
    print(f"Para a velocidade do vento {v:.2f} e temperatura exterior {t:.2f}"
          f" a temperatura é sentida como: {st:.2f}")
