"""
Ficha 6 · Problema 6.2.5 · Estimativa da evolução populacional

Entradas:
  - Frequência de nascimentos (em minutos): 1 nascimento a cada N minutos
  - Frequência de mortes (em minutos): 1 óbito a cada M minutos
  - Frequência de emigrantes (em minutos): 1 emigrante a cada E minutos
  - População inicial
  - Número de anos (ano = 365 dias = 365 * 24 * 60 minutos)

Exemplo: freq_nasc=20, freq_mortes=15, freq_emig=10, pop=10000000
Em 365 dias: minutos = 525600
  nascimentos = 525600 // 20 = 26280
  mortes = 525600 // 15 = 35040
  emigrantes = 525600 // 10 = 52560
  pop_final = 10000000 + 26280 - 35040 - 52560 = 9938680
"""

MINUTOS_POR_ANO = 365 * 24 * 60  # 525600 minutos


def estima_populacao(pop_inicial, freq_nasc, freq_mortes, freq_emig, anos=1):
    """Calcula a estimativa populacional ao fim de um determinado número de anos."""
    minutos_totais = anos * MINUTOS_POR_ANO
    nascimentos = minutos_totais // freq_nasc
    mortes = minutos_totais // freq_mortes
    emigrantes = minutos_totais // freq_emig
    pop_final = pop_inicial + nascimentos - mortes - emigrantes
    return pop_final


if __name__ == '__main__':
    p_ini = 10000000
    fn, fm, fe = 20, 15, 10
    print("Resumo dos dados:")
    print("-----------------")
    print(f"Frequência de nascimentos : {fn} min")
    print(f"Frequência de mortes      : {fm} min")
    print(f"Frequência de emigrantes  : {fe} min")
    print(f"População Inicial         : {p_ini}")
    print("Estimativa:")
    print("-----------")
    p_1ano = estima_populacao(p_ini, fn, fm, fe, anos=1)
    p_5anos = estima_populacao(p_ini, fn, fm, fe, anos=5)
    print(f"A população ao fim de um ano: {p_1ano}")
    print(f"A população ao fim de 5 anos: {p_5anos}")
