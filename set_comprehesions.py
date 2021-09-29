# Criando um set comprehesions

set_1 = {1, 2}
set_2 = {3, 4}

set_comprehesions  = {i * i for i in range(0, 10)}
print(type(set_comprehesions))

set_comprehesions_2 = {i for i in set_1.union(set_2)}
print(type(set_comprehesions_2))

