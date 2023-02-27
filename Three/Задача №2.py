# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень.
# Вероятность попадания
# для первого спортсмена равна 0.9,
# для второго — 0.8,
# для третьего — 0.6.
# Найти вероятность того, что выстрел произведен:
# a). первым спортсменом
# б). вторым спортсменом
# в). третьим спортсменом

p1 = 0.9
p2 = 0.8
p3 = 0.6

# используем формулу Байеса: P(B|A)=P(B)⋅P(A|B)/P(A)

pA = 1/3*0.9+1/3*0.8+1/3*0.6
# 0.7666666666666666

p1 = 1/3*0.9/pA
# Ответ: 0.391304347826087 или ~ 39.13%
p2 = 1/3*0.8/pA
# Ответ: 0.3478260869565218 или ~ 34.78%
p3 = 1/3*0.6/pA
# Ответ 0.2608695652173913 или ~ 26.08%