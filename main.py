from menu.menu import Menu
from menu.menu_no_lineal import menu_arbol

def main():
    opc = 0
    while opc != 3:
        print("\nMenús")
        print("1.- Menú lineales\n2.- Menú de árbol")
        opc = input("Elige un menú: ")
        match opc:
            case "1":
                menu = Menu()
                menu.ejecutar()
            case "2":
                menu = menu_arbol()
                menu.menu()
            
if __name__ == "__main__":
    main()