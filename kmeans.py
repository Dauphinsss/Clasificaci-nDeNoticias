from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# Función para ejecutar K-Means con convergencia
def kmeans_converge(X, n_clusters, max_iter=300, tol=1e-6):
    kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, n_init=10, random_state=42, tol=tol)
    kmeans.fit(X)
    print(f"Convergencia alcanzada después de {kmeans.n_iter_} iteraciones.")
    return kmeans

# Función para buscar el mejor número de clusters en un rango determinado
def buscar_mejor_kmeans(X, min_clusters=2, max_clusters=15, n_iteraciones=5, max_iter=300, tol=1e-6):
    mejor_kmeans = None
    mejor_silueta = -1  # Silueta va de -1 a 1
    mejor_numero_clusters = None
    
    for n_clusters in range(min_clusters, max_clusters + 1):
        print(f"\nEvaluando K-Means con {n_clusters} clusters...")
        
        kmeans = kmeans_converge(X, n_clusters=n_clusters, max_iter=max_iter, tol=tol)
        labels = kmeans.predict(X)
        
        # Evaluar silueta
        silueta = silhouette_score(X, labels)
        print(f"Índice de Silueta para {n_clusters} clusters: {silueta}")
        
        if silueta > mejor_silueta:
            mejor_silueta = silueta
            mejor_kmeans = kmeans
            mejor_numero_clusters = n_clusters

    print(f"\nMejor número de clusters según silueta: {mejor_numero_clusters}")
    return mejor_kmeans