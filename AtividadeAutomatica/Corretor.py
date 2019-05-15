from Atividade import *

def test_questao1():
    print("\nQuestao 1")
    #criando personagem e arma
    p = personagem()
    atkInicial = p.ataque
    bonus = 5
    a = arma(bonus)

    #testando acrescimo de ataque
    p.equipar(a)
    atkEquipado = p.ataque
    ok= atkEquipado == atkInicial + bonus
    if (ok):
        print("[OK] item equipado com sucesso")
    else:
        print("[FAIL] problema ao equipar item")
    
    #testando se equipa duas armas
    p.equipar(a)
    ok = p.ataque == atkEquipado
    if (ok):
        print("[OK] nao equipou duas armas")
    else:
        print("[FAIL] aparentemente estah equipando 2 armas")

    #testando se desequipou
    p.desequiparArma()
    ok = p.ataque == atkInicial and atkInicial != atkEquipado
    if (ok):
        print("[OK] desequipou a arma com sucesso")
    else:
        print("[FAIL] problemas ao desequipar arma")

def test_questao2():
    print("\nQuestao 2")
    #um sobrevivente, 1kg por dia, 50 dias
    s = sobrevivente(1)
    list = [s]
    ok = s.quantosDiasSobreviveriamos(list) == 50
    if (ok):
        print("[OK] teste com um sobrevivente ok!")
    else:
        print("[FAIL] nao funciona para 1 sobrevivente na lista")

    #2 sobreviventes, 1kg por dia, 25 dias
    s2 = sobrevivente(1)
    list.append(s2)
    ok = s.quantosDiasSobreviveriamos(list) == 25
    if (ok):
        print("[OK] teste com 2 sobreviventes")
    else:
        print("[FAIL] 2 sobreviventes na lista")

    #4 sobreviventes, e o que faz a conta nao esta na lista
    s3 = sobrevivente(1)
    s4 = sobrevivente(1)
    s5 = sobrevivente(1)
    list.extend([s3,s4,s5])
    list.remove(s)
    ok = s.quantosDiasSobreviveriamos(list) == 10
    if (ok):
        print("[OK] para 4 sobreviventes, e esse nao pre-incluso na lista")
    else:
        print("[FAIL] 4 sobreviventes e esse nao pre-incluso na lista")

    #5 sobreviventes com taxas diferentes
    s.comidaPorDia = 2
    s2.comidaPorDia = 4
    s3.comidaPorDia = 3
    s4.comidaPorDia = 3
    list = [s,s2,s3,s4]
    ok = s.quantosDiasSobreviveriamos(list) == 5
    if (ok):
        print("[OK] 5 sobreviventes com taxas diferentes de comida")
    else:
        print("[FAIL] 5 sobreviventes com taxas diferentes de comida")


test_questao1()
test_questao2()
