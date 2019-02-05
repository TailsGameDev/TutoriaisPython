class SecondClass:
    #python nao permite construtores multiplos, mas permite default value
    def __init__ (self, arg1 = "SecondBatata", arg2 = "SecondPeixe"):
        self.atributo1 = arg1
        self.atributo2 = arg2

    def metodo(self):
        print("chamou Second.metodo")

""" block comment

firstObj = FirstClass()

print("atributo1: " + str(firstObj.atributo1))

firstObj.metodo()

secondObj = FirstClass("pudim", "chucrute")

print("secondObj.atributo2: " + secondObj.atributo2)

"""
