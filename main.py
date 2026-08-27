# Byron Manqueñir Vera
from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from periodico import Periodico
from material import Material


def main():
    
    # SE CREA LA BIBLIOTECA
    catalogo = Biblioteca
    
    # SE INSTANCIAN LOS LIBROS
    libro1 = Libro("Cazafortunas", "Jairo muñoz", 25000, True, 250)
    
    libro2 = Libro("Genialidad", "Leandro Parrao", 50000, True, 300)
    
    # SE INSTANCIA LA REVISTA
    revista1 = Revista("¿Solo dos ruedas?", "Fernando Del Villar", 35000, False, 30)
    
    # SE INSTANCIA EL PERIODICO
    periodico1 = Periodico("¿Que sucede con la programación hoy?", "Byron Manqueñir", 2000, True, "26/08/2026")
    
    
    # SE MUESTRAN LAS DESCRIPCIONES
    libro1.descripcion()
    libro2.descripcion()
    
    revista1.descripcion()
    
    periodico1.descripcion()
    
    # SE MODIFICA EL PRECIO DEL PERIODICO
    
    periodico1.set_precio(input("\n - Introduzca el precio: "))
    
    # SE AGREGAN LOS MATERIALES A LA BIBLIOTECA
    catalogo.agregar_material(libro1)
    catalogo.agregar_material(libro2)
    catalogo.agregar_material(revista1)
    catalogo.agregar_material(periodico1)
    
    # SE MUESTRA EL CATALOGO COMPLETO
    catalogo.mostrar_catalogo()
    
    
    
    
    
    
    


if __name__ == "__main__":
    main()