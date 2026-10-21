"""
Ficha 6 · Problema 6.1.3 · Energia térmica necessária para aquecer água

Fórmula: E = m * (tf - ti) * 4184
onde E é a energia em Joules, m a massa de água em kg e ti/tf as temperaturas em Celsius.
Exemplo: ti = 10, tf = 30, m = 25 kg -> E = 2092000.00 Joules
"""


def energia_aquecimento_agua(massa_kg, temp_inicial, temp_final):
    """Calcula a energia térmica em Joules necessária para variar a temperatura da água."""
    delta_t = abs(temp_final - temp_inicial)
    return massa_kg * delta_t * 4184


if __name__ == '__main__':
    m = 25.0
    ti = 10.0
    tf = 30.0
    energia = energia_aquecimento_agua(m, ti, tf)
    print(f"Para a massa de água {m:.2f} kg, temperatura inicial {ti:.2f} ºC "
          f"e temperatura final {tf:.2f} ºC a energia necessária é: {energia:.2f} Joules.")
