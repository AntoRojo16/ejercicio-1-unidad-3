from manejadorFacultad import Manejador
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            0:self.salir
                          }
    def opcion(self,op,lista):
        print(op)
        func=self.__switcher.get(op,lambda: print("Opción no válida"))
        func(lista)

    def salir(self,lista):
        print('Usted salio del programa')
    def opcion1(self,lista):
        j=input("Ingrese el codig de la facultad")
        lista.item1(j)


    def opcion2(self,lista):
        nom=input("Ingrese el nombre de la carrera")
        lista.nombreCarrera(nom)
