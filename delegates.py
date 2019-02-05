def myFavoriteFunction():
    print("Let's make some delegates!")

minhasFuncoes = myFavoriteFunction

minhasFuncoes();

def anotherCoolFunction():
    print("this is the second funcion")

''' this didn't work
minhasFuncoes += anotherCoolFunction1
minhasFuncoes()
'''
print("\n"+"Let's make a function vector!!")

vectFunc = [myFavoriteFunction, anotherCoolFunction]

for x in vectFunc:
    x()
