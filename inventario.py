# Este archivo define la clase 'Inventario', que contiene toda la lógica
# para gestionar la colección de productos, como añadir, eliminar y buscar.

# Se importa la clase 'Producto' para poder crear objetos de ese tipo.
from producto import Producto

# Esta clase presenta la lógica para la gestión del inventario.
class Inventario:
    
    # El constructor inicializa el inventario con una lista vacía para los productos.
    def __init__(self):
        self.productos = []

    def __buscar_producto_por_id(self, producto_id):
        # Este bucle recorre todos los productos para encontrar una coincidencia.
        for p in self.productos:
            if p.get_producto_id() == producto_id:
                return p
        return None

    # Esta función añade un nuevo producto a la lista de inventario.
    def anadir_producto(self, producto):
        # Se comprueba que el ID del nuevo producto no exista previamente.
        if self.__buscar_producto_por_id(producto.get_producto_id()):
            print(f"Error: El producto con ID '{producto.get_producto_id()}' ya existe.")
        else:
            # Si el ID es único, se añade el producto a la lista.
            self.productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' añadido correctamente.")

    # Esta función elimina un producto de la lista usando su ID.
    def eliminar_producto(self, producto_id):
        producto_a_eliminar = self.__buscar_producto_por_id(producto_id)
        # Si el producto existe, se elimina de la lista.
        if producto_a_eliminar:
            self.productos.remove(producto_a_eliminar)
            print(f"Producto con ID '{producto_id}' eliminado correctamente.")
        else:
            print(f"Error: No se encontró un producto con ID '{producto_id}'.")

    # Esta función actualiza la cantidad o el precio de un producto.
    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        producto_a_actualizar = self.__buscar_producto_por_id(producto_id)
        if producto_a_actualizar:
            if nueva_cantidad is not None:
                producto_a_actualizar.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto_a_actualizar.set_precio(nuevo_precio)
            print(f"El producto con ID '{producto_id}' actualizado correctamente.")
        else:
            print(f"Error: No se ha encontrado un producto con ID '{producto_id}'.")

    # Esta función busca productos cuyo nombre contenga el texto buscado.
    def buscar_producto_por_nombre(self, nombre_buscado):
        # Se crea una lista para almacenar los productos que coincidan.
        resultados = []
        for p in self.productos:
            # La búsqueda no distingue entre mayúsculas y minúsculas.
            if nombre_buscado.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_inventario(self):
        print("\n--- INVENTARIO ACTUAL ---")
        # Se verifica si el inventario está vacío antes de intentar mostrarlo.
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
        print("-------------------------")