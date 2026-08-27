

class Biblioteca:
    
    def __init__(self):
        
        self.materiales = []
    
    def agregar_material(self, material):
        
        self.materiales.append(material)
        print(f"{material.nombre} ha sido agregado a la biblioteca.")
    
    def mostrar_catalogo(self):
        
        print("\n --- Catálogo --- ")
        
        if len(self.materiales) == 0:
            print("No existe ningun material en el catálogo.")
        else:
            
            for material in self.materiales:
                print(f"\n - {material.nombre} - ")