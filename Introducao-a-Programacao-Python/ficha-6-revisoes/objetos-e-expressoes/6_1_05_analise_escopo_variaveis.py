"""
Ficha 6 · Problema 6.1.5 · Análise de Escopo e Espaço de Nomes

Código analisado:
    def prod(x, y):
        return x * y

    a = 5
    print(prod(a, 3))  # 15
    print(a)           # 5
    print(x)           # NameError: name 'x' is not defined

Explicação rigorosa:
  1. A função prod(x, y) define dois parâmetros formais: x e y.
     Estes parâmetros pertencem ao espaço de nomes local (local scope)
     criado durante a chamada de prod.
  2. Quando a chamada prod(a, 3) termina, o frame da função é destruído
     e as variáveis locais deixam de existir.
  3. No espaço de nomes global (global scope) existe o nome 'a' associado
     ao objeto 5, mas não existe qualquer variável com o nome 'x'.
  4. Por isso, aceder a 'x' no módulo principal gera um NameError.
"""


def prod(x, y):
    """Multiplica dois valores."""
    return x * y


if __name__ == '__main__':
    a = 5
    print("Chamada prod(a, 3) =", prod(a, 3))
    print("Valor de 'a' no escopo global =", a)
    try:
        # Tentativa de acesso à variável local fora do seu escopo:
        # globals()['x'] simula com segurança o acesso a 'x' no escopo global
        print(globals()['x'])
    except KeyError:
        print("Acesso a 'x' no escopo global gera erro: 'x' não existe fora de prod()")

