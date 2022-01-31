# Curso de Python - Lógica de Programação
---
    MUNDO 1
---
## Aula 1
- Variáveis simples e print
- hashtag(#) transforma uma linha num comentário.
- """Também transforma em comentário, mas em quebra de linhas também"""

## Aula 2
- Tipos Primitivos:
    [int] - Números inteiros: 7, -4, 0, 9875;
    [float] - Números reais(ou flutuantes): 4.5, 0.076, -15.223, 7.0;
    [bool] - Aceita apenas dois valores, verdadeiro e falso: True, False;
    [str] - Valores são palavras: 'Olá', '7.5', ''.

## Aula 3
- Operadores Aritméticos
    [+] adição                  5 + 2 == 7
    [-] Subtração               5 - 2 == 3
    [*] Multiplicação           5 * 2 == 10
    [/] Divisão                 5 / 2 == 2.5
    [**] Potência               5 ** 2 == 25
    [//] Divisão Inteira        5 // 2 == 2
    [%] Resto da Divisão        5 % 2 == 1

- Ordem de Precedência
    [1] ()
    [2] **
    [3] *   /   //  %
    [4] +   -

## Aula 4
- Módulos
    Para importar bibliotecas é só utilizar [import] e a biblioteca desejada, ou [from] >>> biblioteca >>> [import] >>> funcionalidade específica.

## Aula 5
- Strings
    
## Aula 6
- Condições
    Condições Simples, Compostas e Simplificadas
    [if]
    [else]
    [and]
    [or]

## Aula 7
- Cores no Terminal
---
    MUNDO 2
---
## Aula 1
- Condições Aninhadas
    [elif] = else + if no python
    [in] - ex: elif <nome> in 'Algo':

## Aula 2, 3 e 4
- Laços de Repetição
    [for] c in range(0, 10, 1): ----------- range = gera uma sequência de números.
    [while] (enquanto):
    [break] (Quebra de laço "while True:")
---
    MUNDO 3
---
## Aula 1
- Variáveis Compostas 
    Tuplas:
    - len(variável) = ler quantas tuplas tem dentro de uma variável.
    Obs: As túplas são imutáveis, ou seja, uma tupla não tem como ser redefinida.

    Variável = (Túpla) [Lista] {Dicionário}

    [del(variável)] = apagar a composição da variável, ou seja, variével deixa de existir.

    Listas:
    [.append('')] = adiciona um item extra no final da lista.
    [.insert(0,')] = adiciona um item extra na posição informada da lista.
    [del] variével[3] = apaga o item da posição escolhida.
    [variável.pop()] = apaga o item da última posição ou da posição escolhida.
    [variável.remove('')] = elimina o valor indicado da lista.

    valores = list(range(4, 11))
    valores = 4, 5, 6, 7, 8, 9, 10

    valores = [8, 2, 5, 4, 9, 3, 0]
    valores.sort() = 0, 2, 3, 4, 5, 8, 9
    valore.sort(reverse=True) = 9, 8, 5, 4, 3, 2, 0

    len(valores) = conta a quantidade de valores da variável

    