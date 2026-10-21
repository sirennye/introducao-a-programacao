# Introdução à Programação — Python Exercises

> **GitHub Repository Description:**  
> *Códigos em Python feitos para estudar Introdução à Programação no curso de Artificial Intelligence and Data Science — University of Coimbra.*

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![University of Coimbra](https://img.shields.io/badge/UC-FCTUC%20%2F%20DEI-red.svg)](https://www.uc.pt/fctuc/dei/)

This repository contains clean, modular, and thoroughly documented Python solutions for the exercise problem sets (**Fichas 2 through 6**) of the **Introdução à Programação (IP)** course in the Bachelor's in **Artificial Intelligence and Data Science** (Licenciatura em Inteligência Artificial e Ciência de Dados) at the **University of Coimbra (DEI / FCTUC)**.

---

## 📂 Repository Structure

All exercise scripts are grouped into descriptive directories inside [Introducao-a-Programacao-Python](Introducao-a-Programacao-Python/) categorized by worksheet and functional topic:

```text
.
├── README.md
└── Introducao-a-Programacao-Python/
    ├── ficha-2-numeros-e-expressoes/
    │   ├── explorar-o-interpretador/
    │   │   ├── 2_2_01_identidade_valor_tipo.py
    │   │   ├── 2_2_03_nomes_validos.py
    │   │   ├── 2_2_04_maiusculas_e_minusculas.py
    │   │   ├── 2_2_05_tipos_dos_valores.py
    │   │   ├── 2_2_06_precedencia_de_operadores.py
    │   │   ├── 2_2_07_traduzir_expressoes.py
    │   │   └── 2_2_08_tipos_dos_resultados.py
    │   └── programas-no-editor/
    │       ├── 2_2_09_polinomio.py
    │       ├── 2_2_10_volume_cone.py
    │       ├── 2_2_11_celsius_para_fahrenheit.py
    │       └── 2_2_12_seguro_automovel.py
    ├── ficha-3-instrucoes-de-controlo/
    │   ├── objetos-simples/
    │   │   ├── 3_2_01_imc.py
    │   │   ├── 3_2_02_volume_esfera.py
    │   │   ├── 3_2_03_cambio_moeda.py
    │   │   ├── 3_2_04_area_triangulo.py
    │   │   └── 3_2_05_batimento_cardiaco.py
    │   └── instrucoes-de-controlo/
    │       ├── 3_3_01_ordenar_tres_numeros.py
    │       ├── 3_3_02_custo_viagem_porto_coimbra.py
    │       ├── 3_3_03_vencimento_liquido.py
    │       ├── 3_3_04_avaliacao_cadeira.py
    │       ├── 3_3_05_while_para_for.py
    │       ├── 3_3_06_ciclos_encadeados.py
    │       ├── 3_3_07_aproximacao_euler.py
    │       ├── 3_3_08_lancamento_dado.py
    │       ├── 3_3_09_padroes_numericos.py
    │       └── 3_3_10_pertence_fibonacci.py
    ├── ficha-4-definicoes-e-sequencias/
    │   ├── cadeias-de-carateres/
    │   │   ├── 4_3_01_descodifica_pares_impares.py
    │   │   ├── 4_3_02_cifra_substituicao.py
    │   │   ├── 4_3_03_complementar_adn.py
    │   │   ├── 4_3_04_gerador_adn.py
    │   │   ├── 4_3_05_substitui_vogais.py
    │   │   ├── 4_3_06_subcadeias_comprimento_k.py
    │   │   ├── 4_3_07_prefixos.py
    │   │   ├── 4_3_08_sufixos.py
    │   │   ├── 4_3_09_palavras_amigas.py
    │   │   └── 4_3_10_cifra_cesar.py
    │   └── tuplos/
    │       ├── 4_4_01_uniao_tuplos.py
    │       ├── 4_4_02_desempacotamento_tuplo.py
    │       ├── 4_4_03_filtrar_pares.py
    │       ├── 4_4_04_intercalar_tuplos.py
    │       └── 4_4_05_achatar_tuplo_recursivo.py
    ├── ficha-5-modulo-turtle/
    │   ├── formas-geometricas/
    │   │   ├── 5_3_01_quadrados_concentricos.py
    │   │   ├── 5_3_02_quadrados_concentricos_coloridos.py
    │   │   ├── 5_3_03_nautilus.py
    │   │   ├── 5_3_04_hexagono_fatiado.py
    │   │   ├── 5_3_05_estrela.py
    │   │   └── 5_3_06_espiral_estrelas.py
    │   ├── simulacoes-e-desenho-modular/
    │   │   ├── 5_3_07_passeio_aleatorio.py
    │   │   ├── 5_3_08_casa_portuguesa.py
    │   │   ├── 5_3_09_piramide_quadrados.py
    │   │   ├── 5_3_10_piramide_invertida.py
    │   │   └── 5_3_11_piramide_triangulos.py
    │   └── simbolos-e-figuras-curvas/
    │       ├── 5_3_12_esse_deitado.py
    │       ├── 5_3_13_smiley.py
    │       ├── 5_3_14_jogos_olimpicos.py
    │       ├── 5_3_15_rasto_stamp.py
    │       ├── 5_3_16_radioatividade.py
    │       └── 5_3_17_yin_yang.py
    └── ficha-6-revisoes/
        ├── objetos-e-expressoes/
        │   ├── 6_1_01_sensacao_termica.py
        │   ├── 6_1_02_pista_aviao.py
        │   ├── 6_1_03_energia_aquecimento_agua.py
        │   ├── 6_1_04_analise_add2me.py
        │   └── 6_1_05_analise_escopo_variaveis.py
        ├── instrucoes-de-controlo/
        │   ├── 6_2_01_fatorial.py
        │   ├── 6_2_02_conversao_milhas_km.py
        │   ├── 6_2_03_tabela_quadrados.py
        │   ├── 6_2_04_tabuada.py
        │   └── 6_2_05_estimativa_populacional.py
        ├── cadeias-de-carateres/
        │   ├── 6_3_01_acronimo.py
        │   ├── 6_3_02_compressao_caracteres.py
        │   ├── 6_3_03_parenteses_validos.py
        │   ├── 6_3_04_anagramas.py
        │   ├── 6_3_05_substitui_manual.py
        │   └── 6_3_06_maior_subcadeia_unica.py
        ├── tuplos-e-matrizes/
        │   ├── 6_4_01_imprime_matriz_posicoes.py
        │   ├── 6_4_02_analise_tuplo_memoria.py
        │   ├── 6_4_03_intercala_ordenados.py
        │   ├── 6_4_04_compacta_intervalos.py
        │   ├── 6_4_05_pontos_de_sela.py
        │   └── 6_4_06_agrupa_por_vogais.py
        └── turtle-simulacoes/
            ├── 6_5_01_tartaruga_genetica_fixa.py
            ├── 6_5_02_tartaruga_genetica_aleatoria.py
            ├── 6_5_03_tartaruga_adn_aleatorio.py
            ├── 6_5_04_grelha.py
            └── 6_5_05_passeio_aleatorio_grelha.py
```

---

## 📘 Worksheets Overview & Key Concepts

### [Ficha 2 — Números e Expressões](Introducao-a-Programacao-Python/ficha-2-numeros-e-expressoes/)
Focuses on Python fundamentals:
- **Object Model**: Identity (`id()`), Value, and Type (`type()`).
- **Naming & Scope**: Valid identifiers (`isidentifier`), reserved keywords (`keyword`), case sensitivity.
- **Arithmetic & Precedence**: Binary operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`), unary operators, and floating-point vs. integer division semantics.
- **Real-world Modeling**: Polynomial evaluation, cone volume using `math.pi`, temperature conversion (`Celsius <-> Fahrenheit`), and a comprehensive car insurance calculator with conditional surcharges and refusal rules.

### [Ficha 3 — Instruções de Controlo](Introducao-a-Programacao-Python/ficha-3-instrucoes-de-controlo/)
Focuses on flow control and algorithm design:
- **Functions & Math**: BMI calculation, sphere volume, currency conversion, Heron's formula for triangle areas, and empirical maximum heart rate models.
- **Decision Trees**: Optimal sorting of 3 numbers minimizing comparisons ($\le 3$ comparisons without built-in sort).
- **Financial Calculations**: Route cost evaluation (Porto-Coimbra), progressive/flat net salary taxation (IRS, SS, CGA), and grading systems.
- **Loops & Series**: Conversion of `while` to `for` loops, nested loops analysis, Taylor series approximation of Euler's constant $e = \sum \frac{1}{i!}$, Monte Carlo dice rolling simulation, numeric pyramids, and Fibonacci membership tests.

### [Ficha 4 — Definições e Sequências (Strings & Tuplos)](Introducao-a-Programacao-Python/ficha-4-definicoes-e-sequencias/)
Explores immutable sequences and function abstraction:
- **String Manipulation & Ciphers**:
  - Even/odd index split decoding (`XMLEEPO` $\rightarrow$ `EXEMPLO`).
  - Substitution ciphers and Caesar ciphers with circular modular arithmetic (`% 26`).
  - DNA complementary strands and random sequence generator using the cycle-accumulator pattern.
  - Vowel removal, sliding-window substrings of length $k$, prefixes, suffixes, and friendly words ($< 10\%$ character differences).
- **Tuples**:
  - Concatenation, unpacking, filtering even integers into new tuples.
  - Alternating interleaving of equal-sized tuples.
  - Recursive arbitrary nested tuple flattening (`achatar_tuplo`).

### [Ficha 5 — Módulo Turtle](Introducao-a-Programacao-Python/ficha-5-modulo-turtle/)
Hands-on graphical programming with Python's standard `turtle` module:
- **Geometric Shapes**: Concentric squares (both monochrome and randomly colored), square nautilus spirals, sliced hexagons, 5-pointed stars, and star spirals.
- **Modular Top-Down Design**:
  - Random walks with randomized colors.
  - Traditional Portuguese house composed of modular rectangular, triangular, and window primitives.
  - Top-down pyramid construction (`piramide` $\rightarrow$ `desenha_linha` $\rightarrow$ `desenha_quadrado`), inverted pyramids, and regular polygon pyramids.
- **Curved Figures & Symbols**:
  - Wave S-curves with alternating positive/negative radii.
  - Smiley face using coordinate-relative circles.
  - Official Olympic 5-ring interlocking logo.
  - Footprint/clock face stamp trail (`turtle.stamp()`).
  - Radioactivity hazard trefoil symbol.
  - Taoist Yin-Yang symbol with interlocking semicircular fills.

### [Ficha 6 — Revisões Gerais](Introducao-a-Programacao-Python/ficha-6-revisoes/)
Comprehensive synthesis covering all semester themes:
- **Objects & Expressions**: Wind chill sensation, runway takeoff distances, thermodynamic water heating energy, operator polymorphism (`+` with floats vs strings), and local vs global namespace scoping analysis (`NameError`).
- **Control Flow**: Custom factorial, miles-to-km conversion tables, variable-row square tables, multiplication tables, and demographic population evolution models.
- **Advanced Strings**: Acronym generator with stopword handling and conventions (`Universidade de Coimbra` $\rightarrow$ `UC`, `Artificial Intelligence and Data Science` $\rightarrow$ `AIDTS`), run-length consecutive character compression, balanced parentheses validator (`parenteses_validos`), anagram detection, manual string replacement without `str.replace()`, and longest unique non-repeating substring search.
- **Matrices & Tuples**: Matrix coordinate printing, tuple memory interning analysis (`t = (1,) * 3`), $O(n+m)$ two-pointer merge of sorted tuples without `.sort()`, consecutive range interval compaction, matrix saddle points (`pontos_de_sela`), and word grouping by vowel signature.
- **Turtle Simulations**: Genetic turtle automaton (`ADN: 'f', 't', 'd', 'e'`), random walk within finite 2D bounded grids.

---

## 🚀 How to Run the Code

### Requirements
- **Python 3.10+** (Python 3.14 recommended, using standard library modules `math`, `random`, `turtle`, `keyword`).

### Execution Examples

Run any non-graphical problem directly in the terminal:
```bash
# Example: Car insurance calculator (Ficha 2)
python3 Introducao-a-Programacao-Python/ficha-2-numeros-e-expressoes/programas-no-editor/2_2_12_seguro_automovel.py

# Example: Approximation of Euler's e (Ficha 3)
python3 Introducao-a-Programacao-Python/ficha-3-instrucoes-de-controlo/instrucoes-de-controlo/3_3_07_aproximacao_euler.py

# Example: Caesar cipher and DNA complement (Ficha 4)
python3 Introducao-a-Programacao-Python/ficha-4-definicoes-e-sequencias/cadeias-de-carateres/4_3_10_cifra_cesar.py

# Example: Anagrams and saddle points (Ficha 6)
python3 Introducao-a-Programacao-Python/ficha-6-revisoes/cadeias-de-carateres/6_3_04_anagramas.py
python3 Introducao-a-Programacao-Python/ficha-6-revisoes/tuplos-e-matrizes/6_4_05_pontos_de_sela.py
```

Run Turtle graphics visualizations (opens a Tkinter GUI window; click on canvas to exit):
```bash
# Concentric colored squares
python3 Introducao-a-Programacao-Python/ficha-5-modulo-turtle/formas-geometricas/5_3_02_quadrados_concentricos_coloridos.py

# Sliced hexagon
python3 Introducao-a-Programacao-Python/ficha-5-modulo-turtle/formas-geometricas/5_3_04_hexagono_fatiado.py

# Yin-Yang symbol
python3 Introducao-a-Programacao-Python/ficha-5-modulo-turtle/simbolos-e-figuras-curvas/5_3_17_yin_yang.py

# 2D Grid Random Walk
python3 Introducao-a-Programacao-Python/ficha-6-revisoes/turtle-simulacoes/6_5_05_passeio_aleatorio_grelha.py
```

---

## ✍️ Author & Course Reference

- **Course:** Introdução à Programação (IP)
- **Degree:** Licenciatura em Inteligência Artificial e Ciência de Dados (LEI / LCD / LTI)
- **Institution:** Departamento de Engenharia Informática (DEI), Faculdade de Ciências e Tecnologia da Universidade de Coimbra (FCTUC)
