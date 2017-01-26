import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.qhull import ConvexHull
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point


class MyPolygon:
    def __init__(self, sides):
        self.points = None
        self.hull = None
        self.polygon = None
        self.sides = sides

    # TODO SAVE IMages
    def generate_convex_hull_unit_square(self):
        self.points = np.random.rand(3, 2)
        self.hull = ConvexHull(self.points)
        self.polygon = Polygon(Polygon(self.points).convex_hull)
        while len(self.hull.vertices) < self.sides:
            # print(len(self.hull.vertices))
            rand = np.random.rand(1, 2)
            point = Point(rand[0][0], rand[0][1])
            if not self.polygon.contains(point):
                # self.hull.add_points(rand)
                self.points = np.concatenate((self.points, rand))
                self.hull = ConvexHull(self.points)
                self.polygon = Polygon(Polygon(self.points).convex_hull)

    def generate_convex_hull_unit_circle(self):
        n = 0
        self.points = np.empty([1, 2])
        while n < 3:
            rand = np.random.rand(1, 2)
            if (rand[0][0] - 0.5) * (rand[0][0] - 0.5) + (rand[0][1] - 0.5) * (rand[0][1] - 0.5) <= .25:
                self.points = np.concatenate((self.points, rand))
                n += 1
        self.hull = ConvexHull(self.points)
        self.polygon = Polygon(Polygon(self.points).convex_hull)
        while len(self.hull.vertices) < self.sides:
            rand = np.random.rand(1, 2)
            point = Point(rand[0][0], rand[0][1])
            if not self.polygon.contains(point) and (
                                (rand[0][0] - 0.5) * (rand[0][0] - 0.5) + (rand[0][1] - 0.5) * (
                                    rand[0][1] - 0.5) <= .25):
                # self.hull.add_points(rand)
                self.points = np.concatenate((self.points, rand))
                self.hull = ConvexHull(self.points)
                self.polygon = Polygon(Polygon(self.points).convex_hull)

    def generate_convex_hull_unit_equilateral_triangle(self):
        n = 0
        self.points = np.empty([1, 2])
        while n < 3:
            rand = np.random.rand(1, 2)
            if (rand[0][0] >= np.math.sqrt(3) / 3 * rand[0][1]) and (
                        rand[0][0] <= 1 - (np.math.sqrt(3) / 3 * rand[0][1])):
                self.points = np.concatenate((self.points, rand))
                n += 1
        self.hull = ConvexHull(self.points)
        self.polygon = Polygon(Polygon(self.points).convex_hull)
        while len(self.hull.vertices) < self.sides:
            print(len(self.hull.vertices))
            rand = np.random.rand(1, 2)
            point = Point(rand[0][0], rand[0][1])
            if not self.polygon.contains(point) and (
                        (rand[0][0] >= np.math.sqrt(3) / 3 * rand[0][1]) and (
                                rand[0][0] <= 1 - (np.math.sqrt(3) / 3 * rand[0][1]))):
                # self.hull.add_points(rand)
                self.points = np.concatenate((self.points, rand))
                self.hull = ConvexHull(self.points)
                self.polygon = Polygon(Polygon(self.points).convex_hull)


p1 = MyPolygon(40)
p1.generate_convex_hull_unit_equilateral_triangle()
print(len(p1.points))
# p1 = MyPolygon(100)
# # p2 = MyPolygon(10)
# # p1.generate_convex_hull_unit_equilateral_triangle()
# p1.generate_convex_hull_unit_circle()
# # p3 = p1.subscription(p2)
# fig, ax = plt.subplots()
# circle = plt.Circle((0.5, 0.5), .5, color="black")
# ax.add_artist(circle)
#
# plt.plot(p1.points[:, 0], p1.points[:, 1], 'o')
# for simplex in p1.hull.simplices:
#     plt.plot(p1.points[simplex, 0], p1.points[simplex, 1], 'white')
# plt.show()
# # plt.plot(p2.points[:, 0], p2.points[:, 1], 'o')
# # for simplex in p2.hull.simplices:
# #     plt.plot(p2.points[simplex, 0], p2.points[simplex, 1], 'r-')
#
# # for simplex in p3.hull.simplices:
# #     plt.plot(p3.points[simplex, 0], p3.points[simplex, 1], 'g-')
