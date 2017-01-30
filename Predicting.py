import matplotlib.pyplot as plt
import numpy as np


class Predicting():
    def __init__(self, deg, x, y, my_min=None, my_max=None):
        self.y = sorted(y)
        self.x = sorted(x)
        self.deg = deg
        if my_min:
            self.my_min = float(my_min)
        else:
            self.my_min = float(min(self.x))
        if my_max:
            self.my_max = float(my_max)
        else:
            self.my_max = float(max(self.x))
        self.minimum_mean_square_error_coefficients = self.minimum_mean_square_error()
        self.method_of_moment_coefficients = self.method_of_moment()
        self.show()

    def minimum_mean_square_error(self):
        return np.polyfit(self.x, self.y, self.deg)

    def method_of_moment(self):
        a = np.zeros(shape=(self.deg + 1, self.deg + 1))
        b = np.zeros(shape=(self.deg + 1, 1))
        ret = np.zeros(shape=self.minimum_mean_square_error_coefficients.shape)
        for i in range(self.deg + 1):
            excepted = 0
            for k in range(len(self.x)):
                try:
                    excepted += np.power((self.x[k]), (i + 1)) * self.y[k] * (
                        (self.x[k] - self.x[k - 1]) + (self.x[k] - self.x[k + 1])) / 2
                except:
                    if (k == 0):
                        excepted += np.power((self.x[k]), (i + 1)) * self.y[k] * (self.x[1] - self.x[k])
                    if (k == len(self.x) - 1):
                        excepted += np.power((self.x[k]), (i + 1)) * self.y[k] * (self.x[k] - self.x[k-1])

            b[i] = excepted
            coefficients = []
            for j in range(self.deg + 1):
                coefficients.append(
                    (np.math.pow(self.my_max, (j + i + 2)) - np.power(self.my_min, (j + i + 2))) / (j + i + 2))
            a[i] = coefficients
        x = np.linalg.solve(a, b)
        if np.allclose(np.dot(a, x), b):
            for i in range(self.deg):
                ret[self.deg - i] = x[i]
            return ret
        else:
            return False

    # def show_minimum_mean_square_error(self):
    #     xp = np.linspace(0, 3, 10000)
    #     p = np.poly1d(self.minimum_mean_square_error_coefficients)
    #     plt.plot(self.x, self.y, '.', xp, p(xp), '-')

    def show(self):
        pmmse = np.poly1d(self.minimum_mean_square_error_coefficients)
        pmm = np.poly1d(self.method_of_moment_coefficients)
        xp = np.linspace(self.my_min, self.my_max, 1000)
        plt.plot(self.x, self.y, '.', xp, pmmse(xp), '-', xp, pmm(xp), '--')
        # plt.xlim(min(0.9 * min(self.x), 1.1 * min(self.x)), 1.1 * max(self.x))
        # plt.ylim(min(0.2 * min(self.y), 5 * min(self.y)), 5 * max(self.y))
        plt.show()
        plt.savefig("static/Pre/graphobs.jpg")


def generate_data_from_uniform(my_min, my_max, n):
    return list(np.random.uniform(my_min, my_max, n)), [1 / (my_max - my_min)] * n


def generate_data_from_expotential(scale, n):
    x = list(np.random.exponential(scale, n))
    y = [np.exp(i / scale) / scale for i in x]

    return x, y


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
inter = Predicting(3, my_x, my_y, my_min, my_max)

"""
this part get data from data generator
"""
# x, y = generate_data_from_uniform(0, 1, 20000)
# # x, y = generate_data_from_expotential(1, 10000)
# pre = Predicting(50, x, y, min(x), max(x))
