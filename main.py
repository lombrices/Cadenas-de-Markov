import numpy as np
import tkinter as tk
from tkinter import ttk, scrolledtext

#Funcion para mostrara la matriz de transición en la interfaz, recibe el marco creado en la interfaz
def mostrar_tabla(marco):
    # Datos de la tabla
    columnas = ["Producto Actual", "Big Mac", "McFlurry", "Papas Fritas"]
    datos = [
        ["Big Mac", "0.6", "0.2", "0.2"],
        ["McFlurry", "0.3", "0.5", "0.2"],
        ["Papas Fritas", "0.4", "0.1", "0.5"],
    ]

    tabla = ttk.Treeview(marco, columns=columnas, show="headings", height=3)
    tabla.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=10, pady=10)

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor=tk.CENTER, stretch=True)

    for fila in datos:
        tabla.insert("", tk.END, values=fila)

#Funcion que crea una interfaz para mostrat el problema y la probaboñodad estacionaria obtenida
def lanzarInterfaz(ruta_readme,matriz):
    
    with open(ruta_readme, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    partes = contenido.split("| Producto Actual")
    antes_tabla = partes[0].strip()
   
    despues_tabla=partes[1].split("0.5          |\n\n")[1]
    despues_tabla+="\nLa probabilidad estacionaria es: \n"+"Big Mac: "+str(matriz[0])+"\nMcFlurry: "+str(matriz[1])+"\nPapas Fritas: "+str(matriz[2])

    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Problema Cadena de Markov")
    ventana.geometry("800x600")

    # Crear un frame para el texto antes de la tabla
    frame_texto_antes = tk.Frame(ventana)
    frame_texto_antes.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=10, pady=5)

    texto_antes = scrolledtext.ScrolledText(frame_texto_antes, wrap=tk.WORD, height=7, font=("Arial", 12))
    texto_antes.pack(expand=True, fill=tk.BOTH)
    texto_antes.insert(tk.INSERT, antes_tabla)
    texto_antes.configure(state='disabled')  # Desactivar edición

    # Crear un frame para la tabla
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(side=tk.TOP, expand=False, fill=tk.BOTH, padx=10, pady=5)
    mostrar_tabla(frame_tabla)

    # Crear un frame para el texto después de la tabla
    frame_texto_despues = tk.Frame(ventana)
    frame_texto_despues.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, padx=10, pady=5)

    texto_despues = scrolledtext.ScrolledText(frame_texto_despues, wrap=tk.WORD, height=10, font=("Arial", 12))
    texto_despues.pack(expand=True, fill=tk.BOTH)
    texto_despues.insert(tk.INSERT, despues_tabla)
    texto_despues.configure(state='disabled')  # Desactivar edición

    # Ejecutar la ventana
    ventana.mainloop()




# Matriz de transicion
p = np.array([
    [0.6, 0.2, 0.2], 
    [0.3, 0.4, 0.3],  
    [0.2, 0.3, 0.5]   
], dtype=float)

for i in range(0,3):
    s=p[i,0]+p[i,1]+p[i,2]
    if(s!=1.0):
        print("Las filas de la matriz de transicion deben sumar 1")
        exit(0)


#transponemos la matriz
p_traspuesta = p.T
p_traspuesta -= np.eye(p.shape[0])

#Construimos el sistema de ecuaciones
A = np.vstack([p_traspuesta, np.ones(p.shape[0])])
b = np.zeros(p.shape[0] + 1) 
b[-1] = 1  #Condicion de que la suma de los pi sea igual a 1

# Resolver el sistema de ecuaciones
pi = np.linalg.lstsq(A, b, rcond=None)[0]

print("La probabilidad estacionaria es:", pi)
lanzarInterfaz("readme.md",pi)