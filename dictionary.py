myDictionary = {
    1: "um",
    2: "dois",
    "tres": 3,
}

print(myDictionary)

for x in myDictionary:
    print(x)

thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

for x,y in myDictionary.items():
    print(str(x) + " " + str(y))

votosPorCandidato = {
    "paulo": 0,
    "pedro": 0,
}

print("\n" + "Vamos votar!!")

votosPorCandidato["paulo"] = votosPorCandidato["paulo"] + 1

print("votos do Paulo: " + str(votosPorCandidato["paulo"]))
