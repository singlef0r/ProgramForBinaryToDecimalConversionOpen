from lab.BinNomber import BinNomberFun
def dictionaryСreation(parameters, number):
    listNumbers = [i for i in number]
    binDictinary = {i:'' for i in range(10)}
    for i in binDictinary:
        binDictinary[i] = BinNomberFun(parameters,i)
    finalBinNumber = [[] for _ in range(max([len(binDictinary[i]) for i in binDictinary]))]
    for j in range(len(finalBinNumber)):
        for i in listNumbers:
            if (i in "0123456789" or i in "-1-2-3-4-5-6-7-8-9") and i != "-":
                if len(binDictinary[int(i)]) == 3:
                    finalBinNumber[j].append(binDictinary[int(i)][j])
                elif len(binDictinary[int(i)]) == 2:
                    finalBinNumber[j].append(binDictinary[int(i)][j-1])
                else:
                    finalBinNumber[j].append(binDictinary[int(i)][0])
            else:
                finalBinNumber[j].append(i)
    if finalBinNumber[0] == finalBinNumber[1]:
        return finalBinNumber[0]
    else:
        return finalBinNumber
def DictionaryFinal(parameters, number):
    finalBinNumber = ''
    for i in dictionaryСreation(parameters, number):
        for j in i:
            for k in j:
                finalBinNumber += str(k)
            # finalBinNumber += "|"
        finalBinNumber += ' или '
    finalBinNumber = finalBinNumber[:-4]
    print("Для параметров кода: ",*parameters," и введенного числа: ",*number," Ответом будет:")
    return finalBinNumber