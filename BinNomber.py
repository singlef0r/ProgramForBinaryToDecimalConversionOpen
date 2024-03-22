def BinNomberFun(parameters, number):
    listForTryNomber = []
    listForBin = [0, 0, 0, 0]
    for i in range(len(parameters)):
        listNotI = parameters[i + 1:len(parameters)]
        if int(parameters[i]) == number:
            listForBin[i] = 1
        if listForBin not in listForTryNomber and sum(listForBin) != 0:
            listForTryNomber.append(listForBin)
            listForBin = [0, 0, 0, 0]
        for j in range(len(listNotI)):
            listNotJ = listNotI[j + 1:len(listNotI)]
            if int(parameters[i]) + int(listNotI[j]) == number:
                listForBin[i] = 1
                listForBin[i + j + 1] = 1
            if listForBin not in listForTryNomber and sum(listForBin) != 0:
                listForTryNomber.append(listForBin)
                listForBin = [0, 0, 0, 0]
            for k in range(len(listNotJ)):
                listNotK = listNotJ[k + 1:len(listNotJ)]
                if int(parameters[i]) + int(listNotI[j]) + int(listNotJ[k]) == number:
                    listForBin[i] = 1
                    listForBin[i + j + 1] = 1
                    listForBin[i + j + k + 2] = 1
                if listForBin not in listForTryNomber and sum(listForBin) != 0:
                    listForTryNomber.append(listForBin)
                    listForBin = [0, 0, 0, 0]
                for l in range(len(listNotK)):
                    if int(parameters[i]) + int(listNotI[j]) + int(listNotJ[k]) + int(listNotK[l]) == number:
                        listForBin[i] = 1
                        listForBin[i + j + 1] = 1
                        listForBin[i + j + k + 2] = 1
                        listForBin[i + j + k + l + 3] = 1
                    if listForBin not in listForTryNomber and sum(listForBin) != 0:
                        listForTryNomber.append(listForBin)
                        listForBin = [0, 0, 0, 0]
    if listForTryNomber == []:
        return [[0,0,0,0]]
    else:
        return listForTryNomber