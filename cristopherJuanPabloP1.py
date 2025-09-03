#Juan Pablo Ruiz Trujillo y Cristopher Arboleda
from abc import ABC, abstractmethod

# --- Material base (abstracción y encapsulamiento) ---
class MaterialBiblioteca(ABC):
    def __init__(self, titulo):
        self.__titulo = titulo
        self.__disponible = True

    @abstractmethod
    def dias_devolucion(self):
        pass

    def get_titulo(self):
        return self.__titulo

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

# --- Tipos de material (herencia + polimorfismo) ---
class Libro(MaterialBiblioteca):
    def dias_devolucion(self): return 5

class Revista(MaterialBiblioteca):
    def dias_devolucion(self): return 3

class MaterialAudiovisual(MaterialBiblioteca):
    def dias_devolucion(self): return 2

# --- Usuario ---
class Usuario:
    def __init__(self, nombre, identificacion):
        self.__nombre = nombre
        self.__id = identificacion

    def get_nombre(self): return self.__nombre
    def get_id(self): return self.__id

# --- Biblioteca ---
class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_material(self, material):
        self.catalogo.append(material)

    def mostrar_catalogo(self):
        print("\n--- Catálogo ---")
        for i, mat in enumerate(self.catalogo, 1):
            estado = "Disponible" if mat.esta_disponible() else "Prestado"
            print(f"{i}. {mat.get_titulo()} ({mat.__class__.__name__}) - {estado}")

    def prestar_material(self, usuario, indice):
        if 1 <= indice <= len(self.catalogo):
            mat = self.catalogo[indice-1]
            if mat.prestar():
                print(f"{usuario.get_nombre()} prestó '{mat.get_titulo()}' ({mat.dias_devolucion()} días)")
            else:
                print(f"'{mat.get_titulo()}' ya está prestado.")
        else:
            print("Número inválido.")

    def devolver_material(self, indice):
        if 1 <= indice <= len(self.catalogo):
            mat = self.catalogo[indice-1]
            if not mat.esta_disponible():
                mat.devolver()
                print(f"'{mat.get_titulo()}' devuelto.")
            else:
                print(f"'{mat.get_titulo()}' no estaba prestado.")
        else:
            print("Número inválido.")

# --- Menú de usuario ---
def menu_usuario(biblio, usuario):
    while True:
        biblio.mostrar_catalogo()
        print(f"\nUsuario: {usuario.get_nombre()}")
        print("1. Prestar material  2. Devolver material  3. Salir del usuario")
        op = input("Opción: ")
        if op == "1":
            num = input("Número del material a prestar: ")
            if num.isdigit(): biblio.prestar_material(usuario, int(num))
        elif op == "2":
            num = input("Número del material a devolver: ")
            if num.isdigit(): biblio.devolver_material(int(num))
        elif op == "3": break
        else: print("Opción inválida.")

# --- Sistema principal ---
def main():
    biblio = Biblioteca()
    # Inventario más grande
    materiales = [
        Libro("Cien años de soledad"), Libro("Don Quijote"), Libro("La sombra del viento"),
        Libro("El principito"), Libro("1984"),
        Revista("National Geographic"), Revista("Time"), Revista("Muy Interesante"),
        Revista("Scientific American"), Revista("Forbes"),
        MaterialAudiovisual("Interstellar"), MaterialAudiovisual("Inception"),
        MaterialAudiovisual("The Matrix"), MaterialAudiovisual("Avatar"), MaterialAudiovisual("Toy Story")
    ]
    for m in materiales: biblio.agregar_material(m)

    print("Sistema de Biblioteca\n")
    while True:
        print("1. Nuevo usuario  2. Salir del sistema")
        op = input("Opción: ")
        if op == "1":
            nombre = input("Nombre del usuario: ")
            idu = input("ID del usuario: ")
            menu_usuario(biblio, Usuario(nombre, idu))
        elif op == "2": break
        else: print("Opción inválida.")

if __name__ == "__main__":
    main()

