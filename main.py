def z1():
    spisok = []
    while (slovo:=str(input())) != "stop":
        spisok.append(slovo)
    print(" ".join(spisok))

def z2():
    spisok = []
    while (slovo:=str(input())) != "стоп":
        if "ф" in slovo or "Ф" in slovo:
            print("Это редкое слово")
        else:
            print("Это не редкое слово")

def z3():
    from random import randint
    k = 0
    kp=0
    while (k != 3):
        a = randint(1, 9)
        b = randint(1, 9)
        rez = input(str(a) + "+" + str(b) + "=")
        if rez == "stop":
            break
        if int(rez) == (a + b):
            kp+=1
            print("Правильно!")
        elif int(rez) != (a + b):
            k += 1
            print("Ответ неверный.")
        if k == 3:
            print("Игра окончена. Правильных ответов:", kp)

