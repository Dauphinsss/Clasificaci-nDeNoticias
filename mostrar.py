import pandas as pd
import tkinter as tk
from tkinter import scrolledtext

def show_news(csv_file):
    # Cargar el archivo CSV
    df = pd.read_csv(csv_file)

    # Agrupar las noticias por su número de cluster
    clustered_news = df.groupby('cluster')['news'].apply(list).reset_index()

    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    root.title("Noticias por Cluster")
    root.geometry("800x600")

    # Función que se llama cuando se hace clic en un cluster
    def show_news(cluster):
        # Limpiar el área de texto
        news_text.delete(1.0, tk.END)
        
        # Obtener las noticias del cluster seleccionado
        news_list = clustered_news[clustered_news['cluster'] == cluster]['news'].values[0]
        
        # Mostrar las noticias con mejor separación
        for i, news in enumerate(news_list):
            # Agregar título de cluster y número de noticia
            news_text.insert(tk.END, f"Cluster {cluster} - Noticia {i+1}\n")
            
            # Agregar el contenido de la noticia
            news_text.insert(tk.END, f"{news}\n")
            
            # Línea separadora mejorada (más visual)
            news_text.insert(tk.END, "="*80 + "\n\n")  # Línea más destacada y espaciado extra

    # Frame izquierdo para los números de los clusters
    frame_left = tk.Frame(root, width=200)
    frame_left.pack(side=tk.LEFT, fill=tk.Y, padx=10)

    # Frame derecho para mostrar las noticias
    frame_right = tk.Frame(root)
    frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)

    # Crear los botones para los clusters
    for cluster in clustered_news['cluster']:
        button = tk.Button(frame_left, text=f"Cluster {cluster}", width=15, command=lambda c=cluster: show_news(c))
        button.pack(pady=5)

    # Crear un área de texto con barra de desplazamiento para mostrar las noticias
    news_text = scrolledtext.ScrolledText(frame_right, wrap=tk.WORD, width=60, height=30)
    news_text.pack(expand=True, fill=tk.BOTH)

    # Ejecutar la aplicación
    root.mainloop()

# Para importar este módulo y ejecutar la función, simplemente se hace lo siguiente:
# import nombre_del_modulo
# nombre_del_modulo.show_clustered_news('./noticias_clasificadas_sin_supervision.csv')
