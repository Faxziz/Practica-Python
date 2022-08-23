#Ejercicio 1
def datosDePalo(valor,palo):
	return (palo == "Diamond") or (palo == "Trebol") or (palo == "Pica") or (palo == "Corazon")

def datos_fuera_rangoValor(valor,palo):
	return (valor < 1) or (valor > 13)

def validar_carta(valor,palo):
	if datosDePalo(valor,palo):
		respuesta = True
	elif datos_fuera_rangoValor(valor,palo):
		respuesta = False
	else:
		respuesta = False
	
	return respuesta

def newCarta(valor,palo):
	if validar_carta(valor,palo):
		respuesta = (valor,palo)
	else:
		respuesta = ("Carta invalida","Carta invalida")
	
	return respuesta

#Ejercicio 2
def rango_fueraSegundo(hora,minuto,segundo):
	return (segundo > 60) or (segundo < 1)

def rango_fueraMinuto(hora,minuto,segundo):
	return (minuto > 60) or (segundo < 1)

def rango_fueraHora(hora,minuto,segundo):
	return (hora > 24) or (segundo < 1)

def validarTiempo(hora,minuto,segundo):
	if rango_fueraSegundo(hora,minuto,segundo):
		respuesta = False
	elif rango_fueraMinuto(hora,minuto,segundo):
		respuesta = False
	elif rango_fueraHora(hora,minuto,segundo):
		respuesta = False 
	else:
		respuesta = True
	return respuesta

def crearTiempo(hora,minuto,segundo):
	if validarTiempo(hora,minuto,segundo):
		respuesta = (hora,minuto,segundo)
	else:
		respuesta = ("Tiempo Invalido")
	return respuesta

#3
def suma_tiempo1 (t1, t2):
	suma_horas = t1[0] + t2 [0]
	suma_min = t1 [1] + t2 [1]
	suma_seg = t1[2] + t2[2]
	if suma_seg > 60:
		suma_min +=1
		suma_seg -= 60
	elif suma_min > 60:
		suma_hora += 1
		suma_min -= 60
	else:
		print("Suma invalida")
	print(suma_horas,suma_min,suma_seg)
		
def resta_tiempo(t1, t2):
	h1,m1,s1 = t1
	h2,m2,s2 = t2
	resta_horas = h1-h2
	resta_min = m1-m2
	resta_seg = s1-s2
	if h1 > h2:
		resta_horas = h1 - h2
	elif m1 > m2:
		resta_min = m1 - m2
	elif s1 > s2:
		resta_seg = s1 - s2
	else:
		print("La resta es invalida")
	
	print(resta_horas,resta_min,resta_seg)

#Ejercicio 3
def fechaFueraRango(dia,mes,year):
	return (dia < 1) or (dia > 31) or (mes < 1) or (mes > 12) or (year < 0)

def datosMes30(dia,mes,year):
	return (((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and (1 <= dia <= 30))

def datosMes31(dia,mes,year):
	return (((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)) and (1 <= dia <= 31))

def validarFecha(dia,mes,year):
	if datosMes30(dia,mes,year):
		respuesta = True
	elif datosMes31(dia,mes,year):
		respuesta = True
	elif fechaFueraRango(dia,mes,year):
		respuesta = False
	else:
		respuesta = False
	return respuesta

def newFecha(dia,mes,year):
	if validarFecha(dia,mes,year):
		respuesta = (dia,mes,year)
	else:
		respuesta = "Fecha invalida"
	
	return respuesta
def meses(m):
	if m == 1:
		mes = "Enero"
	elif m == 2:
		mes = "Febrero"
	elif m == 3:
		mes = "Marzo"
	elif m == 4:
		mes = "Abril"
	elif m == 5:
		mes = "Mayo"
	elif m == 6:
		mes = "Junio"
	elif m == 7:
		mes = "Julio"
	elif m == 8:
		mes = "Agosto"
	elif m == 9:
		mes = "Septiembre"
	elif m == 10:
		mes = "Octubre"
	elif m == 11:
		mes = "Noviembre"
	else:
		mes = "Diciembre"
	
	return mes

def diaAnteriorNum (f):
    d,m,a = f
    if d == 1:
        if (meses(m)):
            if m == 1:
                dia_anterior=(31,meses(m),a-1)
            else:
                 dia_anterior = (31,(meses(m-1)),a)
        elif m == 3:
            dia_anterior=(28,(meses(m-1)),a)
        else:
            dia_anterior= (30,(meses(m-1)),a)
    else:
        dia_anterior = (d-1,meses(m),a)
    return dia_anterior

#Ejercicio 4
#DIseño de datos:
#Una ficha de domino es: (n1,n2)
#Siendo (int, int)
#Donde ambos numeros representan un numero del 0-9
#Construccion de la ficha:
#newFicha: Int Int -> Ficha
def fueraRangoParte1(n1,n2):
	return (n1 < 0) or (n1 > 9)
	
def fueraRangoParte2(n1,n2):
	return (n2 < 0) or (n2 > 9)

def validarFicha(n1,n2):
	if fueraRangoParte1(n1,n2):
		respuesta = False
	elif fueraRangoParte2(n1,n2):
		respuesta = False
	else:
		respuesta = True
		
	return respuesta
		
def crearFicha(n1,n2):
	if validarFicha(n1,n2):
		respuesta = (n1,n2)
	else:
		respuesta = "Ficha Invalida"
	return respuesta

def puedeJugar (f1,f2):
	num1,num2 = f1
	num3,num4 = f2
	if num1==num3:
		respuesta = "Encajan"
	elif num1==num4:
		respuesta = "Encajan"
	elif num2==num3:
		respuesta = "Encajan"
	elif num2==num4:
		respuesta = "Encajan"
	else:
		respuesta = "No encajan"
	return respuesta

#Ejercicio 5

def crearPersona(nombre,apellido,direccion,telefono,edad):
	respuesta = (nombre,apellid,direccion,telefono,edad)
	return respuesta

def familiares(p1,p2):
	n1,a1,d1,t1,e1 = p1
	n2,a2,d2,t2,e2 = p2
	if ((a1 == a2) and (d1 == d2)):
		respuesta = "Son Familia"
	else:
		respuesta = "No tienen relacion"
	return respuesta

#Ejercicio 8
def crearAuto(modelo,year,patente,combustible,rendimiento):
	respuesta = (modelo,year,patente,combustible,rendimiento)
	return respuesta

def rendimientoO(modelo,year,patente,combustible,rendimiento):
	if ((year >= 1) and (year <= 5)):
		rendimiento = (rendimiento  - (rendimiento*0.02))
	elif ((year >= 6) and (year < 10)):
		rendimiento = (rendimiento - (rendimiento*0.06))
	elif ((year >= 10) and (year <= 15)):
		rendimiento = (rendimiento - (rendimiento*0.1))
	else:
		rendimiento = (rendimiento - (rendimiento*0.15))
	
	return rendimiento
		
def costoViaje(auto1,km):
	mod,a1,pat,comb,rendimiento = auto1
	sumaTotal = 0	
	peaje = (km//100)*50
	sumaTotal = ((km/(rendimientoO(mod,a1,pat,comb,rendimiento)))*comb)+peaje
	return sumaTotal





