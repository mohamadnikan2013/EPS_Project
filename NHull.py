import math
import os

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.qhull import ConvexHull
from shapely.geometry.polygon import Polygon


# TODO for all N and def only for distribution and else
class NHull:
    def __init__(self, vertex):
        self.vertex = vertex
        self.points = None
        self.hull = None
        self.polygon = None
        # self.overlapping_area = 0

    def generate_convex_hull(self):
        self.points = np.random.rand(self.vertex, 2)
        self.hull = ConvexHull(self.points)
        self.polygon = Polygon(Polygon(self.points).convex_hull)

    def subscription(self, my_poly):
        p = NHull(self.vertex)
        try:
            p.polygon = self.polygon.intersection(my_poly.polygon)
            x, y = p.polygon.exterior.coords.xy
            my_points = np.empty([1, 2])
            for i in range(len(x)):
                my_points = np.append(my_points, [[x[i], y[i]]], 0)

            my_points = np.delete(my_points, 0, 0)
            new_hull = ConvexHull(my_points)
            p.hull = new_hull
            p.points = my_points
        except:
            pass
        return p


def estimating_the_distribution(vertex, samples):
    data = []
    for i in range(samples):
        p1 = NHull(vertex)
        p2 = NHull(vertex)
        p1.generate_convex_hull()
        p2.generate_convex_hull()
        p3 = p1.subscription(p2)
        # here for visualize and can removed for performance
        # plt.plot(p1.points[:, 0], p1.points[:, 1], 'o')
        # plt.plot(p2.points[:, 0], p2.points[:, 1], 'o')
        # for simplex in p1.hull.simplices:
        #     plt.plot(p1.points[simplex, 0], p1.points[simplex, 1], 'b-')
        # for simplex in p2.hull.simplices:
        #     plt.plot(p2.points[simplex, 0], p2.points[simplex, 1], 'g-')
        # if not os.path.exists("static/NHull/"+str(vertex)+"/sample" + str(i)):
        #     os.makedirs("static/NHull/"+str(vertex)+"/sample" + str(i))
        # plt.savefig("static/NHull/"+str(vertex)+"/sample" + str(i) + "/points.jpg")
        # plt.close()
        # for simplex in p1.hull.simplices:
        #     plt.plot(p1.points[simplex, 0], p1.points[simplex, 1], 'g-')
        # for simplex in p2.hull.simplices:
        #     plt.plot(p2.points[simplex, 0], p2.points[simplex, 1], 'r-')
        # if p3.polygon.area>0:
        #     for simplex in p3.hull.simplices:
        #         plt.plot(p3.points[simplex, 0], p3.points[simplex, 1], 'b-')
        # plt.savefig("static/NHull/"+str(vertex)+"/sample" + str(i) + "/Hull.jpg")
        # plt.close()
        data.append(p3.polygon.area)
    y = [0 for i in range(100)]
    for i in data:
        y[math.ceil(i / 0.01) - 1] += 1
    y_pos = np.arange(100)
    performance = y
    plt.bar(y_pos, performance, align='center', alpha=1)
    plt.xticks(y_pos, [])
    if not os.path.exists("static/NHull/bar_charts/"):
        os.makedirs("static/NHull/bar_charts/")
    plt.savefig("static/NHull/bar_charts/bar" + str(vertex) + "jpg")
    print(data)


my_vertexes = [5, 10, 15, 100, 200, 500, 4000]
for j in my_vertexes:
    estimating_the_distribution(j, 10)
