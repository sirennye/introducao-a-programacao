"""
Ficha 3 · Problema 3.2.2 · Volume de uma esfera (módulo math)

V = 4/3 * pi * r^3
"""
import math


def volume_esfera(raio):
    """Calcula o volume de uma esfera de raio r."""
    return (4 / 3) * math.pi * (raio ** 3)


if __name__ == '__main__':
    r = 5.0
    vol = volume_esfera(r)
    print(f"Raio: {r} -> Volume da esfera: {vol:.4f}")
