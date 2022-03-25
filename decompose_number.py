"""
Descrição do Desafio: Decompondo números

Complete a seguinte função, para que a mesma devolva todos os possíveis
números de 4 dígitos, onde cada um seja menor ou igual a <maxDigit>, e a
soma dos dígitos de cada número gerado seja 21.

Exemplos com maxDigit = 6: 3666; 4566
"""

import itertools
import sys


def decompose_number(maxDig):
    l1 = sorted(list(range(0, maxDig + 1)) * 4)
    l2 = set(list(itertools.permutations(l1, 4)))

    for i in l2:
        if sum(i) == 21:
            sys.stdout.write(''.join(map(str, i)) + '\n')


decompose_number(6)
