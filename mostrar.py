import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
from tkinter import font

def show_news(csv_file):
    # Cargar el archivo CSV
    df = pd.read_csv(csv_file)

    # Validar y limpiar datos
    df['news_clean'] = df['news_clean'].fillna("").astype(str)
    df['news'] = df['news'].fillna("").astype(str)
    df['cluster_name'] = df['cluster_name'].fillna("Cluster-desconocido")

    # Verificar si existe la columna "titular"
    has_title = 'titular' in df.columns

    # Agrupar las noticias por su número de cluster
    clustered_news = df.groupby('cluster')['news'].apply(list).reset_index()
    if 'cluster_name' not in df.columns:
        raise ValueError("El archivo CSV no contiene la columna 'cluster_name'.")
    cluster_names = dict(zip(df['cluster'], df['cluster_name']))

    frequent_words = df.groupby('cluster')['news_clean'].apply(
        lambda news: " ".join(news).split()
    ).apply(
        lambda words: ", ".join(pd.Series(words).value_counts().head(5).index) if words else "Sin palabras frecuentes"
    )

    # Crear la ventana principal de Tkinter
    root = tk.Tk()
    root.title("Noticias por Cluster")
    root.geometry("1000x700")

    # Crear el área de texto con barra de desplazamiento
    news_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=30)
    news_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Configurar la etiqueta de texto en negrita
    news_text.tag_configure("bold", font=("Helvetica", 10, "bold"))

    # Crear la fuente en negrita para los titulares
    bold_font = font.Font(weight="bold")

    # Función que se llama cuando se hace clic en un cluster
    def show_news_cluster(cluster):
        # Limpiar el área de texto
        news_text.delete(1.0, tk.END)

        # Obtener las noticias del cluster seleccionado
        news_list = clustered_news[clustered_news['cluster'] == cluster]['news'].values[0]

        # Mostrar las palabras más frecuentes del cluster
        news_text.insert(tk.END, f"Palabras frecuentes del cluster '{cluster_names[cluster]}':\n")
        news_text.insert(tk.END, f"{frequent_words[cluster]}\n")
        news_text.insert(tk.END, "-"*80 + "\n\n")

        # Mostrar las noticias
        for i, news in enumerate(news_list):
            # Si existe la columna "titular", agregarla antes de la noticia
            if has_title:
                title = df.loc[df['news'] == news, 'titular'].values[0]
                news_text.insert(tk.END, f"{title}\n","bold")
                news_text.insert(tk.END, f"\n{news}\n")
            else:
              news_text.insert(tk.END, f"Noticia {i+1}:\n{news}\n")
                
            news_text.insert(tk.END, "="*80 + "\n\n")
    
    # Frame izquierdo para los números de los clusters
    frame_left = tk.Frame(root, width=200, bg="#f4f4f4")
    frame_left.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

    # Crear los botones para los clusters en una cuadrícula
    row = 0
    col = 0
    for cluster in clustered_news['cluster']:
        cluster_name = cluster_names[cluster]
        button = tk.Button(
            frame_left, text=cluster_name, width=20, height=2, 
            command=lambda c=cluster: show_news_cluster(c), fg="black",
            font=("Helvetica", 10, "bold"), relief="solid", bd=2
        )
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        col += 1
        if col == 3:  # Cambia a la siguiente fila después de 3 columnas
            col = 0
            row += 1

    # Hacer que las columnas y filas se ajusten automáticamente
    for i in range(row + 1):
        frame_left.grid_rowconfigure(i, weight=1)
    for i in range(3):
        frame_left.grid_columnconfigure(i, weight=1)

    # Ejecutar la aplicación
    root.mainloop()

