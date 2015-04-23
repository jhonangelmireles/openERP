#Esta funcion aparentemente sirve para verificar que el ultimo digito del RIF es el correcto o no lo es

def calculoUltimoDigitoRif(RIF):
	lista = RIF.split('-')
	#posicion 0  Letra - pos 1 num_intermedio- pos 3 numero final

	#rellena con 0  a la izq por ejemplo 123 -> 00000123
	num_intermedio_rif =  lista [1].rjust(8, '0')

	#A continuacion se inician el vector de multiplicadores
	array_multplicador = [ 4, 3, 2, 7, 6, 5, 4, 3, 2]

	#Letra supongo que es el primer caracter dado del RIF, 
	#defino un segundo array llamado numeros

	letra = lista[0]

	numero = []
	#Condiciones

	if letra == 'V':		#rif venezolano
		numeros =[ 1 ]
	elif	letra == 'E':	#rif extranjero
		numeros =[ 2 ]
	elif 	letra == 'J':	#rif juridico
		numeros =[ 3 ]
	elif  letra == 'P':		#rif personal
		numeros = [ 4 ]
	elif  letra == 'G':		#rif organismo del estado
		numeros = [ 5]

	numeros.extend( [ int(i) for i in num_intermedio_rif])
	 
	 #quedaria como lista de [ 1,1,9,5,9,8,6,0,6 ]
	 # Se inicia el vector de resultados y se efectuan las operacione

	resultados = []

	#multiplico los numeros * multiplicadores
	for i in range(9):
		resultados.append( array_multplicador[i] * numeros[i])

	#se suman todos los numeros

	suma = 0
	for i in range(9):
		suma=suma+resultados[i]

	#le saco el modulo a la sumatoria
	modulo_suma = suma%11

	#saco el dato a retornar
	retorno = 11 - modulo_suma

	if (retorno > 9)  or (retorno < 1):
		retorno = 0

	print RIF
	print 'valor calculado',retorno
	print 'valor introducido', lista[2]

	numero_final = int(lista[2])

	if(retorno!=numero_final):
		print 'el valor introducido es falso'
		return False
	else:
		print 'el valor introducido es verdadero'
		return True
	

RIF = 'V-18545601-0'
print calculoUltimoDigitoRif(RIF)
