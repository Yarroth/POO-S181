from tkinter import Tk, Frame, Button, Entry, Label
from funciones_logicas import login

ventana = Tk()
ventana.title("Práctica 12: login con tkinter y P.O.O")
ventana.geometry("600x400")

label = Label(ventana, text="correo:")
label.pack()
from tkinter import Tk, Frame, Button, Entry, Label, messagebox

ventana = Tk()
ventana.title("Práctica 12: login con tkinter y P.O.O")
ventana.geometry("600x400")

label = Label(ventana, text="Correo:")
label.pack()
texto_email = Entry(ventana)
texto_email.pack()

label = Label(ventana, text="Contraseña:")
label.pack()
texto_password = Entry(ventana, show="*")
texto_password.pack()

def boton_login_click():
    from funciones_logicas import login
    resultado, exitoso = login(texto_email.get(), texto_password.get())
    if exitoso:
        messagebox.showinfo("Inicio de sesión exitoso", resultado)
    else:
        messagebox.showerror("Error de inicio de sesión", resultado)

boton_login = Button(ventana, text="Iniciar sesión", bg="#66ff99", command=boton_login_click)
boton_login.pack()

ventana.mainloop()
