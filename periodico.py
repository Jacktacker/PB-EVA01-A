from material import Material

class Periodico(Material):
    def __init__(self, titulo, autor, precio, es_nuevo, fecha_publicacion):
        super().__init__(titulo, autor, precio, es_nuevo)
        self.fecha_publicacion = fecha_publicacion
    
    # AQUI HAY POLIFORMISMO
    def descripcion(self):
        print("\n --- Periodico ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.precio}")
        print(f"Es nuevo: {self.es_nuevo}")
        print(f"La fecha de publicación es: {self.fecha_publicacion}")