minha_tupla = (1, 2, 3, "olá", "mundo", 1.5, True)
minha_tupla2 = 1, 2, 3, "olá", "mundo", 1.5, True

print(type(minha_tupla2))
print(type(minha_tupla))

# count
print(minha_tupla.count(1))

# index
print(minha_tupla.index(3))

# verificar a existência de um elemento na tupla
print(2 in minha_tupla)

print(minha_tupla.__add__(minha_tupla2))
