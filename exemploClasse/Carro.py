#para gerar um numero inteiro aleatorio:
from random import randint

class Carro:
    #metodo construtor. Toda classe deve ter!!
    def __init__(self, marca, p = 0): # p eh argumento padrao!
        self.velocidade = 40 #km/h
        self.posicao = p
        self.marca = marca

    def andarPor1H(self):
        self.posicao=self.posicao+self.velocidade

    def PrintCarro(self):
        print("carro marca: "+self.marca)
        print("posicao: "+str(self.posicao))


#0  40     80      120      160
# ---------------------------->

#criando varios objetos da classe Carro
toyota = Carro("TOYOTA")
audi = Carro("AUDI")
ferrari = Carro("FERRARI")
lamborghini = Carro("LAMBORGHINI")

listaDeCarros = [toyota, audi,
 ferrari, lamborghini]

#as proximas 3 linhas fazem as seguintes repetirem 5 vezes
horasDaCorrida = 5;
while horasDaCorrida > 0:
    horasDaCorrida -= 1
    #para cada carro na lista
    for carro in listaDeCarros:
        print(carro.velocidade)
        #velocidade recebe inteiro aleatorio 80<inteiro
        carro.velocidade = randint(80, 200)
        carro.andarPor1H()
        carro.PrintCarro()
    print(" ") #pula uma linha

#daqui para baixo eh a logica de ver quem venceu
maiorPosicao = 0
vencedor = listaDeCarros[0]
for carro in listaDeCarros:
    if(carro.posicao>maiorPosicao):
        maiorPosicao = carro.posicao
        vencedor = carro

print("O carro vencedor eh: ")
vencedor.PrintCarro()
