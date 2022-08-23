#Ejercicio 1
def posicionesMultiplo(lista,n):
    respuesta = lista[::n]
    return respuesta

#Ejercicio 2
def nuevaLista(lista):
    nuevoResultado = 0
    nuevaLista = []
    for i in lista:
        nuevoResultado += i
        nuevaLista.append(nuevoResultado)
    return nuevaLista

#Ejercicio 3
def elimina(lista):
    lista.pop(0)
    lista.pop(-1)
    return lista

#Ejercicio 4
def ordenada(lista):
    respuesta = True
    for i,index in enumerate(lista[:-1]):
        if index > lista[i+1]:
            respuesta = False

    return respuesta

#Ejercicio 5
def duplicado(lista):
	respuesta = False
	index = 0
	longitud = len(lista)
	while (index < longitud) and (not(respuesta)):
		elemento = lista[index]
		if lista.count(elemento) > 1:
			respuesta = True
		index = index + 1
	return respuesta

#Ejercicio 6
def eliminaDuplicados(lista):
	for elemento in lista[:]:
		if lista.count(elemento) > 1:
			ayuda = 0
			while lista.count(elemento) > ayuda:
				lista.remove(elemento)
				ayuda += 1
	return lista

#Ejercicio 7
def elementosDistintos(lista):
    index = 0
    nuevaLista = [];
    for elemento in lista[:]:
        if duplicado(lista):
            nuevaLista = eliminaDuplicados(lista)
    longitud = len(nuevaLista)
    return longitud

#Ejercicio 8
def busquedaDicotomica(lista,palabra):
    steps = 0
    izq = 0
    der = len(lista)-1
    respuesta = "Elemento no encontrado"
    while izq <= der:
        steps += 1
        puntoMedio = (izq+der) // 2

        if lista[puntoMedio] == palabra:
            return "Elemento encontrado en la lista"
        if lista[puntoMedio] > palabra:
            der = puntoMedio - 1
        if lista[puntoMedio] < palabra:
            izq = puntoMedio + 1
    return respuesta

#Ejercicio 9
#1
def raicesLista(n):
	return n**0.5

def raices(lista):
	nuevaLista = map(raicesLista,lista)
	nuevaLista2 = list(nuevaLista)
	print(nuevaLista2)

#2
def distanciaAlOrigen(punto):
	x,y = punto
	return ((pow(x,2))+(pow(y,2)))**0.5

def distancias(lista):
	nuevaLista = map(distanciaAlOrigen,lista)
	nuevaLista2 = list(nuevaLista)
	return nuevaLista2

#3
def numCuadrado(n):
	return pow(n,2)

def cuadrados(lista):
	nuevaLista = map(numCuadrado,lista)
	nuevaLista2 = list(nuevaLista)
	return nuevaLista2

#4
def longitudCadena(strings):
	return len(strings)

def longitudes(lista):
	nuevaLista = map(longitudCadena,lista)
	nuevaLista2 = list(nuevaLista)
	return nuevaLista2

#5
def convertirTemp(n):
	return (n-32)*5/9

def convertirFC(lista):
	nuevaLista = map(convertirTemp,lista)
	nuevaLista2 = list(nuevaLista)
	return nuevaLista2

#FINAL
MAX = 3

def distanciasss(punto):
	posnx,posny = punto
	return (pow(posnx,2)+pow(posny,2))**0.5

def menoresAMax(lista):
	nuevaLista = map(distanciasss,lista)
	nuevaLista2 = list(nuevaLista)

	for valor in nuevaLista2[:]:
		if valor < MAX:
			nuevaLista2.remove(valor)
	return nuevaLista2

#Ejercicio 10
#1
def esPar(l):
	respuesta = False
	if l%2 == 0:
		respuesta = True
	else:
		respuesta
	return respuesta

def pares(lista):
	nuevaLista = filter(esPar,lista)
	nuevaLista2 = list(nuevaLista)
	return nuevaLista2

#2
def esCorta(strings):
	respuesta = False
	if len(strings) < 5:
		respuesta = True
	else:
		respuesta

	return respuesta

def cortas(lista):
	nuevaLista = filter(esCorta,lista)
	nuevaLista2 = list(nuevaLista)
	return nuevaLista2

#3
def distancia1(punto):
	posnx,posny = punto
	return (pow(posnx,2)+pow(posny,2))**0.5

def cerca(lista,MAX):
	nuevaLista = list(map(distancia1,lista))
	nuevaLista2 = list(filter(lambda x: x < MAX, nuevaLista))
	return nuevaLista2

#4
def esPositivo(n):
	respuesta = False
	if n > 0:
		respuesta = True
	else:
		respuesta
	return respuesta

def positivos(lista):
	nuevaLista = filter(esPositivo,lista)
	nuevaLista2 = list(nuevaLista)
	return nuevaLista2

#Ejercicio 11
from functools import reduce

#1
def esBooleano(x,y):
	respuesta = False
	if (x == True) and (y == True):
		respuesta = True
	elif (x == False) and (y == True):
		respuesta = True
	elif (x == False) and (y == False):
		respuesta = True
	else:
		respuesta
	return respuesta

def todosVerdaderos(lista):
	nuevaLista = reduce(esBooleano,lista)
	return nuevaLista

#2
def unoverdadero(lista):
    respuesta = False
    for valor in lista[:]:
        if valor == True:
            respuesta = True
        else:
            respuesta

    return respuesta


#3
def cantelementos(lista):
    contador = 0
    for index in lista:
        contador += 1

    return contador


#4
def promedio(lista):
	nuevaLista = reduce(lambda x,y:x+y,lista)/len(lista)
	return nuevaLista

#5
def productoLista(lista):
	longitud = len(lista)
	respuesta = []
	if longitud > 1:
		respuesta = reduce(lambda x,y: x*y,lista)
	else:
		respuesta = 1

	return respuesta

#6
def pegarStrings(lista):
	nuevaLista = reduce(lambda x,y: str(x)+str(y), lista)
	return nuevaLista


print(pegarStrings(["Hola","Mama"]))
