# Este programa es el punto de entrada de la aplicación. Crea una interfaz
# de menú en la consola para que el usuario interactúe con el inventario.

# Se importan las clases necesarias desde los otros archivos del proyecto.
from producto import Producto
from inventario import Inventario

# Esta es la función principal que ejecuta el menú de la aplicación.
def main():
    # Esta línea crea el objeto principal que gestionará el inventario.
    mi_inventario = Inventario()
    
    # Este bucle mantiene el menú de opciones activo hasta que se elija salir.
    while True:
        print("\n--- GESTIÓN DE INVENTARIO ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todo el inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        # En caso de que el usuario elija la opción '1', se ejecuta este bloque.
        if opcion == '1':
            try:
                id_prod = input("Introduce el identificador del producto: ")
                nombre = input("Introduce el nombre del producto: ")
                cantidad = int(input("Introduce la cantidad: "))
                precio = float(input("Introduce el precio: "))
                nuevo_producto = Producto(id_prod, nombre, cantidad, precio)
                mi_inventario.anadir_producto(nuevo_producto)
            except ValueError:
                print("Error: La cantidad y el precio deben ser valores numéricos.")
        
        # En caso de que el usuario elija la opción '2', se ejecuta este bloque.
        elif opcion == '2':
            id_prod = input("Introduce el identificador del producto a eliminar: ")
            mi_inventario.eliminar_producto(id_prod)

        # Si la opción es '3', se solicita la información para actualizar.
        elif opcion == '3':
            id_prod = input("Introduce el identificador del producto a actualizar: ")
            try:
                cant_str = input("Introduce la nueva cantidad (dejar en blanco para no cambiar): ")
                precio_str = input("Introduce el nuevo precio (dejar en blanco para no cambiar): ")
                
                nueva_cantidad = int(cant_str) if cant_str else None
                nuevo_precio = float(precio_str) if precio_str else None

                if nueva_cantidad is not None or nuevo_precio is not None:
                    mi_inventario.actualizar_producto(id_prod, nueva_cantidad, nuevo_precio)
                else:
                    print("No se introdujo ningún cambio.")
            except ValueError:
                print("Error: La cantidad y el precio deben ser valores numéricos.")

        # Si la opción es '4', se realiza una búsqueda por nombre.
        elif opcion == '4':
            nombre_buscado = input("Introduce el nombre a buscar: ")
            resultados = mi_inventario.buscar_producto_por_nombre(nombre_buscado)
            if not resultados:
                print("No se encontraron productos con ese nombre.")
            else:
                print("\n--- Resultados de la Búsqueda ---")
                for producto in resultados:
                    print(producto)
                print("---------------------------------")

        # Si la opción es '5', se muestra el inventario completo.
        elif opcion == '5':
            mi_inventario.mostrar_inventario()

        # Si la opción es '6', se termina la ejecución del programa.
        elif opcion == '6':
            print("Saliendo del programa.")
            # Esta instrucción finaliza el bucle para terminar el programa.
            break
        
        # Este bloque gestiona las entradas que no son válidas.
        else:
            print("Error: Opción no válida. Intente de nuevo.")

# Este bloque se asegura de que la función main() solo se ejecute
# cuando este archivo es el punto de entrada principal.
if __name__ == "__main__":
    main()