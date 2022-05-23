import csv
from claseFacultad import Facultad
class Manejador:

    def __init__(self):
        self.__lista=[]


    def inicializar(self):
        archivo=open("Facultades.csv")
        reader=csv.reader(archivo,delimiter=";")
        aux=0
        ant=-1
        for fila in reader:
            aux=fila[0]
            if aux!=ant:
                unaFacultad=Facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(unaFacultad)
                ant=aux
            else:
                if aux==ant:
                    self.__lista[int(aux)-1].agregarCarrera(fila)
        archivo.close()


    def __str__(self):
        s=""
        for facultad in self.__lista:
            s=str(facultad) + "\n"

        return s

    def mostrar(self):
        for facultad in self.__lista:
            facultad.mostrar()


    def item1(self,codigo):
        i=0
        cod=self.__lista[i].getCodig()
        while(i<len(self.__lista)and(cod!=codigo)):
            i+=1
            cod=self.__lista[i].getCodig()
        if i<len(self.__lista):
            print("se encontro la facultad")
            unafacultad=self.__lista[i]
            print("nombre {} ".format(unafacultad.getNombre()))
            unafacultad.mostrardatoscarrera()

    def nombreCarrera(self,nombre):
        print("item 2")
        i=0
        bandera=True
        while (i<len(self.__lista))and(bandera):
            bandera=self.__lista[i].buscarCarrera(nombre)
            i+=1
        if bandera==True:
            print("No se encontro la carrera")






