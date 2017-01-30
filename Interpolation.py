import random
from Predicting import Predicting
from NHull import NHull
from NGon import MyPolygon
import numpy as np


def section1():
    my_vertexes = [5, 10, 15, 100, 200, 500, 4000]
    distributions = []
    for i in my_vertexes:
        areas = []
        for j in range(10 ** 4):
            m1 = NHull(i)
            m2 = NHull(i)
            m3 = m1.subscription(m2)
            areas.append(m3.polygon.area)
        # areas = sorted(areas)
        dis = [0 for i in range(100)]
        for i in areas:
            dis[int(i // 0.01)] += 1

        x = []
        y = []
        l = 0
        while l < 5:
            rnd = random.randint(0, 99)
            kaka = dis[rnd]
            if kaka > 0:
                x.append(rnd / 100 + 0.005)
                y.append(kaka)
                l += 1

        pre = Predicting(5, x, y, min(x), max(x))
        distributions.append(pre)
        print(pre.method_of_moment_coefficients)


def section2():
    p1 = MyPolygon(3)
    p2 = MyPolygon(3)
    p3 = MyPolygon(3)
    for i in range(3, 20):
        p1.sides = i
        p1.generate_convex_hull_unit_circle(100)
        print(i)

    for i in range(3, 20):
        p2.sides = i
        p2.generate_convex_hull_unit_square(100)
        print(i)

    for i in range(3, 15):
        p3.sides = i
        p3.generate_convex_hull_unit_equilateral_triangle(100)
        print(i)

    rnd = np.random.randint(3, 20, 8, )
    pre1 = Predicting(30, rnd, [np.mean(p1.areas[i]) for i in rnd])
    pre2 = Predicting(30, rnd, [np.mean(p2.areas[i]) for i in rnd])
    pre3 = Predicting(30, rnd, [np.mean(p3.areas[i]) for i in rnd])


section2()
