productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

import time

def stock_marca(marca):
    marca=marca.lower()
    total_stock=0
    for c in productos:
        if productos[c][0].lower()==marca:
            total_stock += stock[c][1]
    print(f"Stock total disponible para {marca} : {total_stock}")
    time.sleep(1)

def búsqueda_precio(p_min,p_max):
    modelos_rango=[]
    for c in stock:
        precio,cantidad=stock[c]
        if p_min <= precio <= p_max and cantidad >0:
            marca=productos[c][0]
            modelos_rango.append(f"{marca}--{c}")
    if modelos_rango:
        modelos_rango.sort()
        print("Modelos disponibles en el rango de precios :")
        for c in modelos_rango:
            print(c)
            time.sleep(1)
    else:
        print("No hay modelos en ese rango de precios ")

def actualizar_precio(modelo,p):
    if modelo in productos:
        stock[modelo][0]= p
        return True
    else:
        return False

def menu():
    while True:
        print("***MENU PRINCIPAL***")
        print("1. Stock Marca\n2. busqueda por precio\n3. Actualizar precio\n4. Salir")

        opcion=input("Ingrese su opcion : \n")

        if opcion=="1":
            marca=input("Ingrese Marca a Consultar :\n")
            stock_marca(marca)
        elif opcion=="2":
            try:
                p_min=int(input("Ingrese el precio minimo :\n"))
                p_max=int(input("Ingrese el precio maximo :\n")) 
                búsqueda_precio(p_min,p_max)
            except ValueError:
                print("!!!DEBE INGRESAR VALORES ENTEROS¡¡¡") 
        elif opcion=="3":
            while True:
                modelo=input("Ingrese Modelo a actualizar :\n")
                try:
                    p=int(input("Ingrese precio nuevo :\n"))
                    if actualizar_precio(modelo,p):
                        print("!Precio Actualizado¡")
                        time.sleep(1)
                    else:
                        print("!Modelo no encontrado¡")
                except ValueError:
                    print("!!DEBE INGRESAR UN PRECIO VALIDO(ENTERO¡¡)")

                continuar=input("Desea Actualizar otro precio (s/n): \n").lower()
                if continuar != "s":
                    break
        elif opcion=="4":
            print("PROGRAMA FINALIZADO...")
            break
        else:
            print("!!Ingrese una opcion valida¡¡")
menu()                