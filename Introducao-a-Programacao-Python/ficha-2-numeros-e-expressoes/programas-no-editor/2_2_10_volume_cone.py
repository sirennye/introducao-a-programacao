"""
Ficha 2 · Problema 2.2.10 · Volume de um cone (módulo math)

V = (pi * r^2 * h) / 3, com r = 90 cm e h = 1.5 m.
"""
import math

raio = 0.90    # 90 cm convertidos para metros
altura = 1.5   # metros

volume = math.pi * raio ** 2 * altura / 3
print(f'Volume do cone: {volume:.4f} m³')
