
class Personaje:
    
    # Constructor de la clase Personaje
    def __init__(self, especie, nombre, altura):
        self.__especie = especie
        self.__nombre = nombre
        self.__altura = altura
    
    # Métodos getter para los atributos encapsulados
    def getEspecie(self):
        return self.__especie
    
    def getNombre(self):
        return self.__nombre
    
    def getAltura(self):
        return self.__altura
    
    # Métodos Personaje
    def correr(self, status):
        if status:
            print("El personaje " + self.__nombre + " está corriendo")
        else:
            print("El personaje " + self.__nombre + " se detuvo")
    
    def lanzar_granada(self):
        print("Se lanzó una granada")
    
    def recargar_arma(self, municiones):
        cargador = 5
        cargador += municiones
        print("El arma tiene ahora " + str(cargador) + " balas")

class Villano:
    
    # Constructor de la clase Villano
    def __init__(self, especie, nombre, altura):
        self.__especie = especie
        self.__nombre = nombre
        self.__altura = altura
    
    # Métodos getter para los atributos encapsulados
    def getEspecie(self):
        return self.__especie
    
    def getNombre(self):
        return self.__nombre
    
    def getAltura(self):
        return self.__altura
    
    # Métodos Villano
    def correr(self, status):
        if status:
            print("El villano " + self.__nombre + " está corriendo")
        else:
            print("El villano " + self.__nombre + " se detuvo")
    
    def lanzar_granada(self):
        print("El villano " + self.__nombre + " lanzó una granada")
    
    def disparar(self):
        print("El villano " + self.__nombre + " está disparando")
    
    def recargar(self):
        print("El villano " + self.__nombre + " está recargando")


# Instanciar un objeto
heroe = Personaje("Humano", "Marcus Fenix", 1.90)

# Acceder a sus atributos
print("Atributos Personaje")
print("El personaje pertenece a la raza: " + heroe.getEspecie())
print("Se llama: " + heroe.getNombre())
print("Mide: " + str(heroe.getAltura()) + " metros")
print("")

# Métodos Personaje
heroe.correr(True)
heroe.lanzar_granada()
heroe.recargar_arma(68)

# Acceder a atributos y métodos del objeto
print("Atributos y Métodos del Héroe")
print("El personaje pertenece a la raza: " + heroe.getEspecie())
print("Se llama: " + heroe.getNombre())
print("Mide: " + str(heroe.getAltura()) + " Metros")
print("")

# Métodos Personaje
heroe.correr(True)
heroe.lanzar_granada()
heroe.recargar_arma(68)