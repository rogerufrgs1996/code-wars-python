strng = "56 65 74 90 180 68 86"


def order_weight(strng):
    soma = 0
    peso = ""
    ordem = {}
    somas = []
    pesos = []
    for x in strng:
        if x.isalnum():
            peso = str(peso) + x
            soma = soma + int(x)
        else:
            ordem.update({peso: soma})
            somas.append(soma)
            pesos.append(peso)
            peso = ""
            soma = 0
    ordem.update({peso: soma})
    somas.append(soma)
    pesos.append(peso)
    somas.sort()
    pesos.sort()
    for pe in pesos:
        i = somas.index(ordem.get(pe))
        somas[i] = pe
    return " ".join(somas)


print(order_weight(strng))
