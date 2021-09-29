listas_simples_inteiro = [1, 2, 3, 4, 5]
listas_simples_string = ["Olá", "Mundo"]
listas_simples_mesclada = [1, 2, 3, "Olá, mundo", True, 1.5]

nested_list = [[1, 2, True], ["Olá", "mundo"]]

# len
print(len(listas_simples_mesclada))
print(len(nested_list))

# append()
listas_simples_inteiro.append(6)
print(listas_simples_inteiro)

# insert()
#listas_simples_inteiro.insert(2, "olá")
#print(listas_simples_inteiro)

# Remove()
listas_simples_inteiro.remove(1)
print(listas_simples_inteiro)

# index()

index = listas_simples_inteiro.index(3)
print(index)

# count()
count = listas_simples_inteiro.count(3)
print(count)

# sort()
lista_string = ["A", "B", "C"]
lista_string.sort(reverse=True)
print(lista_string)
