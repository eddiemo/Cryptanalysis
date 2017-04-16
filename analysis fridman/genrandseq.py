import random
alph = "abcdefghijklmnopqrstuvwxyz"
alph_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
f = open("randfile3.txt", "w")
for i in range(0, 31000):
    f.write(alph[random.randint(0, len(alph) - 1)])
f.close()