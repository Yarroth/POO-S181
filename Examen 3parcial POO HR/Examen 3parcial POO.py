import tkinter as tk
import sqlite3

conn = sqlite3.connect('BD_Banco.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master
        master.title("BD Banco")

        c.execute('''CREATE TABLE IF NOT EXISTS TBCuentas
                     (NoCuenta INTEGER,
                      Saldo INTEGER)''')
        conn.commit()

        self.label_ncuenta = tk.Label(master, text="No. Cuenta")
        self.label_ncuenta.grid(row=0, column=0)

        self.entry_ncuenta = tk.Entry(master)
        self.entry_ncuenta.grid(row=0, column=1)

        self.label_saldo = tk.Label(master, text="Saldo")
        self.label_saldo.grid(row=1, column=0)

        self.entry_saldo = tk.Entry(master)
        self.entry_saldo.grid(row=1, column=1)

        self.button_insertar = tk.Button(master, text="Insertar", command=self.insertar)
        self.button_insertar.grid(row=2, column=0)

        self.label_idcuenta = tk.Label(master, text="Registro")
        self.label_idcuenta.grid(row=3, column=0)

        self.entry_idcuenta = tk.Entry(master)
        self.entry_idcuenta.grid(row=3, column=1)

        self.button_consultar = tk.Button(master, text="Consultar", command=self.consultar)
        self.button_consultar.grid(row=4, column=0)

    def insertar(self):
        ncuenta = self.entry_ncuenta.get()
        saldo = self.entry_saldo.get()

        c.execute("INSERT INTO TBCuentas (NoCuenta, Saldo) VALUES (?, ?)", (ncuenta, saldo))
        conn.commit()

    def consultar(self):
        registro = self.entry_idcuenta.get()
        c.execute("SELECT * FROM TBCuentas LIMIT 1 OFFSET ?", (registro-1,))
        row = c.fetchone()
        if row:
            print(row)
        else:
            print("No se encontró ningún registro con ese número")

root = tk.Tk()
app = App(root)
root.mainloop()
