strng = "56 65 74 100 99 68 86 "
def order_weight(strng):
    soma = 0
    peso = ""
    ordem = {}
    somas = []
    pesos = []
    resultado = []
    for x in strng:
        if x.isalnum() == True:
            peso = str(peso) + x
            soma = soma + int(x)
        else:
            ordem.update({peso: soma})
            somas.append(soma)
            pesos.append(peso)
            peso = ""
            soma = 0

    else:
        ordem.update({peso: soma})
        somas.append(soma)
        pesos.append(peso)
        somas.sort()
        pesos.sort()
        resultado = somas.copy()
        for pe in pesos:
            i = somas.index(ordem.get(pe))
            resultado.pop(i)
            resultado.insert(i, pe)
            somas[i] = 0
        resultado = " ".join(resultado)

    return resultado