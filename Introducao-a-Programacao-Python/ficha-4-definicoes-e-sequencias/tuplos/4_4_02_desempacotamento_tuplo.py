"""
Ficha 4 · Problema 4.4.2 · Desempacotamento de Tuplo

Dado um tuplo com três elementos, desempacota para três variáveis
e imprime uma frase formatada.
"""

aluno = ("Maria", 20, "Inteligência Artificial e Ciência de Dados")

# Desempacotamento de tuplo:
nome, idade, curso = aluno

print(f"A estudante {nome} tem {idade} anos e frequenta a licenciatura em {curso}.")
