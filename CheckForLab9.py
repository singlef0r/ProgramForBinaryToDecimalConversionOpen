from lab.DictionaryToLab9 import DictionaryFinal
def checkNumber(number):
    Flag = [0 for _ in range(len(number))]
    while len(Flag) != sum(Flag):
        numbers = [i for i in number]
        printNumber = ''.join(numbers)
        for i in range(len(numbers)):
            if 1<=len(numbers[i]) <= 2:
                if numbers[i] in "0123456789" or numbers[i] in "-1-2-3-4-5-6-7-8-9" or number[i] in "/*-+.,":
                    Flag[i] = 1
                else: 
                    print('Неккоректный ввод цифры','"'+numbers[i]+'"','в числе:', printNumber)
                    number[i] = input()
                    break
            else:
                print('Неккоректный ввод цифры','"'+numbers[i]+'"','в числе:', printNumber)
                number[i] = input()
                break
    return number
def checkParametersOne(parameters):
    Flag = [0 for _ in range(len(parameters))]
    while len(Flag) != sum(Flag):
        numbers = [i for i in parameters]
        for i in range(len(numbers)):
            if 1 <= len(numbers[i]) <= 2:
                if numbers[i] in "123456789" or (numbers[i] in "-1-2-3-4-5-6-7-8-9" and numbers[i] != '-'):
                    Flag[i] = 1
                else: 
                    print('Неккоректный ввод','"'+numbers[i]+'"','в параметрах:', parameters)
                    parameters[i] = input('Введите цифру: ')
                    break
            else:
                print('Неккоректный ввод','"'+numbers[i]+'"','в параметрах:', parameters)
                parameters[i] = input('Введите цифру: ')
                break
    return checkParametersTwo(parameters)
def checkParametersTwo(parameters):
    Flag = False
    while Flag == False:
        parameter = [1 for i in parameters if i == '1']
        if len(parameters) != 4 :
            print("Параметров должно быть 4!")
            parameters = [i for i in input("Введите параметры кода правильно, через пробел: ").split()]
        elif sum([int(i) for i in parameters]) < 9:
            print("Сумма параметров должна быть >= 9")
            parameters = [i for i in input("Введите параметры кода правильно, через пробел: ").split()]
        elif len(set(parameters)) != 4 and  sum([int(i) for i in parameters]) > 9:
            print("Параметры одинаковые!")
            parameters = [i for i in input("Введите не одинаковые параметры кода, через пробел: ").split()]
        elif sum(parameter) == 0:
            print("В параметрах должна быть хотябы одна единица")
            parameters = [i for i in input("Введите параметры кода правильно, через пробел: ").split()]
        else:
            Flag = True
    return parameters
def allCheck(parameters, number):
    parametersInDictionary = [i for i in checkParametersOne(parameters)]
    numberInDictionary = [i for i in checkNumber(number)]
    return DictionaryFinal(parametersInDictionary, numberInDictionary)