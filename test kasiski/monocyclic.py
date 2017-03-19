import random
from tkinter.filedialog import *

def open_file():
    op = askopenfile()
    op = str(op)
    st = op.find('name=') + 6
    fin = op.find('mode') - 2
    path = op[st:fin]
    return path

def gen_key(n): #генерация одной моноциклической перестановки
    arr = [0] * n
    for i in range (0, n):
        arr[i] = i
    j = random.randint(0, n - 1)
    for i in range (0, n):
        arr[i], arr[j] = arr[j], arr[i]
    ans = [0] * n
    for i in range (0, n):
        ans[arr[i]] = arr[(i + 1) % n]
    return ans

def is_monocyclic(perm):
    first = perm[0]
    tmp = first
    i = 0
    while i < len(perm) and first != perm[tmp - 1]:
        i += 1
        tmp = perm[tmp - 1]
    return i == (len(perm) - 1) and first == perm[tmp - 1]

def gen_all_keys(n, permm):
    ans = []
    perm = permm.copy()
    def gen_keys(k = 0): #генерация всех моноциклических перестановок
        if k == n:
            if is_monocyclic(perm):
                ans.append(perm.copy())
        else:
            for j in range(k, len(perm)):
                perm[k], perm[j] = perm[j], perm[k]
                gen_keys(k + 1)
                perm[k], perm[j] = perm[j], perm[k]
    gen_keys()
    return ans

def gen_start_perm(n):
    perm = []
    for i in range(0, n):
        perm.append(i + 1)
    return perm

def encrypt(text, key):
    ciphertext = ""
    while not len(text) % len(key) == 0:
        text += text[random.randint(0, len(text) - 1)]
    for i in range(0, len(text)):
        ciphertext += str(text[((i // len(key)) * len(key)) + key[i % len(key)]])
    return ciphertext

def decrypt(text, key):
    invkey = [0]*len(key)
    for i in range(0, len(key)):
        invkey[key[i]] = i
    decrypttext = ""
    for i in range(0, len(text)):
        decrypttext += text[((i // len(key)) * len(key)) + invkey[i % len(key)]]
    return decrypttext

def getdistances(text):
    checkedblocks = set()
    dists = []
    minblock = 3
    maxblock = 10
    for bl in range(minblock, min(maxblock + 1, len(text))):
        for i in range(len(text) - 2 * bl + 1):
            block = text[i:i + bl]
            if block not in checkedblocks:
                checkedblocks.add(block)
                pos = i
                while pos != -1:
                    dist = pos
                    pos = text.find(block, pos + bl)
                    if pos != -1:
                        dist = pos - dist
                        if dist > 0:
                            dists.append(dist)
    return dists

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def getmostfreqgcd(dists):
    freqs = dict()
    for i in range(len(dists)):
        for j in range(i + 1, len(dists)):
            g = gcd(dists[i], dists[j])
            if g < 3:
                continue
            if g in freqs.keys():
                freqs[g] += 1
            else:
                freqs[g] = 1
    f = open("test kasiski\\freqs", 'w')
    f.write(str(freqs))
    f.close()
    return max(freqs, key=lambda i:freqs[i])


mode = print("Выберите режим работы программы:\n1 - генерация ключа\n2 - шифрование\n3 - тест казиски\n4 - дешифрование с ключом\n5 - перебор ключа и дешифрование\n6 - выход из программы")
while True:
    mode = input("Режим ")
    if mode == "1":
        lenkey = int(input("Введите длину ключа: "))
        key = gen_key(lenkey)
        f = open("test kasiski\\filekey", 'w')
        for i in range(0, lenkey):
            f.write(str(key[i]) + " ")
        f.close()
        print("Ключ сгенерирован")
    elif mode == "2":
        print("Выберите файл для шифрования")
        path = open_file()
        f = open(path, 'r')
        plaintext = f.read()
        f.close()
        plaintext = plaintext.lower()
        i = 0
        while i < len(plaintext):
            if (not (plaintext[i] >= "a" and plaintext[i] <= "z")) and (not (plaintext[i] >= "а" and plaintext[i] <= "я")) and \
                    (not(plaintext[i] == "ё") and (not (plaintext[i] >= "0" and plaintext[i] <= "9"))):
                plaintext = plaintext.replace(plaintext[i], "")
            else:
                i += 1
        print("Выберите файл с ключом")
        f = open(open_file(), 'r')
        keytext = f.read()
        f.close()
        keytextsplt = str(keytext).split()
        key = []
        for i in range(0, len(keytextsplt)):
            key.append(int(keytextsplt[i]))
        ciphertext = encrypt(plaintext, key)
        f = open("test kasiski\\ciphertext", 'w')
        f.write(ciphertext)
        f.close()
        print("Текст из выбранного файла успешно зашифрован")
    elif mode == "3":
        print("Выберите файл с текстом для выполнения теста казиски")
        path = open_file()
        f = open(path, 'r')
        ciphertext = f.read()
        f.close()
        f = open("test kasiski\\lenkey", 'w')
        f.write(str(getmostfreqgcd(getdistances(ciphertext))))
        f.close()
        print("Тест казиски успешно завершен")
    elif mode == "4":
        print("Выберите файл для дешифрования")
        path = open_file()
        f = open(path, 'r')
        plaintext = f.read()
        f.close()
        print("Выберите файл с ключом")
        f = open(open_file(), 'r')
        keytext = f.read()
        f.close()
        keytextsplt = str(keytext).split()
        key = []
        for i in range(0, len(keytextsplt)):
            key.append(int(keytextsplt[i]))
        deciphertext = decrypt(plaintext, key)
        f = open("test kasiski\\decrypttext", 'w')
        f.write(deciphertext)
        f.close()
        print("Дешифрование по выбранному ключу выполнено успешно")
    elif mode == "5":
        print("Выберите файл для дешифрования")
        path = open_file()
        f = open(path, 'r')
        plaintext = f.read()
        f.close()
        print("Выберите файл c предпосчитанной тестом казиски длиной ключа")
        path = open_file()
        f = open(path, 'r')
        lenkey = int(f.read())
        f.close()
        startperm = gen_start_perm(lenkey)
        perms = gen_all_keys(lenkey, startperm)
        f = open("test kasiski\\bruteforcedecrypttexts", 'w')
        for perm in perms:
            newperm = []
            for i in range(len(perm)):
                newperm.append(perm[i] - 1)
            key = [0] * lenkey
            for i in range(0, lenkey):
                key[newperm[i]] = newperm[(i + 1) % lenkey]
            deciphertext = decrypt(plaintext, key)
            f.write(str(key) + "\n")
            f.write(deciphertext + "\n")
            f.write("\n")
        f.close()
        print("Дешифрование с перебором ключей успешно выполнено")
    elif mode == "6":
        print("Пока-пока!")
        exit(0)
    else:
        print("Неправильно  режим, сделайте выбор снова")