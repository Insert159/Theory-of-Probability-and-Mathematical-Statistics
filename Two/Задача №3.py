from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

n = 144 # кол-во испытаний
p = 1 / 2 # вероятность одного благоприятого события
k = 70 # кол-во благоприятных исходов
q = 1 - p # обратная вероятность вероятности p

result = combinations(n, k) * p**k * q**(n-k)
# Ответ: вероятность, что орел выпадет ровно 70 раз равна 0.062 или 6.2%