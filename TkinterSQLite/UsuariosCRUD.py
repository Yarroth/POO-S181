import tkinter as tk
import sqlite3
from tkinter import messagebox

class UserRegistrationForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Registro de usuario")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Nombre:").grid(row=0)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Correo electrónico:").grid(row=1)
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Contraseña:").grid(row=2)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=2, column=1)

        tk.Button(self.master, text="Guardar", command=self.save_user).grid(row=3, column=1)

    def save_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (name text, email text PRIMARY KEY, password text)''')

        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))

        conn.commit()
        conn.close()

        messagebox.showinfo("Éxito", "Usuario guardado con éxito")


if __name__ == "__main__":
    root = tk.Tk()
    app = UserRegistrationForm(master=root)
    app.mainloop()