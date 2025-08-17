# Este archivo define la clase 'Producto', que sirve como plantilla
# para crear los objetos que se gestionarán en el inventario.

# Se define la clase que representa un producto.
class Producto:
    
    # Este es el método constructor, se ejecuta al crear un nuevo producto.
    def __init__(self, producto_id, nombre, cantidad, precio):
        # Esta variable almacena el identificador único del producto.
        self.__producto_id = producto_id
        # Esta variable almacena el nombre descriptivo del producto.
        self.__nombre = nombre
        # Esta variable almacena la cantidad de unidades en existencia.
        self.__cantidad = cantidad
        # Esta variable almacena el precio unitario del producto.
        self.__precio = precio

    # --- Métodos Getters (para obtener los valores de los atributos) ---

    # Esta función devuelve el ID del producto.
    def get_producto_id(self):
        return self.__producto_id

    # Esta función devuelve el nombre del producto.
    def get_nombre(self):
        return self.__nombre

    # Esta función devuelve la cantidad en stock del producto.
    def get_cantidad(self):
        return self.__cantidad

    # Esta función devuelve el precio del producto.
    def get_precio(self):
        return self.__precio

    # --- Métodos Setters (para modificar los valores de los atributos) ---

    # Esta función actualiza el nombre del producto.
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Esta función actualiza la cantidad del producto.
    def set_cantidad(self, nueva_cantidad):
        # Este bloque valida que la cantidad no sea un número negativo.
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    # Esta función actualiza el precio del producto.
    def set_precio(self, nuevo_precio):
        # Este bloque valida que el precio no sea un número negativo.
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo.")

    # Este método define cómo se muestra el objeto en formato de texto.
    def __str__(self):
        return (f"ID: {self.__producto_id}, "
                f"Nombre: {self.__nombre}, "
                f"Cantidad: {self.__cantidad}, "
                f"Precio: {self.__precio:.2f}")