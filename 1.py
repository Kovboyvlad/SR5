def perevod(n,i):
    s = ''
    b = ''
    j1 = ''
    j2 = ''
    n1 = int(n)
    n2 = n - int(n)
    n3 = -(n - int(n))

    if i==8 and (int(n)-n!=0) and n>0:
        while n1 > 0:
            j1 = str(n1 % i) + j1
            n1 = n1 // i

        while n2!=8 and len(j2) < 23:                   #### (8) положительное дробное число
            n2 = n2 * i
            j2 = j2 + str(n2)[:1]
            if n2 >= 1:
                n2 -= int(str(n2)[:1])
            if n2 - int(str(n2)[:1])==0:
                break
        if len(j2)==23:
            s = j1 + '.' + j2 + '..'
        else:
            s = j1 + '.' + j2


    if (i==2 or i==8)and n>0 and int(n)-n==0:
        n = int(n)
        while n>0:                             #### положительное, не дробное число
            s = str(n%i) + s
            n = n//i


    if i==2 and n<0 and int(n)-n==0:
        n = int(n)
        n = n * (-1)
        while n > 0:
            b = str(n % i) + b
            n = n // i
        b = b.replace('1', '5')
        b = b.replace('0', '1')                        #### отрицательное, не дробное число
        b = b.replace('5', '0')
        b = int(b, base=2)
        b = b + 1
        while b > 0:
            s = str(b % i) + s
            b = b // i


    if i==2 and (int(n)-n!=0) and n>0:
        while n1 > 0:
            j1 = str(n1 % i) + j1
            n1 = n1 // i

        while n2 != 0 and len(j2) < 23:                   #### положительное дробное число
            n2 = n2 * i
            j2 = j2 + str(n2)[:1]
            if n2 >= 1:
                n2 -= 1
        if len(j2)==23:
            s = j1 + '.' + j2 + '..'
        else:
            s = j1 + '.' + j2


    if i==2 and (int(n)-n!=0) and n<0:
        n = int(n)
        n = n * (-1)
        while n > 0:
            b = str(n % i) + b
            n = n // i
        b = b.replace('1', '5')
        b = b.replace('0', '1')
        b = b.replace('5', '0')
        b = int(b, base=2)
        b = b + 1                                      #### отрицательное дробное число
        while b > 0:
            j1 = str(b % i) + j1
            b = b // i

        while n3 != 0 and len(j2) < 23:
            n3 = n3 * i
            j2 = j2 + str(n3)[:1]
            if n3 >= 1:
                n3 -= 1
            if len(j2) == 23:
                s = j1 + '.' + j2 + '..'
            else:
                s = j1 + '.' + j2




    return s

print("Примечание: перевод отрицательных чисел выполняется только во вторичной системе счисления, приносим свои извинения")
n = float(input("Введите число, которое хотите перевести: "))
if n==0:
    print("Введите какое-нибудь число")
    exit()
i = int(input("Введите в какую разрядность (2 или 8): "))
if not(i== 2 or i==8):
    print('Этот калькулятор создан только для перевода во вторичную или восьмеричную систему счисления')
    exit()
if n<0 and i == 8:
    print('Перевод не выполнится в восьмеричную систему счисления, если число отрицательное')
    exit()

print("Итоговая двоичная запись: ", perevod(n,i))