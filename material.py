class Material:

    def __init__(self, titulo, autor, precio, es_nuevo):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.es_nuevo = es_nuevo

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        
        self.precio = precio
        
        if precio == 0:
            precio = 1
            print("El precio no puede ser 0")
        else:
            print("El precio ha sido cambiado correctamente.")

    def descripcion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.precio}")
        print(f"Es nuevo: {self.es_nuevo}")