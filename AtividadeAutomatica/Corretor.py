#para funcionar tem que estar instalado no PC o pytest.
#para verificar se estah instalado use comando no terminal: pip show pytest
#se mostrar algo está instalado
#se não estiver, usar comando pip install pytest
#obs: o pip precisa estar instalado, mas instalei em todos os PCs menos o 4

#nao altere esse script!!!!!!!!!!

import pytest

from Gabarito import *

def test_questao1_test():
    #criando personagem e arma
    p = personagem()
    atkInicial = p.ataque
    bonus = 5
    a = arma(bonus)

    #testando acrescimo de ataque
    p.equipar(a)
    atkEquipado = p.ataque
    assert atkEquipado == atkInicial + bonus
    
    #testando se equipa duas armas
    p.equipar(a)
    assert p.ataque == atkEquipado
    print(p.ataque)

    #testando se desequipou
    p.desequiparArma()
    print(p.ataque)
    assert p.ataque == atkInicial
    assert atkInicial != atkEquipado

def test_questao2():
    #um sobrevivente, 1kg por dia, 50 dias
    s = sobrevivente(1)
    list = [s]
    assert s.quantosDiasSobreviveriamos(list) == 50

    #2 sobreviventes, 1kg por dia, 25 dias
    s2 = sobrevivente(1)
    list.append(s2)
    assert s.quantosDiasSobreviveriamos(list) == 25

    #4 sobreviventes, e o que faz a conta nao esta na lista
    s3 = sobrevivente(1)
    s4 = sobrevivente(1)
    s5 = sobrevivente(1)
    list.extend([s3,s4,s5])
    list.remove(s)
    assert s.quantosDiasSobreviveriamos(list) == 10

    #5 sobreviventes com taxas diferentes
    s.comidaPorDia = 2
    s2.comidaPorDia = 4
    s3.comidaPorDia = 3
    s4.comidaPorDia = 3
    list = [s,s2,s3,s4]
    assert s.quantosDiasSobreviveriamos(list) == 5
