"""Faça um programa para gerar automaticamente números entre 0 e 99 de uma
cartela de bingo. Sabendo que cada cartela deverá conter 5 linhas de 5
números, gere estes dados de modo a não ter números repetidos dentro das
cartelas. O programa deve exibir na tela a cartela gerada."""

import random
bingo = []
check = []

for i in range(5):
    #Gera as linhas
    linha = []
    coluna = 1
    while coluna <= 5:
        num = random.randint(0, 99)
        if check.count(num) == 1:
            continue
        else:
            check.append(num)
            linha.append(num)
            coluna = coluna + 1
    bingo.append(linha)

for linha in bingo:
    for col in linha:
        print(str(col) + '\t', end = ' ')
    print('')