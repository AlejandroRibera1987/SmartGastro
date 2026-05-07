class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def agregar_stock(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0")
            return

        self.__stock += cantidad
        print(f"Stock actual de {self.__nombre}: {self.__stock}")

    def quitar_stock(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0")
            return False

        if self.__stock == 0:
            print(f"No hay stock disponible de {self.__nombre}")
            return False

        if cantidad > self.__stock:
            print("No hay stock suficiente")
            print(f"Stock disponible: {self.__stock}")
            return False

        self.__stock -= cantidad
        return True

    def mostrar_info(self):
        print(
            f"Producto: {self.__nombre} | "
            f"Precio: ${self.__precio} | "
            f"Stock: {self.__stock}"
        )


class Stock:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.get_nombre()} agregado al inventario")

    def mostrar_stock(self):
        if not self.productos:
            print("El inventario está vacío")
            return

        print("\n----- STOCK ACTUAL -----")
        for i, producto in enumerate(self.productos):
            print(f"{i + 1}. ", end="")
            producto.mostrar_info()
        print("------------------------")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.get_nombre().lower() == nombre.lower():
                return producto
        return None


class Foodtruck:
    def __init__(self, nombre):
        self.nombre = nombre
        self.stock = Stock()
        self.ventas = []

    def agregar_producto(self, nombre, precio, stock):
        producto_existente = self.stock.buscar_producto(nombre)

        if producto_existente:
            producto_existente.agregar_stock(stock)
        else:
            nuevo_producto = Producto(nombre, precio, stock)
            self.stock.agregar_producto(nuevo_producto)

    def registrar_venta(self, nombre_producto, cantidad):
        producto = self.stock.buscar_producto(nombre_producto)

        if producto is None:
            print(f"Producto {nombre_producto} no encontrado")
            return

        venta_exitosa = producto.quitar_stock(cantidad)

        if venta_exitosa:
            total_venta = producto.get_precio() * cantidad
            self.ventas.append({
                "producto": producto.get_nombre(),
                "cantidad": cantidad,
                "total": total_venta
            })

            print("\n------------- VENTA REGISTRADA CORRECTAMENTE -------------")
            print(f"Producto: {producto.get_nombre()}")
            print(f"Cantidad: {cantidad}")
            print(f"Total: ${total_venta}")
            print("----------------------------------------------------------")

    def mostrar_stock(self):
        self.stock.mostrar_stock()


def mostrar_menu():
    print("\n---- SMARTGASTRO ----")
    print("1. Agregar producto")
    print("2. Registrar venta")
    print("3. Mostrar stock")
    print("4. Salir")
    print("---------------------")


def main():
    foodtruck = Foodtruck("SmartGastro")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del producto: ")

                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    stock = int(input("Ingrese el stock del producto: "))

                    if precio <= 0 or stock < 0:
                        print("El precio debe ser mayor a 0 y el stock no puede ser negativo")
                    else:
                        foodtruck.agregar_producto(nombre, precio, stock)

                except ValueError:
                    print("Error: el precio y el stock deben ser números")

            case "2":
                nombre_producto = input("Nombre del producto vendido: ")

                try:
                    cantidad_vendida = int(input("Cantidad vendida: "))

                    if cantidad_vendida <= 0:
                        print("La cantidad debe ser mayor a 0")
                    else:
                        foodtruck.registrar_venta(nombre_producto, cantidad_vendida)

                except ValueError:
                    print("Error: la cantidad debe ser un número entero")

            case "3":
                foodtruck.mostrar_stock()

            case "4":
                print("Gracias por usar SmartGastro")
                break

            case _:
                print("Opción inválida")


if __name__ == "__main__":
    main()