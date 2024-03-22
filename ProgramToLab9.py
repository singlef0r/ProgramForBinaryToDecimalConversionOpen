from lab.CheckForLab9 import allCheck
def main():
    stopWord = ""
    print("Добро пожаловать! Вы звпустили программу:\n     Кодирование информации. Двоично-десятичные коды.")
    while stopWord != "stop":
        parameters = [i for i in input("Введите параметры кода через пробел: ").split()]
        number = [i for i in input("Введите число: ")]
        print(allCheck(parameters, number))
        stopWord = input("Для продолжения нажмите Enter! \nДля выхода из программы напишите Stop:").lower()
    else:
        print("Досвидания!")
if __name__ == "__main__":
    main()


# Введите параметры(через пробел): 1 2 3 3
# Введите число: 25431
# 0100 0101 1001 1100 1000
# 0100 0110 1010 0010 1000
# 0100 1110 1001 0001 1000
#print(allCheck(parameters = ['1','2','3','4'], number = [i for i in '5745-5897+55.82'] ))

#Ф AF 22 - =  -> 1 2 3 4                  $ A . 0 -> 5 2 4 1
#574a-589b+55.ac               123-321+456/asd.1c -> 123-321+456/514.12