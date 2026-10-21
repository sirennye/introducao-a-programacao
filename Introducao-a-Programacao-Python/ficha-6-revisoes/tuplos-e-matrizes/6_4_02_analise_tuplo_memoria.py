"""
Ficha 6 · Problema 6.4.2 · Análise de Memória: t = (1,) * 3

Comando analisado:
    >>> t = (1,) * 3

Explicação clara, sintética e rigorosa:
  1. (1,) cria um objeto tuplo unitário contendo uma referência ao objeto inteiro 1.
  2. O operador '*' sobre sequências (repetição) cria um NOVO tuplo com 3 elementos.
  3. No espaço de objetos, existe apenas UM único objeto inteiro 1 (em Python,
     pequenos inteiros entre -5 e 256 são pré-alocados e reutilizados por interning).
  4. O novo tuplo 't' guarda três referências que apontam todas para o MESMO
     objeto inteiro 1 na memória: id(t[0]) == id(t[1]) == id(t[2]).
  5. No espaço de nomes, o nome 't' passa a apontar para esse novo objeto tuplo.
"""

t = (1,) * 3

print("Valor de t:", t)
print("Tipo de t :", type(t))
print("id do tuplo t:", id(t))
print(f"id(t[0]) = {id(t[0])}")
print(f"id(t[1]) = {id(t[1])}")
print(f"id(t[2]) = {id(t[2])}")
print("Todas as posições referenciam o mesmo objeto?", id(t[0]) == id(t[1]) == id(t[2]))
