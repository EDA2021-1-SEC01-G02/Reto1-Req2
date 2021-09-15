"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.Algorithms.Sorting import quicksort as qu
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():

    catalog = {
        "artworks" : None,
    }
    catalog['artworks'] =  lt.newList(type, None)

    return catalog
# Funciones para agregar informacion al catalogo
def addArtWork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAdquired(artwork1,artwork2):
    date1 = artwork1["DateAcquired"].split("-")
    date2 = artwork2["DateAcquired"].split("-")
    if len(date1)!= 3:
        return True
    if len(date2) != 3:
        return False

    if int(date1[0]) < int(date2[0]):
        return True
    elif int( date1[0]) == int(date2[0]):
        if date1[1] < date2[1]:
            return True
        elif int(date1[1]) == int(date2[1]):
            if int(date1[2]) < int(date2[2]):
                return True  
    else:
        return False



# Funciones de ordenamiento
def sortByDate(lst, sortType):
    
    if sortType == 1:
        ins.sort(lst, cmpArtworkByDateAdquired)
    elif sortType == 2:
        sa.sort(lst,cmpArtworkByDateAdquired)
    elif sortType == 3:
        me.sort(lst,cmpArtworkByDateAdquired)
    elif sortType == 4:
        qu.sort(lst,cmpArtworkByDateAdquired)
    