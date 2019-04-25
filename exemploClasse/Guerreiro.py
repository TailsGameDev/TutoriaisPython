from Arma import *
from Personagem import *

class Guerreiro:

    def __init__(self, nome = "fulano", vida = 40):
        Personagem.__init__(self,nome)
        self.vida = vida

    def TahVivo(self):
        vivo = self.vida > 0
        return vivo

    def PrintGuerreiro(self):
        print("Nome do guerreiro: " + self.nome)
        print("Vida: " + str(self.vida))

guerreiro1 = Guerreiro("Franco", 50)
print(guerreiro1.nome)

if guerreiro1.TahVivo():
    print("O guerreiro "+guerreiro1.nome
    + " estah vivo!")

guerreiroPadrao = Guerreiro()
guerreiroPadrao.PrintGuerreiro()

caina = Guerreiro("Caina")
caina.PrintGuerreiro()

# usando classe de outro arquivo
Espada = Arma(20)
print(Espada.dano)
