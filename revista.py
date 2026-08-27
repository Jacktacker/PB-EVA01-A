from material import Material

class Revista(Material):
    def __init__(self, titulo, autor, precio, es_nuevo, edicion):
        super().__init__(titulo, autor, precio, es_nuevo)
        self.edicion = edicion
    
    # AQUI HAY POLIFORMISMO
    def descripcion(self):
        print("\n --- Revista ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.precio}")
        print(f"Es nuevo: {self.es_nuevo}")
        print(f"La edición es: {self.edicion}")