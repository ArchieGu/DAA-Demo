from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np
import matplotlib.pyplot as plt
points = np.random.rand(30, 2)   # 30 random points in 2-D
print(points)
hull = ConvexHull(points)
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    print(simplex)
    print(points[simplex, 0], points[simplex, 1])
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
plt.show()