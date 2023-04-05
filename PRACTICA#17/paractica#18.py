import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import sqlite3
import bcrypt

# Crear la conexión a la base de datos y cursor
conn = sqlite3.connect('CRUD usuarios.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT)")
conn.commit()

def agregar_usuario():
    global id_usuario
    id_usuario = id_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if id_usuario:
        # Encriptar contraseña
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO usuarios (id, email, password) VALUES (?, ?, ?)", (int(id_usuario), email, hashed_password))
        conn.commit()
        actualizar_lista()
        messagebox.showinfo("Éxito", "Usuario agregado con éxito") 

def buscar_usuario():
    id_usuario = id_entry_buscar.get()
    cursor.execute("SELECT * FROM usuarios WHERE id=?", (id_usuario,))
    resultado = cursor.fetchone()
    if resultado is None:
        resultado_label.configure(text="Usuario no encontrado")
    else:
        resultado_label.configure(text=f"ID: {resultado[0]}, Email: {resultado[1]}")
        


def actualizar_usuario():
    id_usuario = id_entry_actualizar.get()
    nuevo_id = new_id_entry_actualizar.get() # Corregido el nombre de la variable
    cursor.execute("UPDATE usuarios SET id=? WHERE id=?", (int(nuevo_id), int(id_usuario))) # Corregido el tipo de datos
    conn.commit()
    actualizar_lista()
    messagebox.showinfo("Éxito", "Usuario actualizado con éxito")


def eliminar_usuario():
    id_usuario = id_entry_eliminar.get()
    confirmacion = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar este usuario?")
    if confirmacion:
        cursor.execute("DELETE FROM usuarios WHERE id=?", (int(id_usuario),)) # Corregido el tipo de datos
        conn.commit()
        actualizar_lista()
        messagebox.showinfo("Éxito", "Usuario eliminado con éxito")

def actualizar_lista():
    global usuarios_treeview
    usuarios_treeview.delete(*usuarios_treeview.get_children())
    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()
    for resultado in resultados:
        id_usuario, email, password = resultado
        hashed_password = '*' * 8  # Mostrar una contraseña oculta en la tabla de la interfaz de usuario
        usuarios_treeview.insert('', 'end', text=id_usuario, values=(email, hashed_password))

root = tk.Tk()
root.title("CRUD de usuarios")

notebook = ttk.Notebook(root)

agregar_frame = ttk.Frame(notebook)
buscar_frame = ttk.Frame(notebook)
actualizar_frame = ttk.Frame(notebook)
eliminar_frame = ttk.Frame(notebook)

notebook.add(agregar_frame, text="Agregar")
notebook.add(buscar_frame, text="Buscar")
notebook.add(actualizar_frame, text="Actualizar")
notebook.add(eliminar_frame, text="Eliminar")

notebook.pack(expand=True, fill="both")
email_label = ttk.Label(agregar_frame, text="Email:")
email_label.pack(side=tk.LEFT, padx=10, pady=10)

email_entry = ttk.Entry(agregar_frame)
email_entry.pack(side=tk.LEFT, padx=10, pady=10)

id_label = ttk.Label(agregar_frame, text="ID:")
id_label.pack(side=tk.LEFT, padx=10, pady=10)

id_entry = ttk.Entry(agregar_frame)
id_entry.pack(side=tk.LEFT, padx=10, pady=10)

password_label = ttk.Label(agregar_frame, text="Contraseña:")
password_label.pack(side=tk.LEFT, padx=10, pady=10)

password_entry = ttk.Entry(agregar_frame, show="*")
password_entry.pack(side=tk.LEFT, padx=10, pady=10)

agregar_button = ttk.Button(agregar_frame, text="Agregar", command=agregar_usuario)
agregar_button.pack(side=tk.LEFT, padx=10, pady=10)

#Buscar usuario
id_label_buscar = ttk.Label(buscar_frame, text="ID:")
id_label_buscar.pack(side=tk.LEFT, padx=10, pady=10)

id_entry_buscar = ttk.Entry(buscar_frame)
id_entry_buscar.pack(side=tk.LEFT, padx=10, pady=10)

buscar_button = ttk.Button(buscar_frame, text="Buscar", command=buscar_usuario)
buscar_button.pack(side=tk.LEFT, padx=10, pady=10)

resultado_label = ttk.Label(buscar_frame)
resultado_label.pack(side=tk.LEFT, padx=10, pady=10)

#Actualizar usuario
#Actualizar usuario
id_label_actualizar = ttk.Label(actualizar_frame, text="Actual ID:")
id_label_actualizar.pack(side=tk.LEFT, padx=10, pady=10)

id_entry_actualizar = ttk.Entry(actualizar_frame)
id_entry_actualizar.pack(side=tk.LEFT, padx=10, pady=10)

new_id_label_actualizar = ttk.Label(actualizar_frame, text="Nuevo ID:")
new_id_label_actualizar.pack(side=tk.LEFT, padx=10, pady=10)

new_id_entry_actualizar = ttk.Entry(actualizar_frame)
new_id_entry_actualizar.pack(side=tk.LEFT, padx=10, pady=10)

actualizar_button = ttk.Button(actualizar_frame, text="Actualizar", command=actualizar_usuario)
actualizar_button.pack(side=tk.LEFT, padx=10, pady=10)


#Eliminar usuario

eliminar_label = ttk.Label(eliminar_frame, text="ID:")
eliminar_label.pack(side=tk.LEFT, padx=10, pady=10)

id_entry_eliminar = ttk.Entry(eliminar_frame)
id_entry_eliminar.pack(side=tk.LEFT, padx=10, pady=10)


eliminar_button = ttk.Button(eliminar_frame, text="Eliminar", command=eliminar_usuario)
eliminar_button.pack(side=tk.LEFT, padx=10, pady=10)


#Tabla de usuarios
usuarios_treeview = ttk.Treeview(root, columns=("Email", "Contraseña"))
usuarios_treeview.heading("#0", text="ID")
usuarios_treeview.heading("Email", text="Email")
usuarios_treeview.heading("Contraseña", text="Contraseña")
usuarios_treeview.pack(expand=True, fill="both")

actualizar_lista()

root.mainloop()

#Cerrar conexión a la base de datos
conn.close()



