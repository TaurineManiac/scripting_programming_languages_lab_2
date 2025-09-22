import random


def checkTryToInputString():
    while True:
        try:
            user_input = input("Введите строку: ").strip()

            # Проверка на пустой ввод
            if not user_input:
                print("Ввод не должен быть пустым. Попробуйте снова.")
                continue

            # Проверка на строку только из пробелов
            if user_input.isspace():
                print("Ввод не должен состоять только из пробелов. Попробуйте снова.")
                continue

            user_input = user_input.strip()

            return user_input

        except KeyboardInterrupt:
            print("\nВвод прерван пользователем")
            return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            continue

def calculateSpace():
    str = checkTryToInputString()
    maxLength = 0
    currentLength = 0
    counter=1
    start=0
    end=0
    isFirst = True
    str2=""
    for i in range(0, len(str)):
        if not str[i].isspace():
            currentLength += 1
            end = i
            if isFirst:
                start = i
                isFirst = False
                continue
            if str[i - 1].isspace():
                start = i
            if(currentLength >= maxLength):
                maxLength = currentLength
                if(start==end):
                    str2 = str
                else:
                    str2=str[start:end+1]

        else:
            counter+=1
            currentLength = 0

    print(counter)
    print(str2)

def lab2Task1():
    calculateSpace()
#==========================================================================
def defineType(type):
    if isinstance(type, dict):
        sortForDict(type)
    elif isinstance(type, list):
        findLettersAndNumbers(type)
    elif isinstance(type, str):
        isPalindrome(type)
    elif isinstance(type, int):
        isNumSimple(type)
def sortForDict(dict):
    dict2= dict
    dict2 = sorted(dict2.items(), key=lambda x: x[0])
    print("Сортировка по возрастанию:")
    print(dict2)
    dict2 = sorted(dict2, key=lambda x: x[0], reverse=True)
    print("По убыванию:")
    print(dict2)

def findLettersAndNumbers(type):
        print(type)
        coutnerLetters = 0
        counterNums=0
        for i in range(0, len(type)):
            if isinstance(type[i], str):
                for letter in type[i]:
                    if letter.isalpha():
                        coutnerLetters += 1
                    elif letter.isnumeric():
                        counterNums += 1
            if isinstance(type[i], int):
                counterNums += len(str(abs(type[i])))
        print(f"Количество букв и цифр соответственно:{coutnerLetters}, {counterNums}")

def isPalindrome(type):
    words = type.split()
    pals = []

    for word in words:
        clean_word = word.lower()
        if clean_word == clean_word[::-1]:
            pals.append(word)

    print("Найденные палиндромы:", pals)

def isNumSimple(type):
    if type <2:
        print(False)
        return

    for i in range (2,type):
        if type%i==0:
            print(False)
            return
    print(True)



def chooseType():
    while True:
        print("Выберите входящий аргумент 1-4 5-Выход:")
        choice = checkYourSolution(5)
        if choice == 1:
            type = {"qwerty" : 1, "zazza" : 2, "sosa": 3}
            defineType(type)
        elif choice == 2:
            type = ["Sosa", "&!&!&!&!&pppp",12345,666,"zxc2281337"]
            defineType(type)
        elif(choice == 3):
            type = checkTryToInputInt()
            defineType(type)
        elif(choice == 4):
            type = checkTryToInputString()
            defineType(type)
        else:
            break


def checkTryToInputInt():
    while True:
        try:
            user_input = input("Введите целое число: ").strip()


            if not user_input:
                print("Ввод не должен быть пустым. Попробуйте снова.")
                continue


            if user_input.isspace():
                print("Ввод не должен состоять только из пробелов. Попробуйте снова.")
                continue


            if user_input.startswith('-'):

                if not user_input[1:].isdigit() or len(user_input) == 1:
                    print("Некорректный ввод. Введите целое число.")
                    continue
            else:

                if not user_input.isdigit():
                    print("Некорректный ввод. Введите целое число.")
                    continue


            result = int(user_input)


            return result

        except ValueError:
            print("Некорректный ввод. Введите целое число.")
        except OverflowError:
            print("Число выходит за пределы диапазона для типа int.")


def checkYourSolution(last_num):
    while True:
        try:
            user_input = input("Введите число для выбора: ").strip()

            if not user_input:
                print("Ввод не должен быть пустым. Попробуйте снова.")
                continue

            result = int(user_input)

            if result < 1 or result > last_num:
                print(f"Число должно быть от 1 до {last_num}")
                continue

            return result

        except ValueError:
            print("Некорректный ввод. Введите целое число.")
        finally:
            print("Бебебебеббе сделал для тз")

def lab2Task2():
    chooseType()
#==========================================================================

def createMassive(ii,jj):
    rows=ii
    cols=jj
    matrix = [[0] * cols for _ in range(rows)]
    print("Выберите заполнить рандомно или самостоятельно 1/2")
    choice = checkYourSolution(2)
    if choice == 1:
        for i in range(0, rows):
            for j in range(0, cols):
                matrix[i][j] = random.randint(1, 100)
    elif choice == 2:
        for i in range(0, rows):
            for j in range(0, cols):
                matrix[i][j]=checkTryToInputInt()
    print(matrix)
    return matrix

def swapCols(matrix):
    n=-1
    m=-1
    while n<0:
        n = checkTryToInputInt()
    while m<0:
        m = checkTryToInputInt()
    if m >= len(matrix[0]) or n >= len(matrix[0]):
        print("Смена невозможна")
        return
    for i in range(len(matrix)):
        matrix[i][m], matrix[i][n] = matrix[i][n], matrix[i][m]
    print(matrix)

def lab2Task3():
    print("Введите размер массива IxJ:")
    i=-1
    j=-1
    while(i<0):
        i = checkTryToInputInt()
    while(j<0):
        j = checkTryToInputInt()
    swapCols(createMassive(i,j))

#==========================================================================
def main():
    while True:
        print("Выберите задание 1-3 4-Выход:")
        choice = checkYourSolution(3)
        if choice == 1:
            print("1.	Напишите функцию для определения количества слов в строке и определения самого длинного слова. – 2 балла ")
            lab2Task1()
        elif choice == 2:
            print("2.	Напишите функцию, которая будет принимать один аргумент.\n "
                  "Если в функцию передаётся словарь, отсортировать в порядке возрастания и убывания по значению ключей.\n "
                  "Если список, то посчитать кол-во букв и чисел в нём.\n  "
                  "Число – определить простое, или нет Строка – вывести все слова палиндромы.\n "
                  "Сделать проверку со всеми этими случаями. – 4 балла ")
            lab2Task2()
        elif choice == 3:
            print("3.	Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат. \n"
                  "Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j. – 2 балла ")
            lab2Task3()
        elif choice == 4:
            print("Произошёл выход")
            break

if __name__ == "__main__":
    main()