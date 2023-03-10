# Посчитать коэффициент линейной регрессии при заработной плате (zp), 
# используя градиентный спуск (без intercept).

import numpy as np

zp = zp.reshape((10,1))
ks = ks.reshape((10,1))

zp = np.hstack([np.ones((10,1)), zp])
b = np.linalg.inv(zp.T@zp)@zp.T@ks # 2.62
# a = 444.178