# Este archivo define la clase 'Inventario', que contiene toda la lógica
# para gestionar la colección de productos, como añadir, eliminar y buscar.

from producto import Producto

# Esta clase presenta la lógica para la gestión del inventario.
class Inventario:
    
    # El constructor inicializa el inventario y carga los datos desde el archivo.
    def __init__(self):
        self.nombre_archivo = "inventario.txt"
        self.productos = []
        self._cargar_inventario()

    # Carga los productos desde el archivo de texto, manejando posibles errores.
    def _cargar_inventario(self):
        try:
            with open(self.nombre_archivo, 'r') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) == 4:
                        id_prod, nombre, cantidad, precio = partes
                        producto = Producto(id_prod, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
            print("Inventario cargado exitosamente desde inventario.txt.")
        except FileNotFoundError:
            print("Archivo 'inventario.txt' no encontrado. Se creará uno nuevo al guardar.")
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    # Guarda la lista de productos actual en el archivo de texto.
    def _guardar_inventario(self):
        try:
            with open(self.nombre_archivo, 'w') as f:
                for producto in self.productos:
                    linea = (f"{producto.get_producto_id()},{producto.get_nombre()},"
                             f"{producto.get_cantidad()},{producto.get_precio()}\n")
                    f.write(linea)
            return True
        except Exception as e:
            print(f"Error al guardar el inventario en el archivo: {e}")
            return False

    # Busca un producto por su ID de forma interna.
    def __buscar_producto_por_id(self, producto_id):
        for p in self.productos:
            if p.get_producto_id() == producto_id:
                return p
        return None

    # Añade un producto nuevo y guarda los cambios en el archivo.
    def anadir_producto(self, producto):
        if self.__buscar_producto_por_id(producto.get_producto_id()):
            print(f"Error: El producto con ID '{producto.get_producto_id()}' ya existe.")
        else:
            self.productos.append(producto)
            if self._guardar_inventario():
                print(f"Producto '{producto.get_nombre()}' añadido y guardado correctamente.")
            else:
                print(f"AVISO: Producto '{producto.get_nombre()}' añadido, pero no se pudo guardar en el archivo.")

    # Elimina un producto por su ID y guarda los cambios en el archivo.
    def eliminar_producto(self, producto_id):
        producto_a_eliminar = self.__buscar_producto_por_id(producto_id)
        if producto_a_eliminar:
            self.productos.remove(producto_a_eliminar)
            if self._guardar_inventario():
                print(f"Producto con ID '{producto_id}' eliminado y cambios guardados.")
            else:
                print(f"AVISO: Producto con ID '{producto_id}' eliminado, pero no se pudieron guardar los cambios.")
        else:
            print(f"Error: No se encontró un producto con ID '{producto_id}'.")

    # Actualiza los datos de un producto y guarda los cambios en el archivo.
    def actualizar_producto(self, producto_id, nueva_cantidad=None, nuevo_precio=None):
        producto_a_actualizar = self.__buscar_producto_por_id(producto_id)
        if producto_a_actualizar:
            if nueva_cantidad is not None:
                producto_a_actualizar.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto_a_actualizar.set_precio(nuevo_precio)
            if self._guardar_inventario():
                print(f"Producto con ID '{producto_id}' actualizado y cambios guardados.")
            else:
                print(f"AVISO: Producto con ID '{producto_id}' actualizado, pero no se pudieron guardar los cambios.")
        else:
            print(f"Error: No se ha encontrado un producto con ID '{producto_id}'.")

    # Busca productos en el inventario cuyo nombre coincida con un término.
    def buscar_producto_por_nombre(self, nombre_buscado):
        resultados = []
        for p in self.productos:
            if nombre_buscado.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    # Imprime en la consola todos los productos del inventario.
    def mostrar_inventario(self):
        print("\n--- INVENTARIO ACTUAL ---")
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
        print("-------------------------")