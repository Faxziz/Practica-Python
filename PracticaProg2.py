import time
import os

#PRACTICA 1
#Ejercicio de Ejemplo
def imprimir_cuadrados():
    n1 = int(input("Ingrese un numero entero por favor: ? "))
    n2 = int(input("Ingrese otro numero entero: ? "))
    suma = 0
    for x in range(n1,n2):
        suma = suma + x*x

    print("La suma de los cuadrados entre ", n1,"y ",n2,"es: ",suma)
    print("Eso es todo por ahora")

#Ejercicio 3
def preguntaR():
    nombre = input("Cual es tu nombre? ?")

    print("Hola, ",nombre)

    n1 = int(input("Ingrese un numero por favor: ?"))
    n2 = int(input("Ingrese otro numero: ? "))
    mult = 0
    mult = n1*n2

    print("La multiplicacion entre ",n1,"y ",n2," es: ",mult)

#Ejercicio 4
def ejercicio4AB():
    base = int(input("Ingrese el numero de una base de un rectangulo: ?"))
    altura = int(input("Ingrese su altura: ?"))
    perimetro = (base*2)+(altura*2)
    area = base*altura
    print("El perimetro del rectangulo es: ",perimetro,"y su area: ",area)

def ejercicio4C(x1,x2,y1,y2):
    ''' x1,x2,y1,y2 representan coordenadas '''
    base = x2-x1
    altura = y2-y1
    perimetro = (base*2)+(altura*2)
    area = base*altura
    print("El perimetro del rectangulo es: ",perimetro,"y el area: ",area)

def ejercicio4EFG(radio):
    pi = 3.141592

    areaCirculo = 2*pi*radio
    volumenEsfera = (4/3)*pi*(radio*radio*radio)
    print("El area del circulo es: ",areaCirculo,"y el volumen de la esfera: ",volumenEsfera)
    
