import tkinter as tk
from password import PasswordGenerator

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Generador de contraseñas')
        self.password_label = tk.Label(self.root, text='Contraseña:')
        self.password_label.grid(row=0, column=0)
        self.password_entry = tk.Entry(self.root, width=30)
        self.password_entry.grid(row=0, column=1)
        self.length_label = tk.Label(self.root, text='Longitud:')
        self.length_label.grid(row=1, column=0)
        self.length_entry = tk.Entry(self.root, width=10)
        self.length_entry.insert(0, '8')
        self.length_entry.grid(row=1, column=1)
        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbutton = tk.Checkbutton(self.root, text='Incluir mayúsculas', variable=self.uppercase_var)
        self.uppercase_checkbutton.grid(row=2, column=0)
        self.special_var = tk.BooleanVar()
        self.special_checkbutton = tk.Checkbutton(self.root, text='Incluir caracteres especiales', variable=self.special_var)
        self.special_checkbutton.grid(row=3, column=0)
        self.generate_button = tk.Button(self.root, text='Generar contraseña', command=self.generate_password)
        self.generate_button.grid(row=4, column=0)
        self.root.mainloop()

    def generate_password(self):
        password_length = int(self.length_entry.get())
        include_uppercase = self.uppercase_var.get()
        include_special = self.special_var.get()
        password_generator = PasswordGenerator(password_length, include_uppercase, include_special)
        password_string = password_generator.generate_password()
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password_string)

if __name__ == '__main__':
    gui = GUI()
