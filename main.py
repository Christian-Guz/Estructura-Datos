from menu.menu import Menu
from menu.menu_no_lineal import menu_arbol
from estructuras.no_lineales.Arbol_expresiones import NodeExpression

def main():
    opc = 0
    while True:
        print("\nMenús")
        print("1.- Menú lineales\n2.- Menú no lineales\n3.- Salir")
        opc = input("Elige un menú: ")
        if opc == "1":
            menu = Menu()
            menu.ejecutar()
        elif opc == "2":
            menu = menu_arbol()
            menu.menu()
        elif opc == "3":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida. Intente nuevamente")
        
if __name__ == "__main__":
    main()