def raiz_cuadrada(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n**0.5

def triangulo():
    cateto1 = int(input("Ingrese el numero del cateto 1: ?"))
    cateto2 = int(input("Ingrese el numero del cateto 2: ?"))

    calculo = raiz_cuadrada((cateto1**2)+(cateto2**2))
    print("La hipotenusa del triangulo es igual a: ",calculo)

#Ejercicio 6
def factorial():
    num = int(input("Ingrese un numero a calcular: ? "))
    suma = 1 
    for i in range(1,num+1):
        suma *= i
    print(suma)

#Ejercicio 7
def ejercicio7A():
    n1 = int(input("Ingrese un numero por favor: ? "))
    n2 = int(input("Ingrese un numero por favor: ? "))

    suma = n1+n2
    resta= n1-n2
    mult = n1*n2
    division = n1/n2

    print("La suma es: ",suma,"la resta ",resta,"la multiplicacion ",mult,"y la division ",division)

def tabla():
    num = int(input("Ingrese el numero a imprimir su tabla: ?"))
    mult = 1
    for i in range(0,11):
        mult = num*i
        print(i," | ",mult)

#Ejercicio 8-9
def ejercicio89():
    word = input("Ingrese una palabra a imprimir: ?")
    sepp = input("Ingrese el separador de la palabra: ")
    num = int(input("Ingrese el numero que va a repetir la palabra: ?"))
    
    print(word*num,sep=sepp)

# --------------------------------PRACTICA 2--------------
#Ejercicio 6
#A
def parono(n):
    if (n%2==0):
        print("Es par")
    else:
        print("No es impar")
#B
def multipli(n):
    if n%3==0:
        print("Es multiplo de 3")
    else: 
        print("No es multiplo")
#C
def esmultiplo(n,f):
    if f%n==0:
        print(n," es multiplo de ",f)
    else:
        print("No es multiplo")

#Ejercicio 7
def absoluto():
    n = float(input("Ingrese un numero: ? "))
    calc = 0

    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    elif n>1:
        print(n) 
    else:
        calc = n-n-n 
        print(calc)

#Ejercicio 9
#A 
def bisiesto():
    year = int(input("Ingrese un año: ?"))

    if ((year%4==0 and year%100 != 0) or year%400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")

#B 
def daysOM():
    month = int(input("Ingrese un numero de mes 1-12: ?"))

    if (month == 1 and 3 and 5 and 7 and 8 and 10 and 12):
        print("El mes tiene 31 dias")
    elif (month == 4 and 6 and 9 and 11):
        print("El mes tiene 30 dias")
    else:
        print("El mes tiene 28 dias")

#C 
def meses(mes):

    if (mes == 1):
        return "Enero"
    elif (mes == 2):
        return "Febrero"
    elif (mes == 3):
        return "Marzo"
    elif (mes == 4):
        return "Abril"
    elif (mes == 5):
        return "Mayo"
    elif (mes == 6):
        return "Junio"
    elif (mes == 7):
        return "Julio"
    elif (mes == 8):
        return "Agosto"
    elif (mes == 9):
        return "Septiembre"
    elif (mes == 10):
        return "Octubre"
    elif (mes == 11):
        return "Noviembre"
    else:
        return "Diciembre"

#D 
def fecha_palabra(d,m,a):
    print(d,"de",meses(m),"de",a)

#EJercicio 10
def intervalo(hora,mins,seg):
    seg = 1 
    mins = 60*seg
    hora = 60*mins
    intervaloo = hora+mins+seg
    print(intervaloo)

#Ejercicio 12-13
def observar_clima():
    temp = float(input("Ingrese una temperatura: ? "))
    if (temp < 0):
        print("Helado")
    elif ((temp >= 0) and (temp <= 15)):
        print("Frio")
    elif ((temp >= 15) and (temp < 25)):
        print("Agradable")
    elif ((temp >= 25) and (temp <= 32)):
        print("Caluroso")
    else:
        print("Muy caluroso")

    if (temp > 15):
        print("Es necesario usar protector solar")
    else:
        print("NO es necesario usar protector solar")

#Ejercicio 14 
 


#-----------------------------PRACTICA 3----------------------------
#Ejercicio 1
#A
def lucca(n):
    """ Diseño:
    Numero: Natural
    Signatura:
        Nat Nat -> Nat
    Proposito:
        Calcular la suma de un numero menos 1 
        y el numero menos 2 
        lucca(0)=2 
        lucca(1)=1 
        lucca(5)=11 
    """
    if n == 0:
        return 2 
    elif n == 1:
        return 1 
    else:
        return lucca(n-1)+lucca(n-2)

#B 
def pell(n):
    """ Diseño:
    Numero = Natural
    Signatura: Nat Nat -> Nat 
    Proposito: Suma el numero dado menos 1 por su doble, mas el 
    numero restado a 2
    pell(0)=0 
    pell(1)=1 
    pell(5)=8+3=11 
    """
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return 2*pell(n-1)+pell(n-2)

#C 
def jacob(n):
    """ Diseño:
    Numero  = Natural
    Signatura = Nat Nat -> Nat 
    Proposito: Suma el anterior de un numero mas el 
    doble de su ante antecesor
    jacob(0)=0 
    jacob(1)=1 
    jacob(4)=3+4=7 """
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return jacob(n-1)+2*jacob(n-2) 

#Ejercicio 2
#a
def fibonacci_pasos(n):
	if n == 0 or n == 1:
		return n
	else: 
		resultado = fibonacci_pasos(n-1) + fibonacci_pasos(n-2)
		print("--DEB: El resultado intermedio para ", n," * factorial (", n-1, "y", n-2,"):",resultado)
		return resultado

#b
def suma_pasos(n):
	if n == 0:
		return n
	else:
		resultado = n+suma_pasos(n-1)
		print("--DEB: El resultado intermedio para la suma de los numeros hasta ",n,"es ",n-1,"y: ",resultado)
		return resultado

#Ejercicio 3
#A-B
def cincuenta(n):
	if n == 1:
		return 1
	else:
		return n+cincuenta(n-1)

#Ejercicio 4
def div_nat(n,m):
  if m>n:
    respuesta = 0
  else:
    respuesta = div_nat(n-m, m)+1
  return respuesta

def mult_nat (n,m):
  if m == 0:
    respuesta = 0
  elif m >= 1:
    respuesta = mult_nat (n,m-1)+n
  return respuesta

def pot_nat (n,m):
  if m ==0:
    respuesta = 1
  elif m >=1:
    respuesta = pot_nat(n, m-1)*n
  return respuesta

def rest_nat (n,m):
  if m >n:
    respuesta = 0
  elif m ==0 :
    respuesta = n
  else:
    respuesta = rest_nat (n-1,m-1)
  return respuesta


