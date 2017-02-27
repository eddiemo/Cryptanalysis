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
    ans[j] = 0
    for i in range (0, n):
        ans[arr[i]] = arr[(i + 1) % n]
    return ans

def is_monocyclic(perm):
    pass

def gen_all_keys(): #генерация всех моноциклических перестановок
    pass

def encrypt(text, key):
    ciphertext = ""
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

lenkey = int(input("Введите длину ключа: "))
key = gen_key(lenkey)
f = open("file_key", 'w')
for i in range(0, lenkey):
    f.write(str(key[i]) + " ")
f.close()

print("Выберите файл для шифрования")
path = open_file()
f = open(path, 'r')
plaintext = f.read()
f.close()
plaintext = plaintext.lower()
i = 0
while i < len(plaintext):
    if (not (plaintext[i] >= "a" and plaintext[i] <= "z")) and (not (plaintext[i] >= "а" and plaintext[i] <= "я")) and \
            (not(plaintext[i] == "ё")):
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
f = open("ciphertext", 'w')
f.write(ciphertext)
f.close()

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
f = open("decrypttext", 'w')
f.write(deciphertext)
f.close()
