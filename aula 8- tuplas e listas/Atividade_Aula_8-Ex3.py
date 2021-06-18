# 03 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

lista1 = [5, 7, 2, 9, 4, 1, 3]
print (f"""
a)O tamanho da lista 1 é: {len(lista1)}
b)O maior valor da lista 1 é: {max(lista1)}
c)O menor valor da lista 1 é: {min(lista1)}
d)A soma de todos elementos da lista 1 é: {sum(lista1)}
e)A lista 1 em ordem crescente é: {sorted(lista1)}
f)A lista 1 em ordem drescente é: {sorted(lista1,reverse=True)} """)