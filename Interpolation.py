import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.sandbox.regression import gmm


class Interpolation():
    def __init__(self, deg, x, y):
        self.y = y
        self.x = x
        self.deg = deg
        self.minimum_mean_square_error_coefficients = self.minimum_mean_square_error()

    def minimum_mean_square_error(self):
        return np.polyfit(self.x, self.y, self.deg)

    def method_of_moment(self):
        pass

    def show_minimum_mean_square_error(self):
        xp = np.linspace(0, 3, 10000)
        p = np.poly1d(self.minimum_mean_square_error_coefficients)
        plt.plot(self.x, self.y, '.', xp, p(xp), '-')
