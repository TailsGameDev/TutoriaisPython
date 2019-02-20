#escreve na tela a mensagem e captura input de teclado armazenando em "num"
num = input("Digite um numero e eu lhe direi a soma dele com 8\n")

num = int(num) # convertendo para inteiro

print(num + 8)

num = input("Agora, digite dois numeros separados por espaco\n")

# agora vou somar todos os numeros que o usuario digitar (apesar d que pedi 2)
num = num.split(" ")
acumula = 0 #criando variavel para ir somando cada numero

for x in num: #percorrendo lista com todos os numeros submetidos
    acumula = acumula + int(x) #para cada numero, eu somo ele a acumula
# para mais informacoes sobre listas, veja o arquivo vectors.py

print("A soma dos numeros submetidos eh: " + str(acumula))
