import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interpolate

x = np.linspace(-3, 3, 150)
# print(x)
y = np.power(x, 2) + 0.1 * np.random.randn(150)
# print(y)
# spl = InterpolatedUnivariateSpline(x, y)
spl = interpolate.interp1d(x, y)
plt.plot(x, y, 'ro', ms=5)
xs = np.linspace(-3, 3, 150000000)
plt.plot(xs, spl(xs), 'g', lw=3, alpha=0.7)
plt.show()
