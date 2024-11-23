import tkinter as tk
import os

def listar_archivos(carpeta, listbox):
    # Limpiar el Listbox antes de agregar nuevos archivos
    listbox.delete(0, tk.END)
    
    # Listar los archivos CSV en la carpeta especificada
    archivos_csv = [f for f in os.listdir(carpeta) if f.endswith('.csv')]
    
    # Agregar los archivos al Listbox
    for archivo in archivos_csv:
        listbox.insert(tk.END, archivo)

def mostrar_archivo_seleccionado(carpeta):
    archivo_ruta = None  # Inicializar la variable fuera del if

    def seleccionar():
        nonlocal archivo_ruta  # Usar la variable definida en el ámbito exterior
        # Obtener el archivo seleccionado en el Listbox
        seleccion = listbox.curselection()
        if seleccion:
            archivo_seleccionado = listbox.get(seleccion[0])
            archivo_ruta = os.path.join(carpeta, archivo_seleccionado)
            etiqueta.config(text=f"Archivo seleccionado: {archivo_ruta}")
            print(f"Archivo seleccionado: {archivo_ruta}")
            
            # Cerrar la ventana después de la selección
            root.destroy()  # Usar destroy para cerrar la ventana

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Seleccionar archivos CSV")

    # Etiqueta para mostrar el nombre del archivo seleccionado
    etiqueta = tk.Label(root, text="Selecciona un archivo CSV", width=50, anchor='w')
    etiqueta.pack(pady=10)

    # Listbox para mostrar los archivos CSV
    listbox = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
    listbox.pack(pady=10)

    # Llamar a la función para listar los archivos CSV desde la carpeta
    listar_archivos(carpeta, listbox)

    # Botón "Seleccionar" para mostrar el archivo seleccionado
    boton_seleccionar = tk.Button(root, text="Seleccionar", command=seleccionar)
    boton_seleccionar.pack(pady=10)

    # Iniciar la interfaz gráfica
    root.mainloop()

    return archivo_ruta
