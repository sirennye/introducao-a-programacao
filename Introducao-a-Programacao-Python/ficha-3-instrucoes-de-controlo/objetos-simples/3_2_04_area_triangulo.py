"""
Ficha 3 · Problema 3.2.4 · Área de um triângulo (Fórmula de Heron)

s = (a + b + c) / 2
área = sqrt(s * (s - a) * (s - b) * (s - c))
"""
import math


def area_triangulo(a, b, c):
    """Calcula a área de um triângulo pelos comprimentos dos seus lados."""
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == '__main__':
    lado_a, lado_b, lado_c = 3.0, 4.0, 5.0
    area = area_triangulo(lado_a, lado_b, lado_c)
    print(f"Lados ({lado_a}, {lado_b}, {lado_c}) -> Área: {area:.2f}")
