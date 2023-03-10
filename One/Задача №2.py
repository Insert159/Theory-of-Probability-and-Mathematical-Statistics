"На входной двери подъезда установлен кодовый замок, содержащий десять кнопок"
"с цифрами от 0 до 9. Код содержит три цифры, которые нужно нажать одновременно."
"Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?"

import numpy as np


# формула для вычисления сочетаний
def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


c = combinations(10, 3) # число сочетаний трех цифр из цифр от 0 до 9
p = 1/c # вероятность того, что человек, не знающий код, откроет дверь с первой попытки
print(round(p, 4))