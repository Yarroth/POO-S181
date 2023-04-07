import tkinter as tk
import sqlite3
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.geometry("200x200")
root.title("Main Window")
# Crear nueva ventana
tree_view = tk.Toplevel(root)
tree_view.title("Datos de Autos")

# Crear objeto Treeview
table = ttk.Treeview(tree_view, columns=("marca", "modelo", "ano", "cilindrada", "color", "nuevo_usado", "presupuesto"))

# Definir encabezados
table.heading("#0", text="ID")
table.heading("marca", text="Marca")
table.heading("modelo", text="Modelo")
table.heading("ano", text="Año")
table.heading("cilindrada", text="Cilindrada")
table.heading("color", text="Color")
table.heading("nuevo_usado", text="Nuevo o Usado")
table.heading("presupuesto", text="Presupuesto")

# Estilo de la tabla
table.column("#0", width=50)
table.column("marca", width=100)
table.column("modelo", width=100)
table.column("ano", width=70)
table.column("cilindrada", width=100)
table.column("color", width=70)
table.column("nuevo_usado", width=100)
table.column("presupuesto", width=100)

# Agregar Treeview al layout
table.grid(row=0, column=0)
def mostrar_datos():
    # Conectar a la base de datos
    conn = sqlite3.connect('autos.db')
    c = conn.cursor()

    # Seleccionar todos los registros de la tabla
    c.execute("SELECT rowid, * FROM autos")
    filas = c.fetchall()

    # Borrar datos existentes en la tabla
    for i in table.get_children():
        table.delete(i)

    # Insertar los registros en la tabla
    for fila in filas:
        table.insert(parent="", index="end", iid=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7]))

    # Cerrar la conexión a la base de datos
    conn.close()

# Agregar botón de "Mostrar datos" a la ventana principal
mostrar_button = tk.Button(root, text="Mostrar datos", command=mostrar_datos)
mostrar_button.grid(row=8, column=0, columnspan=2)

def predecir_compra(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        valor = soup.find("td", class_="punit").get_text().strip()
        return float(valor)
    except:
        print("No se pudo obtener el valor de la compra")
        return None

# Create the main window
root = tk.Tk()
root.title("Autos")

# Create the input fields
marca_label = tk.Label(root, text="Marca:")
marca_label.grid(row=0, column=0)
marca_entry = tk.Entry(root)
marca_entry.grid(row=0, column=1)

modelo_label = tk.Label(root, text="Modelo:")
modelo_label.grid(row=1, column=0)
modelo_entry = tk.Entry(root)
modelo_entry.grid(row=1, column=1)

ano_label = tk.Label(root, text="Año:")
ano_label.grid(row=2, column=0)
ano_entry = tk.Entry(root)
ano_entry.grid(row=2, column=1)

cilindrada_label = tk.Label(root, text="Cilindrada:")
cilindrada_label.grid(row=3, column=0)
cilindrada_entry = tk.Entry(root)
cilindrada_entry.grid(row=3, column=1)

color_label = tk.Label(root, text="Color:")
color_label.grid(row=4, column=0)
color_entry = tk.Entry(root)
color_entry.grid(row=4, column=1)

nuevo_usado_label = tk.Label(root, text="Nuevo o usado:")
nuevo_usado_label.grid(row=5, column=0)
nuevo_usado_entry = tk.Entry(root)
nuevo_usado_entry.grid(row=5, column=1)

precio_label = tk.Label(root, text="Presupuesto:")
precio_label.grid(row=6, column=0)
precio_entry = tk.Entry(root)
precio_entry.grid(row=6, column=1)

# Create the function to save the data in the database
def guardar_datos():
    # Connect to the database
    conn = sqlite3.connect('autos.db')
    c = conn.cursor()

    # Create the table if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS autos
                 (marca TEXT, modelo TEXT, ano INT, cilindrada INT, color TEXT, nuevo_usado TEXT, presupuesto INT)''')

    # Convert the input data to the appropriate data types
    try:
        ano = int(ano_entry.get())
    except ValueError:
        ano = None
    try:
        cilindrada = int(cilindrada_entry.get())
    except ValueError:
        cilindrada = None
    nuevo_usado = nuevo_usado_entry.get()
    try:
        precio = int(precio_entry.get())
    except ValueError:
        precio = None

    # Insert the data into the table
    c.execute("INSERT INTO autos VALUES (?, ?, ?, ?, ?, ?, ?)",
              (marca_entry.get(), modelo_entry.get(), ano, cilindrada, color_entry.get(),
               nuevo_usado, precio))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Show a message box confirming that the data has been saved
    messagebox.showinfo("Guardado", "La información del auto ha sido guardada correctamente.")



# Create the button to save the data
guardar_button = tk.Button(root, text="Guardar datos", command=guardar_datos)
guardar_button.grid(row=7, column=0, columnspan=2)

# Create the function to predict the best time to buy a car
def predecir_compra():
    # Obtener los valores de los widgets
    marca = marca_entry.get()
    modelo = modelo_entry.get()
    ano = ano_entry.get()
    cilindrada = cilindrada_entry.get()
    color = color_entry.get()
    nuevo_usado = nuevo_usado_entry.get()
    precio = precio_entry.get()

    print(marca, modelo, ano, cilindrada, color, nuevo_usado, precio)

    # Scrape the "Libro Azul" website to check the value of the car
    url = f"https://www.libroazul.com/resultados.php?brand={marca}&model={modelo}&year={ano}&cc={cilindrada}&type={nuevo_usado}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Check if the car is found in the "Libro Azul" database
    if "No se encontraron resultados" in str(soup):
        messagebox.showwarning("Advertencia", "No se encontraron resultados para el auto deseado en el Libro Azul")
        return

    # Get the value of the car
    valor = soup.find("td", class_="punit").get_text().strip()

    # Connect to the database
    conn = sqlite3.connect('autos.db')
    c = conn.cursor()

    # Query the database to get the average prices by year
    c.execute('''SELECT AVG(precio), ano FROM autos GROUP BY ano ORDER BY ano''')
    resultados = c.fetchall()

    # Calculate the slope of the line that fits the data
    x = [r[1] for r in resultados]
    y = [r[0] for r in resultados]
    n = len(x)
    x_mean = sum(x)/n
    y_mean = sum(y)/n
    numer = sum([xi*yi for xi,yi in zip(x,y)]) - n * x_mean * y_mean
    denum = sum([xi**2 for xi in x]) - n * x_mean**2

    # Calculate the slope
    slope = numer / denum

    # Calculate the best year to buy a car
    best_year = round((y_mean - slope * x_mean) / slope)

    # Check if it's a good time to buy the car
    valor = int(valor.replace("$", "").replace(",", ""))
    if valor < slope * int(ano) + y_mean:
        messagebox.showinfo("Buen momento para comprar el auto", f"El valor del auto deseado es ${valor:,} y es un buen momento para comprarlo")
    else:
        messagebox.showinfo("Malo momento para comprar el auto", f"El valor del auto deseado es ${valor:,} y no es un buen momento para comprarlo")

    # Close the cursor and the connection to the database
    c.close()
    conn.close()
    #Create the button to predict if it's a good time to buy the desired car
predecir_button = tk.Button(root, text="Predecir si es buen momento para comprar el auto deseado", command=predecir_compra)
predecir_button.grid(row=8, column=0, columnspan=2)

#Run the main loop
root.mainloop()