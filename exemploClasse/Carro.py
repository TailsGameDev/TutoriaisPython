from random import randint
class Carro:
    def __init__(self, marca, p = 0):
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


toyota = Carro("TOYOTA")
audi = Carro("AUDI")
ferrari = Carro("FERRARI")
lamborghini = Carro("LAMBORGHINI")

listaDeCarros = [toyota, audi,
 ferrari, lamborghini]

horasDaCorrida = 5;
while horasDaCorrida > 0:
    horasDaCorrida -= 1
    for carro in listaDeCarros:
        print(carro.velocidade)
        carro.velocidade = randint(80, 200)
        carro.andarPor1H()
        carro.PrintCarro()
    print(" ")

maiorPosicao = 0
vencedor = listaDeCarros[0]
for carro in listaDeCarros:
    if(carro.posicao>maiorPosicao):
        maiorPosicao = carro.posicao
        vencedor = carro

print("O carro vencedor eh: ")
vencedor.PrintCarro()
