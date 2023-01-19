arr = [1, 2, 2, 2, 3, 3, 4, 5, 3, 2, 1]
def pick_peaks(arr):

    pos = []
    peak = []
    subindo = 0
    parado = 0
    t = 0
    platopos = 0
    while t < len(arr) - 1:
        if arr[t] < arr[t + 1]: #vendo se a sequencia de numeros está aumentando em valor
            subindo = 1
            parado = 0
            t += 1
        elif arr[t] > arr[t + 1] and subindo == 1: #se o grafico está decrescendo após ter subido é identificado um pico
            if parado == 1: #se o grafico ter como ponto alto uma plato
                pos.append(platopos)
                peak.append(arr[t])
                subindo = 0
                parado = 0
                t += 1
            else:          #se o ponto alto for apenas 1 numero
                pos.append(t)
                peak.append(arr[t])
                subindo = 0
                parado = 0
                t += 1
        elif arr[t] == arr[t + 1] and subindo == 1 and parado != 1: #se o grafico estiver constante após ter crescido
            platopos = t
            parado = 1
            t += 1

        else: #se estiver apenas decrescendo
            t += 1
    print(pos)
    print(peak)
    thisdict = {"pos": pos, "peaks": peak}

    return thisdict
pick_peaks(arr)