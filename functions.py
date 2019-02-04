def helloFunction():
    print("Hello functions")

print("I'm not calling funtion");

helloFunction()

def canIDeclareHere():
    print("I am calling function declared in the middle of the code")

print("I'm not calling funtion declared in the middle of the code");

canIDeclareHere()

def printForMe(string):
    print(string)

printForMe("batata")

def defaultArg(string = "padraozao"):
    print(string)

defaultArg()

def IReturnCrazyStuff(i):
    if i<5:
        return "peixe"
    elif i<10:
        return 42
    return 9.67

print(str(IReturnCrazyStuff(4)))
print(str(IReturnCrazyStuff(7)))
print(str(IReturnCrazyStuff(20)))
