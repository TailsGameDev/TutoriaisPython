i = 11

if i<4: # se i eh menor que 4
    print("i eh menor que 4") #fazer isso
elif i < 10: # se nao, mas i eh menor que 10
    print("i eh menor que 10") #fazer isso
else: #se nao
    print("i eh maior que 10")

print(i)

verdadeiro = 2 == 2; #igual se escreve com dois iguais. Um igual soh significa "recebe"
print(str(verdadeiro))

falso = 4 <= 1 # quatro eh menor ou igual que um? Nao!
print(str(falso))

variavelBooleana = 6*6 == 36
print("6 * 6 eh 36? " + str(variavelBooleana))

condicoesMultiplas = 6 < 7 and 7 < 8
print("seis eh menor que sete e sete eh menor que oito? " + str(condicoesMultiplas))

condicoesMultiplas = 6 < 7 or 1 >= 8
print("6 eh menor que 7 ou 1 eh maior ou igual a 8? " + str(condicoesMultiplas))
