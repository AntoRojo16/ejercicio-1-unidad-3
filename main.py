from manejadorFacultad import Manejador
from ClaseMenu import Menu
if __name__ == '__main__':
    unalista=Manejador()
    unalista.inicializar()
    bandera = False
    while not bandera:
        print("\nMENU DE OPCIONES")
        print("0 Salir")
        print("1 ITEM 1.1: Item 1")
        print("2 ITEM 1.2: Item 2")

        opcion = int(input('Ingrese una opcion:'))
        unmenu=Menu()
        unmenu.opcion(opcion,unalista)
        bandera = int(opcion)== 0


