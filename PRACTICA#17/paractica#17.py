import tkinter as tk
from tkinter import ttk
import sqlite3
import bcrypt
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()
# Crear cursor
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT)")

conn.commit()
def agregar_usuario():
    global id_usuario
    id_usuario = id_entry.get()
    password = password_entry.get().encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
    c.execute("INSERT INTO usuarios (id, password) VALUES (?, ?)", (int(id_usuario), hashed_password))
    conn.commit()
    actualizar_lista()

def buscar_usuario():
    id_usuario = id_entry.get()
    c.execute("SELECT * FROM usuarios WHERE id=?", (id_usuario,))
    resultado = c.fetchone()
    if resultado is None:
        resultado_label.configure(text="Usuario no encontrado")
    else:
        resultado_label.configure(text="Usuario encontrado")

def actualizar_usuario():
    id_usuario = id_entry.get()
    password = password_entry.get().encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')
    c.execute("UPDATE usuarios SET password=? WHERE id=?", (hashed_password, id_usuario))
    conn.commit()
    actualizar_lista()

def eliminar_usuario():
    id_usuario = id_entry.get()
    c.execute("DELETE FROM usuarios WHERE id=?", (id_usuario,))
    conn.commit()
    actualizar_lista()
def actualizar_lista():
    usuarios_treeview.delete(*usuarios_treeview.get_children())
    c.execute("SELECT * FROM usuarios")
    resultados = c.fetchall()
    for resultado in resultados:
        usuarios_treeview.insert('', 'end', text=resultado[0], values=(resultado[1]))

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

buscar_label = ttk.Label(buscar_frame, text="ID:")
buscar_label.pack(side=tk.LEFT, padx=10, pady=10)

id_entry = ttk.Entry(buscar_frame)
id_entry.pack(side=tk.LEFT, padx=10, pady=10)

buscar_button = ttk.Button(buscar_frame, text="Buscar", command=buscar_usuario)
buscar_button.pack(side=tk.LEFT, padx=10, pady=10)

resultado_label = ttk.Label(buscar_frame, text="")
resultado_label.pack(side=tk.LEFT, padx=10, pady=10)

id_label = ttk.Label(actualizar_frame, text="ID:")
id_label.pack(side=tk.LEFT, padx=10, pady=10)

id_entry = ttk.Entry(actualizar_frame)
id_entry.pack(side=tk.LEFT, padx=10, pady=10)

password_label = ttk.Label(actualizar_frame, text="Nueva contraseña:")
password_label.pack(side=tk.LEFT, padx=10, pady=10)

password_entry = ttk.Entry(actualizar_frame, show="*")
password_entry.pack(side=tk.LEFT, padx=10, pady=10)

actualizar_button = ttk.Button(actualizar_frame, text="Actualizar", command=actualizar_usuario)
actualizar_button.pack(side=tk.LEFT, padx=10, pady=10)

id_label = ttk.Label(eliminar_frame, text="ID:")
id_label.pack(side=tk.LEFT, padx=10, pady=10)

id_entry = ttk.Entry(eliminar_frame)
id_entry.pack(side=tk.LEFT, padx=10, pady=10)

eliminar_button = ttk.Button(eliminar_frame, text="Eliminar", command=eliminar_usuario)
eliminar_button.pack(side=tk.LEFT, padx=10, pady=10)

usuarios_treeview = ttk.Treeview(root, columns=("password"))
usuarios_treeview.heading("#0", text="ID")
usuarios_treeview.heading("password", text="Contraseña")
usuarios_treeview.pack(expand=True, fill="both")

actualizar_lista()

root.mainloop()