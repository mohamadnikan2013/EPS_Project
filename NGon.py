from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter
from scipy.spatial.qhull import ConvexHull
from shapely.geometry.point import Point
from shapely.geometry.polygon import Polygon


class MyPolygon:
    def __init__(self, sides=3):
        self.points = None
        self.hull = None
        self.polygon = None
        self.sides = sides
        self.areas = defaultdict(list)

    def generate_convex_hull_unit_square(self, samples):
        for i in range(samples):
            self.points = np.random.rand(3, 2)
            self.hull = ConvexHull(self.points)
            self.polygon = Polygon(Polygon(self.points).convex_hull)
            while len(self.hull.vertices) < self.sides:
                rand = np.random.rand(1, 2)
                point = Point(rand[0][0], rand[0][1])
                if not self.polygon.contains(point):
                    self.points = np.concatenate((self.points, rand))
                    self.hull = ConvexHull(self.points)
                    self.polygon = Polygon(Polygon(self.points).convex_hull)

            self.areas[self.sides].append(self.polygon.area)

            # fig, ax = plt.subplots()
            # ax.add_patch(
            #     patches.Rectangle(
            #         (0, 0),  # (x,y)
            #         1,  # width
            #         1,  # height
            #         facecolor="Black"
            #     )
            # )
            # plt.plot(p1.points[:, 0], p1.points[:, 1], 'o')
            # for simplex in self.hull.simplices:
            #     plt.plot(p1.points[simplex, 0], p1.points[simplex, 1], 'white')
            # plt.show()

    def generate_convex_hull_unit_circle(self, samples):
        for i in range(samples):
            n = 0
            self.points = np.empty([1, 2])
            while n < 3:
                rand = np.random.rand(1, 2)
                if (rand[0][0] - 0.5) * (rand[0][0] - 0.5) + (rand[0][1] - 0.5) * (rand[0][1] - 0.5) <= .25:
                    self.points = np.concatenate((self.points, rand))
                    n += 1
            self.points = np.delete(self.points, 0, 0)
            self.hull = ConvexHull(self.points)
            self.polygon = Polygon(Polygon(self.points).convex_hull)
            while len(self.hull.vertices) < self.sides:
                rand = np.random.rand(1, 2)
                point = Point(rand[0][0], rand[0][1])
                if not self.polygon.contains(point) and (
                                    (rand[0][0] - 0.5) * (rand[0][0] - 0.5) + (rand[0][1] - 0.5) * (
                                        rand[0][1] - 0.5) <= .25):
                    self.points = np.concatenate((self.points, rand))
                    self.hull = ConvexHull(self.points)
                    self.polygon = Polygon(Polygon(self.points).convex_hull)

            self.areas[self.sides].append(self.polygon.area)

            # fig, ax = plt.subplots()
            # circle = plt.Circle((0.5, 0.5), .5, color="black")
            # ax.add_artist(circle)
            # plt.plot(p1.points[:, 0], p1.points[:, 1], 'o')
            # for simplex in p1.hull.simplices:
            #     plt.plot(p1.points[simplex, 0], p1.points[simplex, 1], 'white')
            # plt.show()

    def generate_convex_hull_unit_equilateral_triangle(self, samples):
        for i in range(samples):
            n = 0
            self.points = np.empty([1, 2])
            while n < 3:
                rand = np.random.rand(1, 2)
                if (rand[0][0] >= np.math.sqrt(3) / 3 * rand[0][1]) and (
                            rand[0][0] <= 1 - (np.math.sqrt(3) / 3 * rand[0][1])):
                    self.points = np.concatenate((self.points, rand))
                    n += 1

            self.points = np.delete(self.points, 0, 0)
            self.hull = ConvexHull(self.points)
            self.polygon = Polygon(Polygon(self.points).convex_hull)
            while len(self.hull.vertices) < self.sides:
                rand = np.random.rand(1, 2)
                point = Point(rand[0][0], rand[0][1])
                if not self.polygon.contains(point) and (
                            (rand[0][0] >= np.math.sqrt(3) / 3 * rand[0][1]) and (
                                    rand[0][0] <= 1 - (np.math.sqrt(3) / 3 * rand[0][1]))):
                    self.points = np.concatenate((self.points, rand))
                    self.hull = ConvexHull(self.points)
                    self.polygon = Polygon(Polygon(self.points).convex_hull)

            self.areas[self.sides].append(self.polygon.area)
            # fig, ax = plt.subplots()
            # ax.add_patch(
            #     patches.RegularPolygon(
            #         (0.5, np.sqrt(3) / 6),
            #         3,
            #         np.sqrt(3) / 3,
            #         facecolor="Black"
            #     )
            # )
            # plt.plot(p1.points[:, 0], p1.points[:, 1], 'o')
            # for simplex in self.hull.simplices:
            #     plt.plot(p1.points[simplex, 0], p1.points[simplex, 1], 'white')
            # plt.show()


p1 = MyPolygon(3)
for i in range(3, 70):
    p1.sides = i
    print(p1.sides)
    p1.generate_convex_hull_unit_circle(20)
y = []
for i in p1.areas.values():
    y.append(np.mean(i))

# make up some data in the interval ]0, 1[
x = list(p1.areas.keys())
# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('linear')
plt.xscale('log')
plt.title('log')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
plt.show()
