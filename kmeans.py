from sklearn.cluster import KMeans
import numpy as np

# Función para ejecutar K-Means con convergencia manual
def kmeans_converge(X, n_clusters, max_iter=300, tol=1e-6):
    kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter, n_init=10, random_state=42)
    prev_centroids = None
    for i in range(max_iter):
        kmeans.fit(X)
        # Verificamos la convergencia comparando los centroides
        if prev_centroids is not None and np.allclose(kmeans.cluster_centers_, prev_centroids, atol=tol):
            print(f"Convergencia alcanzada en la iteración {i+1}")
            break
        prev_centroids = kmeans.cluster_centers_.copy()
    return kmeans

# Función para buscar el mejor número de clusters en un rango determinado
def buscar_mejor_kmeans(X, min_clusters=2, max_clusters=15, n_iteraciones=5, max_iter=300, tol=1e-6):
    mejor_kmeans = None
    mejor_convergencia = float('inf')  # Inicializamos con un valor muy alto
    mejor_numero_clusters = None
    mejores_centroides = None

    # Iterar sobre el rango de números de clusters
    for n_clusters in range(min_clusters, max_clusters + 1):
        print(f"\nEvaluando K-Means con {n_clusters} clusters...")
        
        # Inicializar el acumulador de la convergencia
        convergencia_promedio = 0
        
        # Realizar varias iteraciones para evaluar convergencia
        for i in range(n_iteraciones):
            print(f"  Iteración {i+1}...")
            kmeans = kmeans_converge(X, n_clusters=n_clusters, max_iter=max_iter, tol=tol)
            
            # Agregar la inercia de este KMeans al total de convergencia
            convergencia_promedio += kmeans.inertia_
        
        # Promediar la convergencia de las iteraciones
        convergencia_promedio /= n_iteraciones
        
        # Imprimir la convergencia promedio para este número de clusters
        print(f"\nConvergencia promedio para {n_clusters} clusters: {convergencia_promedio}")

        # Si el modelo actual tiene mejor convergencia, lo guardamos
        if convergencia_promedio < mejor_convergencia:
            mejor_convergencia = convergencia_promedio
            mejor_kmeans = kmeans
            mejor_numero_clusters = n_clusters
            mejores_centroides = kmeans.cluster_centers_

    print(f"\nMejor K-Means: {mejor_numero_clusters} clusters con convergencia: {mejor_convergencia}")
    return mejor_kmeans