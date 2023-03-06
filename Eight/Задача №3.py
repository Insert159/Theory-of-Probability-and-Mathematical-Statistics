# Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.

import math
import numpy as np
import scipy.stats as stats

d = 25
n = 27
m = 174.2
a = 0.05

z = stats.norm.ppf(1-(a / 2))

result1 = round (m - z * (math.sqrt(d) / math.sqrt(n)),3)
result2 =round  (m + z * (math.sqrt(d) / math.sqrt(n)),3)
print(f'Доверительный интервал для оценки математического ожидания a с надежностью 0.95 = ({result1},{result2})')

# Ответ: [172.314, 176.086]