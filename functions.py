def helloFunction():
    print("Ola Funcoes")

print("Eu nao chamei a funcao ainda");

helloFunction() #chamando agora

def canIDeclareHere(): #testando declaracao de funcao no meio do arquivo
    print("se impresso, foi chamada funcao declarada no meio do arquivo")

print("Nao chamei a funcao declarada no meio do arquivo ainda");

canIDeclareHere() #chamando agora a funcao declarada no meio do arquivo

#funcao que leva um argumento. Argumento eh uma variavel para a funcao usar, que voce envia para ela quando a chama
def printForMe(string):
    print(string)

printForMe("batata")

#testando opcao de argumento padrao. Nao eh muito importante
def defaultArg(string = "padraozao"):
    print(string)

defaultArg()

#essa funcao eh capaz de retornar tanto uma string, quanto um numero inteiro, ou um numero real.
#em C# isso nao seria tao facil
def IReturnCrazyStuff(i):
    if i<5:
        return "peixe"
    elif i<10:
        return 42
    return 9.67

print(str(IReturnCrazyStuff(4)))
print(str(IReturnCrazyStuff(7)))
print(str(IReturnCrazyStuff(20)))
