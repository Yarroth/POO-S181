# atributos del villano 
especie = "Villano"
nombre = "Desgraciado"
altura = 2.10

# métodos Villano
def correr(self, status):
    if status:
        print("El villano " + self.nombre + " está corriendo")
    else:
        print("El villano " + self.nombre + " se detuvo")

def lanzarGranada(self):
    print("El villano " + self.nombre + " lanzó una granada")
    
def disparar(self):
    print("El villano " + self.nombre + " está disparando")

def recargar(self):
    print("El villano " + self.nombre + " está recargando")


#4. Acceder a atributos y memtodos de cada objeto 
print("")
print( "El personaje pertenece a la raza." + Heroe.get)     