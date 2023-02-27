# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
# для второй - 0.2, для третьей - 0.25.
# Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали
# б). только две детали
# в). хотя бы одна деталь
# г). от одной до двух деталей?

p1 = 0.1
p2 = 0.2
p3 = 0.25

# а.) все детали выйдут из строя
a = p1*p2*p3
# Ответ: 0.005000000000000001 или ~ 0.5%

# б.) только две детали выйдут из строя
# тут три варианта: либо 1-я останется работать, либо вторая будет работать, либо третья будет работать
# умножаем вероятность того, что деталь работает (1 - вероятность, что деталь выйдет из строя)
# на вероятности, что детали выйдут из строя

b = 0.9*p2*p3 + 0.8*p1*p3 + 0.75*p1*p2
# Ответ 0.08 или ~ 8%

# в.) хотя бы одна деталь выйдет из строя
c = 1 - 0.9*0.8*0.75
# Ответ: 0.45999999999999996 или ~ 45.99%

# г.) от одной до двух деталей

d = 1 - 0.9*0.8*0.75 - a
# Ответ: 0.45499999999999996 или ~ 45.49%