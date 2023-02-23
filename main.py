from utils.constants import *
from utils.read_write_db import *
from utils.messages import *
from utils.operations import string_serializer

def main(): # Menú principal de la aplicación
    run = RUN
    option = ZERO

    while run:  # Se ejecuta hasta que ingrese una opción válida
        print(TOP_MENU) # Header
        show_menu() # Body
        print(BOTTOM_MENU) # Footer

        option = input("Elija opción: ")

        if option.isnumeric():
            if str(option) == LOGOUT:
                run = STOP
            elif int(option) in range(int(ADD), int(LOGOUT)):
                break
        else:
            print_warning("Ingrese una opción válida.")
    manage(option)

def is_exit(input): # Verifica si se escribio la palabra clave SALIR que finaliza el programa desde cualquier menú o input
    if(str(input) == EXIT):
        print("¡Lo esperamos pronto, que tenga un buen día!")
        exit()

def show_menu(): # Muestra la lista de productos, precios y stock
    products = getProducts()
    prices = getPrices()
    stocks = getStock()
    if products:
        print(f"\tNúmero \tNombre  \tPrecio \t\tStock")
        for product in products:
            print(f"\t{(product)} \t{string_serializer(products[product], TEN)} \t{string_serializer(prices[product], TEN)} \t{stocks[product]}")
    else:
        print_notify("Sin existencias.")

def manage(option): # Manejo de opciones con respecto al input del usuario
    match option:
        case '1': add_menu()
        case '2': delete_menu()
        case '3': update_menu()
        case '4': 
            print("¡Lo esperamos pronto, que tenga un buen día!")
            exit()
        case default: print("Elección no encontrada")

products = getProducts() # extracción de los productos
prices = getPrices() # extracción de los precios
stocks = getStock() # extracción de los stocks

def add_menu(): # función para agregar un producto
    while RUN:  
        name = input("Ingrese el nombre del producto: ")
        is_exit(name)

        if name:
            break
        print_warning("Ingrese un nombre correcto.")

    while RUN:
        price = input("Ingrese el costo del producto: ")
        is_exit(price)

        if price.isnumeric():
           break
        print_warning("Debe ingresar un costo correcta.") 
    
    while RUN:
        stock = input("Ingrese el stock del producto: ")
        is_exit(stock)

        if stock.isnumeric():
            break
        print_warning("Debe ingresar una cantidad correcta.") 

    save = input("Guardar [s] Sí, [n] No: ")
    is_exit(save)

    new_number = ONE if len(products) == ZERO else int(list(products)[-1])+ONE  #Obtiene el número del último producto y suma una unidad para el nuevo producto

    if save in ACCEPT:
        new_number = str(new_number)
        products[new_number] = name
        setProducts(products)

        prices[new_number] = float(price)
        setPrices(prices)

        stocks[new_number] = int(stock)
        setStock(stocks)

        print_success("Se guardo correctamente.")
    else:
        print_warning("No se guardó.")

    optional_menu(ADD_OPTION)
    

def delete_menu(): # función para eliminar un producto
    number = input("Ingrese el Número del producto que desea eliminar (Ingrese 0 si desea regresar al menú principal): ")
    is_exit(number)

    if number == NO_OPTION:
        main()
    
    if number in products:
        save = input(f"¿Está seguro de eliminar el Producto número {number}? [s] Sí, [n] No: ")
        is_exit(save)

        number = str(number)
        if save in ACCEPT:
            del(products[number])
            setProducts(products)

            del(prices[number])
            setPrices(prices)

            del(stocks[number])
            setStock(stocks)
        else:
            print_warning("No se eliminó.")
    else:
        print_warning("Producto no encontrado.")
        delete_menu()

    optional_menu(DELETE_OPTION)
    

def update_menu(): # función para actualizar un producto
    number = input("Ingrese el Número del producto que desea actualizar: ")
    is_exit(number)

    if number in products:
        number = str(number)
        while RUN:  
            name = input(f"Ingrese un nuevo nombre del producto (Nombre actual = {products[number]}): ")
            is_exit(name)

            if name:
                break
            print_warning("Ingrese un nombre correcto.")
        
        while RUN:
            price = input(f"Ingrese un nuevo costo del producto (Costo actual = {prices[number]}): ")
            is_exit(price)

            if price.isnumeric():
                break
            print_warning("Debe ingresar un costo correcta.") 
        
        while RUN:
            stock = input(f"Ingrese el stock del producto (Stock actual = {stocks[number]}): ")
            is_exit(stock)

            if stock.isnumeric():
                break
            print_warning("Debe ingresar una cantidad correcta.") 

        save = input("Guardar [s] Sí, [n] No: ")
        is_exit(save)

        if save in ACCEPT:
            products[number] = name
            setProducts(products)

            prices[number] = float(price)
            setPrices(prices)

            stocks[number] = int(stock)
            setStock(stocks)

            print_success("Se guardo correctamente.")
        else:
            print_warning("No se guardó.")
    else:
        print_warning("Producto no encontrado.")

    optional_menu(UPDATE_OPTION)

def optional_menu(text): # menú opcional, solo muestra el menú escogido(Agregar, Eliminar o Actualizar) y la opción de volver al menú principal
    print(TOP_MENU)
    show_menu()
    print(LINE, ENTER)

    print(f"[1] {text}, [2] Volver al menú principal")

    option = input("Elija opción: ")
    is_exit(option)

    if option == GENERAL_OPTION:
        if text == ADD_OPTION:
            add_menu()
        elif text == DELETE_OPTION:
            delete_menu()
        elif text == UPDATE_OPTION:
            update_menu()

    elif option != MAIN_MENU_OPTION:
        print_warning("Opción no válida.")
        print_warning("Volviendo al menú principal...")

    main()
main()

