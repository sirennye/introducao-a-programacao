"""
Ficha 2 · Problema 2.2.3 · Nomes válidos

Regras para um nome ser válido:
  - começa por uma letra ou '_';
  - só contém letras, dígitos e '_';
  - não é uma palavra reservada (for, class, if, ...).

No interpretador, um nome inválido provoca SyntaxError.
Aqui usamos str.isidentifier() e keyword.iskeyword() para testar sem erros.
"""
import keyword

nomes = ('abc', 'for', 'minha_altura', '5peso', 'peso$', 'num',
         'peso5', 'peso', 'class', 'num estudante', 'type', 'nome_ALUNO',
         'UmaVariavel', 'a(b)', '12', 'um.dois', 'x', 'Y',
         'área', 'area-rect', 'x___1', 'Indice\\dois', '_x_', 'x_x')

for nome in nomes:
    if nome.isidentifier() and not keyword.iskeyword(nome):
        print(nome, '-> válido')
    else:
        print(nome, '-> inválido')

# Notas:
#  - 'type' é válido, mas não se deve usar: esconde a função type().
#  - 'área' é válido (Python 3 aceita acentos), mas é melhor evitar.
