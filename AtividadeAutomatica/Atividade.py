#fiz um script para testar esse script!

#questao 1
#complete o codigo de maneira que que um personagem ao equipar uma arma receba
#o bonus de ataque dela. Ao desequipar, seu ataque deve voltar ao valor
#original, e ele não tenha o direito de equipar mais de uma arma ao mesmo tempo
class personagem:
    def __init__(self):
        self.ataque = 5
        #podes inserir codigo aqui

    def equipar (self, umaArma):
        pass
        #podes inserir codigo aqui

    def desequiparArma(self):
        pass
        #podes inserir codigo aqui
    
class arma:
    def __init__(self, umBonusAtk):
        self.bonusAtk = umBonusAtk

#questao 2
# em um cenario pos apocalíptico, um sobrevivente decide fazer um programa
# que calcula quantos dias o seu grupo sobreviveria com a comida que tem
# complete com uma logica que verifica quanto cada pessoa na
# listaDeSobreviventes come por dia,
# e então faz as contas de quantos dias restariam para que comida chegasse a 0.
# faça com que o método quantosDiasSobreviveriamos retorne essa quantia.
# alem disso, verifique se ele mesmo está na lista, pois ele também conta!
# e não deve ser contado duas vezes caso ele esteja na lista!

comida = 50 #kg esse valor nao deve ser alterado na execucao
class sobrevivente:
    def __init__(self, taxaDeComidaPorDia = 0.300):
        self.comidaPorDia = taxaDeComidaPorDia

    def quantosDiasSobreviveriamos(self, listaDeSobreviventes):
        pass
        #podes inserir codigo aqui
        #lembre-se de retornar a quantidade de dias.

