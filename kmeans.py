from sklearn.cluster import KMeans
import numpy as np

# Función para ejecutar K-Means con convergencia manual
def kmeans_converge(X, n_clusters=7, max_iter=300, tol=1e-4):
    kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, n_init=10, random_state=42)
    prev_centroids = None
    for i in range(max_iter):
        kmeans.fit(X)
        if prev_centroids is not None and np.allclose(kmeans.cluster_centers_, prev_centroids, atol=tol):
            print(f"Convergencia alcanzada en la iteración {i+1}")
            break
        prev_centroids = kmeans.cluster_centers_.copy()
    return kmeans
