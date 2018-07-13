import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1, 2, 3],
              [4, 5, 5],
              [8, 8, 8],
              [6, 6, 1],
              [9, 11, 7],
              [5, 8, 9]])
clf = KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.", "r.", "c."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=150, linewidths=5)
plt.show()
