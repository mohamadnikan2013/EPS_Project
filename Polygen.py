import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.qhull import ConvexHull
from shapely.geometry.polygon import Polygon


class MyPolygon:
    def __init__(self, vertex):
        self.vertex = vertex
        self.points = None
        self.hull = None
        self.polygon = None
        self.overlapping_area = 0

    def generate_convex_hull_unit_square(self):
        self.points = np.random.rand(self.vertex, 2)
        self.hull = ConvexHull(self.points)
        self.polygon = Polygon(Polygon(self.points).convex_hull)

    def generate_convex_hull_unit_circle(self):
        n = 0
        self.points = np.empty([1, 2])
        while n < self.vertex:
            x = np.random.rand(1, 2)
            if (x[0][0] - 0.5) * (x[0][0] - 0.5) + (x[0][1] - 0.5) * (x[0][1] - 0.5) <= .25:
                self.points = np.append(self.points, x, 0)
                n += 1

        self.points = np.delete(self.points, 0, 0)
        self.hull = ConvexHull(self.points)
        self.polygon = Polygon(Polygon(self.points).convex_hull)

    def generate_convex_hull_unit_equilateral_triangle(self):
        n = 0
        self.points = np.empty([1, 2])
        while n < self.vertex:
            x = np.random.rand(1, 2)
            if (x[0][0] >= np.math.sqrt(3) / 3 * x[0][1]) and (
                        x[0][0] <= 1 - (np.math.sqrt(3) / 3 * x[0][1])):
                self.points = np.append(self.points, x, 0)
                n += 1

        self.points = np.delete(self.points, 0, 0)
        self.hull = ConvexHull(self.points)
        self.polygon = Polygon(Polygon(self.points).convex_hull)

    def subscription(self, my_poly):
        p = MyPolygon(10)
        p.polygon = self.polygon.intersection(my_poly.polygon)
        x, y = p.polygon.exterior.coords.xy
        my_points = np.empty([1, 2])
        for i in range(len(x)):
            my_points = np.append(my_points, [[x[i], y[i]]], 0)

        my_points = np.delete(my_points, 0, 0)
        new_hull = ConvexHull(my_points)
        p.hull = new_hull
        p.points = my_points
        return p


p1 = MyPolygon(100)
# p2 = MyPolygon(10)
# p1.generate_convex_hull_unit_equilateral_triangle()
p1.generate_convex_hull_unit_circle()
# p3 = p1.subscription(p2)
fig, ax = plt.subplots()
circle = plt.Circle((0.5, 0.5), .5, color="black")
ax.add_artist(circle)

plt.plot(p1.points[:, 0], p1.points[:, 1], 'o')
for simplex in p1.hull.simplices:
    plt.plot(p1.points[simplex, 0], p1.points[simplex, 1], 'white')
plt.show()
# plt.plot(p2.points[:, 0], p2.points[:, 1], 'o')
# for simplex in p2.hull.simplices:
#     plt.plot(p2.points[simplex, 0], p2.points[simplex, 1], 'r-')

# for simplex in p3.hull.simplices:
#     plt.plot(p3.points[simplex, 0], p3.points[simplex, 1], 'g-')
