from moreClasses import *

class FirstClass:
    #python nao permite construtores multiplos, mas permite default value
    def __init__ (self, arg1 = "batata", arg2 = "peixe"):
        self.atributo1 = arg1
        self.atributo2 = arg2

    def metodo(self):
        print("chamou metodo")

firstObj = FirstClass()

print("atributo1: " + str(firstObj.atributo1))

firstObj.metodo()

secondObj = FirstClass("pudim", "chucrute")

print("secondObj.atributo2: " + secondObj.atributo2)

ObjFromAnotherFile = SecondClass()

ObjFromAnotherFile.metodo()


print("\n" + "Lets try inheritance!!")

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
