# В результате 10 независимых измерений некоторой величины X, 
# выполненных с одинаковой точностью,
# получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1 
# Предполагая, что результаты измерений подчинены нормальному закону распределения 
# вероятностей, оценить истинное значение величины X при помощи доверительного интервала, 
# покрывающего это значение с доверительной вероятностью 0,95.

from math import sqrt

sample = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
Z = 2.262

M = sum(sample ) / len(sample)
std = sqrt(sum((x - sum(sample ) / len(sample)) ** 2 for x in sample) / (len(sample)))

confidential_interval_a = M - Z * (std / sqrt(len(sample)))
confidential_interval_b = M + Z * (std / sqrt(len(sample)))

print(round (confidential_interval_a,2))
print(round(confidential_interval_b,2))

# Ответ: истиное значение величины Х, находится в данном доверительном интервале (6.28;6.90)