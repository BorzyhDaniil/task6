import codecs
import string
import numpy as np
myfile = codecs.open(r"text.txt", "r", encoding='utf-8')
t = myfile.read()
for s in (string.punctuation+"—«»"):
    if s in t:
        t = t.replace(s, '')
t = t.lower()
text = t.split()
print("Введите первоначальные слова")
prefix = input().split()
print("Введите количество необходимых слов")
n = int(input())
print("Введите количество слов, которым производится поиск")
dd = int(input())
comp = True
words = list()
ln = len(prefix)
dl = len(prefix)
for p in range(n):
    for i in range(len(text)-ln):
        if prefix[ln-dl] == text[i]:
            for j in range(dl):
                if prefix[ln-dl+j] != text[i+j]:
                    comp = False
            if comp:
                words.append(text[i+dl])
            comp = True
    if len(words) == 0:
        print ("Такого префикса не найдено")
        break
    else:
        prefix.append(np.random.choice(words))
        ln = len(prefix)
        if dd > ln:
            dl = len(prefix)
        else:
            dl = dd
        words.clear()
if ln >= n:
    print("Сгенерированный текст:")
    print(" ".join(prefix))
