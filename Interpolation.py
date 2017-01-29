import matplotlib.pyplot as plt
import numpy as np


class Interpolation():
    def __init__(self, deg, x, y, my_min, my_max):
        self.y = y
        self.x = x
        self.deg = deg
        self.my_min = my_min
        self.my_max = my_max
        self.minimum_mean_square_error_coefficients = self.minimum_mean_square_error()
        self.method_of_moment_coefficients = self.method_of_moment()

    def minimum_mean_square_error(self):
        return np.polyfit(self.x, self.y, self.deg)

    def method_of_moment(self):
        a = np.zeros(shape=(self.deg, self.deg))
        b = np.zeros(shape=(self.deg, 1))
        for i in range(self.deg):
            excepted = 0
            for k in range(self.deg):
                excepted += np.power((self.x[k]), (i + 1)) * self.y[k]
            b[i] = excepted
            coefficients = []
            for j in range(self.deg):
                coefficients.append(
                    (np.power(self.my_max, (j + i + 2)) - np.power(self.my_min, (j + i + 2))) / (j + i + 2))
            a[i] = coefficients
        x = np.linalg.solve(a, b)
        if np.allclose(np.dot(a, x), b):
            return x
        else:
            return False

    def show_minimum_mean_square_error(self):
        xp = np.linspace(0, 3, 10000)
        p = np.poly1d(self.minimum_mean_square_error_coefficients)
        plt.plot(self.x, self.y, '.', xp, p(xp), '-')


"""
this part get data from input
"""
fp = open("Observation.txt", 'r')
lines = []
for line in fp.readlines():
    lines.append((line.split()))
my_min = float(lines[0][0])
my_max = float(lines[0][1])
lines.pop(0)
my_x = []
my_y = []
for i in lines:
    my_x.append(float(i[0]))
    my_y.append(float(i[1]))
inter = Interpolation(3, my_x, my_y, my_min, my_max)

"""
this part get data from data generator
"""
