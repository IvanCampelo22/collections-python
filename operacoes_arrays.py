from array import array

array_1 = array('B', [1, 2, 3, 4, 5, 6])
array_2 = array('u', ['O', 'L', 'A'])

for i in array_2:
    print(i)

# print(array_1)

# for i in array_1:
# print(i)

# inserindo elementos no array

array_1.insert(2, 50)
# for i in array_1:
# print(i)


# removendo elementos de array
array_1.remove(4)

# for i in array_1:
#    print(i)

# buscar elementos em um array
print(array_1.index(50))

#atualizando dados em array

array_1[2] = 55

for i in array_1:
    print(i)
