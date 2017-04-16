from tkinter.filedialog import *

def open_file():
    op = askopenfile()
    op = str(op)
    st = op.find('name=') + 6
    fin = op.find('mode') - 2
    path = op[st:fin]
    return path

mode = input("Выберите режим:\n1 - индекс совпадения\n2 - средний индекс совпадения\n3 - шифр виженера ")
if mode == "1":
    print("Выберите первый файл")
    path = open_file()
    f = open(path, 'r')
    plaintext = f.read()
    f.close()

    print("Выберите второй файл")
    path = open_file()
    f = open(path, 'r')
    plaintext2 = f.read()
    f.close()

    l1 = len(plaintext)
    l2 = len(plaintext2)
    if l1 > l2:
        plaintext = plaintext[0:l2]
        print("Первый текст больше второго. Итоговая длина " + str(len(plaintext)))
    elif l2 > l1:
        plaintext2 = plaintext2[0:l1]
        print("Второй текст больше первого. Итоговая длина " + str(len(plaintext2)))
    index = 0
    for i in range(len(plaintext)):
        if plaintext[i] == plaintext2[i]:
            index += 1
    index = index * (1/len(plaintext)) * 100
    print(index)

elif mode == "2":
    print("Выберите первый файл")
    path = open_file()
    f = open(path, 'r')
    plaintext = f.read()
    plaintext = plaintext.lower()
    plaintext = plaintext.replace(" ", "")
    f.close()

    print("Выберите второй файл")
    path = open_file()
    f = open(path, 'r')
    plaintext2 = f.read()
    plaintext2 = plaintext2.lower()
    plaintext2 = plaintext2.replace(" ", "")
    f.close()

    print("Выберите файл с алфавитом")
    path = open_file()
    f = open(path, 'r')
    alph = f.read()
    f.close()

    l1 = len(plaintext)
    l2 = len(plaintext2)
    if l1 > l2:
        plaintext = plaintext[0:l2]
        print("Первый текст больше второго. Итоговая длина " + str(len(plaintext)))
    elif l2 > l1:
        plaintext2 = plaintext2[0:l1]
        print("Второй текст больше первого. Итоговая длина " + str(len(plaintext2)))

    index = 0
    for i in range(0, len(alph)):
        p1 = plaintext.count(alph[i]) / len(plaintext)
        p2 = plaintext2.count(alph[i]) / len(plaintext)
        index += p1 * p2
    index *= 100
    print(index)

elif mode == "3":
    print("Выберите файл с алфавитом")
    path = open_file()
    f = open(path, 'r')
    alph = f.read()
    f.close()
    dictalph = dict()
    for i in range(len(alph)):
        dictalph[alph[i]] = i

    print("Выберите файл с текстом")
    path = open_file()
    f = open(path, 'r')
    plaintext = f.read()
    plaintext = plaintext.lower()
    for symbol in plaintext:
        if symbol not in alph:
            plaintext = plaintext.replace(symbol, "")
    f.close()

    print("Выберите файл с ключом")
    path = open_file()
    f = open(path, 'r')
    key = f.read()
    f.close()

    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += alph[(dictalph[plaintext[i]] + dictalph[key[i % len(key)]]) % len(alph)]
    f = open("ciphertext", "w")
    f.write(ciphertext)
    f.close()

    l1 = int(input("Введите первый сдвиг: "))
    l2 = int(input("Введите последний сдвиг: "))
    for l in range(l1, l2 + 1):
        plaintext2 = plaintext[l:] + plaintext[:l]
        index = 0
        for i in range(len(plaintext)):
            if plaintext[i] == plaintext2[i]:
                index += 1
        index *= 1 / len(plaintext) * 100
        print(index)