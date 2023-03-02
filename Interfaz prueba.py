import tkinter as tk
from tkinter import messagebox

# Función para mostrar el mensaje de confirmación
def confirmacion(seccion):
    respuesta = messagebox.askyesno("Confirmación", f"¿Seguro que desea continuar en la sección {seccion}?")
    if respuesta:
        print(f"Continuando en la sección {seccion}")
    else:
        print("Cancelado")

# Función para agregar nuevos botones a la sección verde
def agregar_botones_verdes():
    # Crear tres nuevos botones y agregarlos a la sección verde
    boton4 = tk.Button(seccion2, text="Botón 4", bg="light green", command=lambda: confirmacion("4"))
    boton4.pack(pady=10, padx=40, fill="x")

    boton5 = tk.Button(seccion2, text="Botón 5", bg="lime green", command=lambda: confirmacion("5"))
    boton5.pack(pady=10, padx=40, fill="x")

    boton6 = tk.Button(seccion2, text="Botón 6", bg="green yellow", command=lambda: confirmacion("6"))
    boton6.pack(pady=10, padx=40, fill="x")

# Crear la ventana
ventana = tk.Tk()
ventana.geometry("300x200")

# Crear las tres secciones con diferentes colores
seccion1 = tk.Frame(ventana, bg="red", width=100, height=200)
seccion1.pack(side="top", fill="both", expand=True)

seccion2 = tk.Frame(ventana, bg="green", width=100, height=200)
seccion2.pack(side="top", fill="both", expand=True)

seccion3 = tk.Frame(ventana, bg="blue", width=100, height=200)
seccion3.pack(side="top", fill="both", expand=True)

# Agregar un botón en cada sección para mostrar el mensaje de confirmación
boton1 = tk.Button(seccion1, text="Rojo", bg="pink", command=lambda: confirmacion("1"))
boton1.pack(pady=10, padx=40, fill="x")

boton2 = tk.Button(seccion2, text="Verde", bg="yellow", command=agregar_botones_verdes)
boton2.pack(pady=10, padx=40, fill="x")

boton3 = tk.Button(seccion3, text="Azul", bg="orange", command=lambda: confirmacion("3"))
boton3.pack(pady=10, padx=40, fill="x")

# Mostrar la ventana
ventana.mainloop()
