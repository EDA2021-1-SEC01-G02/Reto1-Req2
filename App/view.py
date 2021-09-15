"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Elegir el tipo de ordenamiento.")
    print('3- Ejecutar el ordenamiento sobre una muestra dada.')

catalog = None
muestra = 0
lstMuestra = None
sortType = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        print('Elija el tipo de lista: ')

        print('1. SINGLE_LINKED')
        print('2. ARRAY_LIST')

        type = int(input())
        if type == 2:
            type = 'ARRAY_LIST'
        elif type == 1:
            type = 'SINGLE LINKED'

        catalog = controller.initCatalog(type)
        controller.loadData(catalog)
        a = catalog['artworks']
        
        size = lt.size(catalog['artworks'])
        cent = True
        while cent == True:
            muestra = int(input('Ingrese el tamaño de la muestra: '))
            if muestra <= size:
                cent =  False
        
        lstMuestra = lt.subList(catalog['artworks'],1, muestra)
 
    elif int(inputs[0]) == 2:
        print("Elija que tipo de ordenamiento desea: ")
        print("1- InsertionSort")
        print("2- Shell")
        print("3- Merge ")
        print("4- Quick")
        sortType = int(input(''))

        

    elif int(inputs[0]) == 3:

        controller.sortByDate(lstMuestra,sortType)
        for i in range(1, lt.size(lstMuestra)+1):
            print ('\n', lt.getElement(lstMuestra,i))
    else:
        sys.exit(0)
sys.exit(0)
