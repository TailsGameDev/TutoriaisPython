'''
Para usar classes de outros arquivos, use from <nomeDoOutroArquivo> import <nomeDaClasse>
Caso queira importar tudo que estiver no outro arquivo, use asterísco. Exemplo abaixo.
Isso é muito importante! É a maneira para usar código que está escrito em outros arquivos!
É crucial em projetos grandes.
'''
from moreClasses import *

'''
Classes são muito importantes e muito usadas na programação.
Elas servem para organizar melhor os códigos, e torná-los mais fáceis
de serem expandidos (ajudam o projeto a crescer ordenadamente)
Classe é tipo um molde para criar vários objetos de acordo.
Tipo você pode criar uma classe Guerreiro, que vai definir como
os guerreiros são, e depois você pode criar vários guerreiros muito
facilmente.
Uma classe guarda atributos e métodos.
Atributos são as características do objeto, coisas como cor, preço,
peso, durabilidade, nome, etc.
Métodos são coisas que algo é capaz de fazer, tipo atacar, mover,
calcularProbabilidade, perderBraço, explodir.
Não deixe de conferir o exemplo com o Guerreiro.py!! Está no repositório.
'''
class FirstClass:
    #abaixo está o método construtor, que define como os objetos são criados.
    def __init__ (self, arg1 = "batata", arg2 = "peixe"):
        self.atributo1 = arg1
        self.atributo2 = arg2

    def metodo(self):
        print("chamou metodo")

# Aqui está acontecendo a criação de um objeto do tipo FirstClass!!
# A variável que guarda esse objeto está sendo chamada de firstObj
firstObj = FirstClass()

print("atributo1: " + str(firstObj.atributo1))

#chamando método do objeto.
firstObj.metodo()

secondObj = FirstClass("pudim", "chucrute")

print("secondObj.atributo2: " + secondObj.atributo2)

# Aqui estou criando um objeto de uma classe que está em outro arquivo!
# Isso só é possível por causa do import láa no início desse código aqui.
ObjFromAnotherFile = SecondClass()

ObjFromAnotherFile.metodo()


print("\n" + "Partiu testar a herança!!")

class ChildClass(FirstClass):
    def __init__(self, arg1 = "batata", arg2 = "peixe", childArg = "childyAtribute"):
        FirstClass.__init__(self, arg1, arg2) #TEM QUE PASSAR O SELF BICHO!!!
        self.childAtributo = childArg

    def metodo2(self):
        print("chamei meu metodo novo, que nao herdei!")

child = ChildClass()

print("child atributos: " + child.atributo1 + " " +
        child.atributo2 + " " + child.childAtributo)
child.metodo()
child.metodo2()
