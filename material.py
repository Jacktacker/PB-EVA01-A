class Material:

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def descripcion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Precio: ${self.__precio}")