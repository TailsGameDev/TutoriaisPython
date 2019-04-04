# definindo vetor, ou lista
lista = [1,2,4,6,8,9,15]
print(lista)

for x in lista:
    print(x)

print("partiu somar")
soma = 0
for x in lista:
   soma = soma + x
   print(soma)

print("a soma dos elementos nesse vetor eh "+str(soma))

vector2 = ["peixe", 3, 0.7, True]

print(vector2)

for x in vector2:
    print(x)
