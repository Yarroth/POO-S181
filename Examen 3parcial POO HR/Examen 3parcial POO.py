import tkinter as tk
import sqlite3

class BancoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("BancoApp")
        
        # Crea una conexión a la base de datos
        self.conn = sqlite3.connect("BD_Banco.db")
        self.c = self.conn.cursor()
        
        # Crea la tabla si no existe
        self.c.execute('''CREATE TABLE IF NOT EXISTS TBCuentas
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         NoCuenta INTEGER,
                         Saldo INTEGER)''')
        
        # Crea los widgets de la interfaz
        self.label1 = tk.Label(master, text="No. de cuenta:")
        self.label1.grid(row=0, column=0)
        self.entry1 = tk.Entry(master)
        self.entry1.grid(row=0, column=1)
        self.label2 = tk.Label(master, text="Saldo:")
        self.label2.grid(row=1, column=0)
        self.entry2 = tk.Entry(master)
        self.entry2.grid(row=1, column=1)
        self.button1 = tk.Button(master, text="Agregar cuenta", command=self.agregar_cuenta)
        self.button1.grid(row=2, column=0, columnspan=2)
        self.button2 = tk.Button(master, text="Mostrar cuentas", command=self.mostrar_cuentas)
        self.button2.grid(row=3, column=0, columnspan=2)
        self.label3 = tk.Label(master, text="Actualizar saldo:")
        self.label3.grid(row=4, column=0)
        self.button3 = tk.Button(master, text="Actualizar saldo", command=self.actualizar_saldo)
        self.button3.grid(row=5, column=0, columnspan=2)

    def agregar_cuenta(self):
        # Obtiene los datos del usuario
        no_cuenta = int(self.entry1.get())
        saldo = int(self.entry2.get())
        
        # Inserta los datos en la base de datos
        self.c.execute("INSERT INTO TBCuentas (NoCuenta, Saldo) VALUES (?, ?)", (no_cuenta, saldo))
        self.conn.commit()
        
        # Limpia los campos de entrada
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
    
    def actualizar_saldo(self):
        # Obtiene los datos del usuario
        no_cuenta = int(self.entry1.get())
        saldo = int(self.entry2.get())

        # Actualiza el saldo en la base de datos
        self.c.execute("UPDATE TBCuentas SET Saldo = ? WHERE NoCuenta = ?", (saldo, no_cuenta))
        self.conn.commit()

        # Limpia los campos de entrada
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
   
    
    def mostrar_cuentas(self):
        # Obtiene todas las cuentas de la base de datos
        self.c.execute("SELECT * FROM TBCuentas")
        cuentas = self.c.fetchall()
        
        # Muestra las cuentas en la consola
        for cuenta in cuentas:
            print(cuenta)
         
root = tk.Tk()
app = BancoApp(root)
root.mainloop()
