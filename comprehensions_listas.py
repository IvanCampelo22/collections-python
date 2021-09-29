listas_simples_inteiro = [1, 2, 3, 4, 5, 14, 4, 5]
nova_lista = []
for i in listas_simples_inteiro:
    nova_lista.append(i * i)
print(nova_lista)

nova_lista_elegante = [i * i for i in range(1, 10)]
print(nova_lista_elegante)


