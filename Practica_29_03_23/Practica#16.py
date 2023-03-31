import tkinter 
from tkinter import messagebox
import sqlite3
import bcrypt

#Creación de la base de datos
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

#Creación de la tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
					nombre text,
					id text,
					contraseña text
					)""")

#Función para encriptar contraseñas
def encriptar(contraseña):
	return bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())

#Función para agregar usuarios
def agregar_usuario():
	#Creación de la ventana
	ventana_agregar = tkinter.Toplevel()
	ventana_agregar.title("Agregar Usuario")
	
	#Creación de los campos
	etiqueta_nombre = tkinter.Label(ventana_agregar, text="Nombre:")
	entrada_nombre = tkinter.Entry(ventana_agregar)
	
	etiqueta_id = tkinter.Label(ventana_agregar, text="ID:")
	entrada_id = tkinter.Entry(ventana_agregar)
	
	etiqueta_contraseña = tkinter.Label(ventana_agregar, text="Contraseña:")
	entrada_contraseña = tkinter.Entry(ventana_agregar, show="*")
	
	#Función para guardar los datos
	def guardar_datos():
		nombre = entrada_nombre.get()
		id = entrada_id.get()
		contraseña = encriptar(entrada_contraseña.get())
		
		#Insertar datos en la base de datos
		cursor.execute("INSERT INTO usuarios VALUES (:nombre, :id, :contraseña)", {'nombre': nombre, 'id': id, 'contraseña': contraseña})
		conn.commit()
		
		messagebox.showinfo("Guardado", "Usuario guardado satisfactoriamente")
		
		#Cerrar la ventana
		ventana_agregar.destroy()
	
	#Creación de los botones
	boton_guardar = tkinter.Button(ventana_agregar, text="Guardar", command=guardar_datos)
	boton_cancelar = tkinter.Button(ventana_agregar, text="Cancelar", command=ventana_agregar.destroy)
	
	#Acomodar los elementos en la pantalla
	etiqueta_nombre.grid(row=0, column=0, padx=10, pady=10)
	entrada_nombre.grid(row=0, column=1, padx=10, pady=10)
	
	etiqueta_id.grid(row=1, column=0, padx=10, pady=10)
	entrada_id.grid(row=1, column=1, padx=10, pady=10)
	
	etiqueta_contraseña.grid(row=2, column=0, padx=10, pady=10)
	entrada_contraseña.grid(row=2, column=1, padx=10, pady=10)
	
	boton_guardar.grid(row=3, column=0, padx=10, pady=10)
	boton_cancelar.grid(row=3, column=1, padx=10, pady=10)
	
#Función para buscar usuarios
def buscar_usuario():
	#Creación de la ventana
	ventana_buscar = tkinter.Toplevel()
	ventana_buscar.title("Buscar Usuario")
	
	#Creación de los campos
	etiqueta_id = tkinter.Label(ventana_buscar, text="ID:")
	entrada_id = tkinter.Entry(ventana_buscar)
	
	#Función para buscar los datos
	def buscar_datos():
		id = entrada_id.get()
		
		#Buscar datos en la base de datos
		cursor.execute("SELECT * FROM usuarios WHERE id=:id", {'id': id})
		usuario = cursor.fetchone()
		
		if usuario:
			messagebox.showinfo("Usuario encontrado", f"Nombre: {usuario[0]}\nID: {usuario[1]}")
		else:
			messagebox.showerror("Error", "Usuario no encontrado")
			
		#Cerrar la ventana
		ventana_buscar.destroy()
	
	#Creación de los botones
	boton_buscar = tkinter.Button(ventana_buscar, text="Buscar", command=buscar_datos)
	boton_cancelar = tkinter.Button(ventana_buscar, text="Cancelar", command=ventana_buscar.destroy)
	
	#Acomodar los elementos en la pantalla
	etiqueta_id.grid(row=0, column=0, padx=10, pady=10)
	entrada_id.grid(row=0, column=1, padx=10, pady=10)
	
	boton_buscar.grid(row=1, column=0, padx=10, pady=10)
	boton_cancelar.grid(row=1, column=1, padx=10, pady=10)
	
#Función para consultar usuarios
def consultar_usuarios():
	#Creación de la ventana
	ventana_consultar = tkinter.Toplevel()
	ventana_consultar.title("Consultar Usuarios")
	
	#Función para consultar los datos
	def consultar_datos():
		#Consultar datos en la base de datos
		cursor.execute("SELECT * FROM usuarios")
		usuarios = cursor.fetchall()
		
		mensaje = ""
		
		for usuario in usuarios:
			mensaje += f"Nombre: {usuario[0]}\nID: {usuario[1]}\n\n"
		
		messagebox.showinfo("Usuarios", mensaje)
		
		#Cerrar la ventana
		ventana_consultar.destroy()
	
	#Creación de los botones
	boton_consultar = tkinter.Button(ventana_consultar, text="Consultar", command=consultar_datos)
	boton_cancelar = tkinter.Button(ventana_consultar, text="Cancelar", command=ventana_consultar.destroy)
	
	#Acomodar los elementos en la pantalla
	boton_consultar.grid(row=0, column=0, padx=10, pady=10)
	boton_cancelar.grid(row=0, column=1, padx=10, pady=10)
	
#Función para actualizar usuarios
def actualizar_usuario():
	#Creación de la ventana
	ventana_actualizar = tkinter.Toplevel()
	ventana_actualizar.title("Actualizar Usuario")
	
	#Creación de los campos
	etiqueta_id = tkinter.Label(ventana_actualizar, text="ID:")
	entrada_id = tkinter.Entry(ventana_actualizar)
	
	etiqueta_nombre = tkinter.Label(ventana_actualizar, text="Nombre:")
	entrada_nombre = tkinter.Entry(ventana_actualizar)
	
	etiqueta_contraseña = tkinter.Label(ventana_actualizar, text="Contraseña:")
	entrada_contraseña = tkinter.Entry(ventana_actualizar, show="*")
	
	#Función para actualizar los datos
	def actualizar_datos():
		id = entrada_id.get()
		nombre = entrada_nombre.get()
		contraseña = encriptar(entrada_contraseña.get())
		
		#Actualizar datos en la base de datos
		cursor.execute("UPDATE usuarios SET nombre=:nombre, contraseña=:contraseña WHERE id=:id", {'nombre': nombre, 'contraseña': contraseña, 'id': id})
		conn.commit()
		
		messagebox.showinfo("Actualizado", "Usuario actualizado satisfactoriamente")
		
		#Cerrar la ventana
		ventana_actualizar.destroy()
	
	#Creación de los botones
	boton_actualizar = tkinter.Button(ventana_actualizar, text="Actualizar", command=actualizar_datos)
	boton_cancelar = tkinter.Button(ventana_actualizar, text="Cancelar", command=ventana_actualizar.destroy)
	
	#Acomodar los elementos en la pantalla
	etiqueta_id.grid(row=0, column=0, padx=10, pady=10)
	entrada_id.grid(row=0, column=1, padx=10, pady=10)
	
	etiqueta_nombre.grid(row=1, column=0, padx=10, pady=10)
	entrada_nombre.grid(row=1, column=1, padx=10, pady=10)
	
	etiqueta_contraseña.grid(row=2, column=0, padx=10, pady=10)
	entrada_contraseña.grid(row=2, column=1, padx=10, pady=10)
	
	boton_actualizar.grid(row=3, column=0, padx=10, pady=10)
	boton_cancelar.grid(row=3, column=1, padx=10, pady=10)

#Creación de la ventana principal
ventana_principal = tkinter.Tk()
ventana_principal.title("Gestión de Usuarios")

#Creación de los botones
boton_agregar = tkinter.Button(ventana_principal, text="Agregar usuario", command=agregar_usuario)
boton_buscar = tkinter.Button(ventana_principal, text="Buscar usuario", command=buscar_usuario)
boton_consultar = tkinter.Button(ventana_principal, text="Consultar usuarios", command=consultar_usuarios)
boton_actualizar = tkinter.Button(ventana_principal, text="Actualizar usuario", command=actualizar_usuario)

#Acomodar los elementos en la pantalla
boton_agregar.grid(row=0, column=0, padx=10, pady=10)
boton_buscar.grid(row=0, column=1, padx=10, pady=10)
boton_consultar.grid(row=1, column=0, padx=10, pady=10)
boton_actualizar.grid(row=1, column=1, padx=10, pady=10)

#Iniciar el programa
ventana_principal.mainloop()