import json
import Menus
import Matrices 

file = open("memoria.json","r")
contenido = file.read()
file.close()

contenidoJSON = json.loads(contenido)

print()

opcion0 = input("ANTES DE INICIAR, ¿DESEA LIMPIAR LA MEMORIA?. Escriba SI o NO: ")
while opcion0!= "SI" and opcion0!= "NO":
        opcion0 = input("Escriba SI o NO, cualquier otra entrada es inválida: ")
if opcion0 == "SI":
    MATRICES = [0,0,0,0,0,0,0,0,0,0] 
    RESULTADOS = [0,0,0,0,0,0,0,0,0,0]  
else:
    MATRICES = contenidoJSON["Memoria1"]
    RESULTADOS = contenidoJSON["Memoria2"]
print()

Menus.titulo()

DICCIONARIO = {"Memoria1":MATRICES,"Memoria2":RESULTADOS}


while True:
	Menus.opciones()
	opcion = input("INGRESE UNA OPCIÓN: ")
	while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
		opcion = input("Introduzca una opción válida: ")

	if opcion == "1":
		print()
		espacio_memoria = input("¿En que espacio de la primera memoria desea guardar la matriz? Ingrese un número del 1 al 10: ")
		while espacio_memoria != "1" and espacio_memoria != "2" and espacio_memoria != "3" and espacio_memoria != "4" and espacio_memoria != "5" and espacio_memoria != "6" and espacio_memoria != "7" and espacio_memoria != "8" and espacio_memoria != "9" and espacio_memoria != "10":
			espacio_memoria = input("Numero inválido, ingrese un número del 1 al 10: ")
		MATRICES[int(espacio_memoria) - 1] = Matrices.Crear_Matriz()
		print()
		Matrices.dibujar_matriz(MATRICES[int(espacio_memoria) - 1])

	if opcion == "2":
		Menus.operar_matrices()
		opcion2 = input("INGRESE UNA OPCIÓN: ")
		while opcion2 != '1' and opcion2 != '2' and opcion2 != '3' and opcion2 != '4' and opcion2 != '5' and opcion2 != '6':
			opcion = input("Introduzca una opción válida: ")
		if opcion2 == "1":
			print()
			print("Elija las posiciones de la primera memoria de las matrices que quiere Sumar: ")
			print()
			matriz1 = input("Ingrese posicion de la primera matriz: ")
			while matriz1 != "1" and matriz1 != "2" and matriz1 != "3" and matriz1 != "4" and matriz1 != "5" and matriz1 != "6" and matriz1 != "7" and matriz1 != "8" and matriz1 != "9" and matriz1 != "10":
				matriz1 = input("Ingrese una posicion válida: ")
			print()
			matriz2 = input("Ingrese posicion de la segunda matriz: ")
			while matriz2 != "1" and matriz2 != "2" and matriz2 != "3" and matriz2 != "4" and matriz2 != "5" and matriz2 != "6" and matriz2 != "7" and matriz2 != "8" and matriz2 != "9" and matriz2 != "10":
				matriz2 = input("Ingrese una posicion válida: ")
			suma = Matrices.sumaMatrices(MATRICES[int(matriz1) - 1], MATRICES[int(matriz2) - 1])
			print()
			print("RESULTADO:")
			Matrices.dibujar_matriz(suma)

			guardar_resultado = input("¿Desea guardar el resultado? Escriba SI o NO: ")
			while guardar_resultado != "SI" and guardar_resultado != "NO":
				guardar_resultado = input("Escriba SI o NO, cualquier otra entrada es inválida: ")
			if guardar_resultado == "SI":
				print()
				espacio_segunda_memoria=input("¿En que espacio de la segunda memoria desea guardar la matriz? Ingrese un número del 1 al 10: ")
				print()
				while espacio_segunda_memoria!="1" and espacio_segunda_memoria!="2" and espacio_segunda_memoria!="3" and espacio_segunda_memoria!="4" and espacio_segunda_memoria!="5" and espacio_segunda_memoria!="6" and espacio_segunda_memoria!="7" and espacio_segunda_memoria!="8" and espacio_segunda_memoria!="9" and espacio_segunda_memoria!="10":
					espacio_segunda_memoria=input("Numero inválida, ingrese un número del 1 al 10: ")
				RESULTADOS[int(espacio_segunda_memoria)-1] = suma
				print("GUARDADO.")

		if opcion2 == "2":
			print()
			print("Elija las posiciones de memoria de las matrices que quiere Restar: ")
			print()
			matriz1 = input("Ingrese posicion de la primera matriz: ")
			while matriz1 != "1" and matriz1 != "2" and matriz1 != "3" and matriz1 != "4" and matriz1 != "5" and matriz1 != "6" and matriz1 != "7" and matriz1 != "8" and matriz1 != "9" and matriz1 != "10":
				matriz1 = input("Ingrese una posicion válida: ")
			print()
			matriz2 = input("Ingrese posicion de la segunda matriz: ")
			while matriz2 != "1" and matriz2 != "2" and matriz2 != "3" and matriz2 != "4" and matriz2 != "5" and matriz2 != "6" and matriz2 != "7" and matriz2 != "8" and matriz2 != "9" and matriz2 != "10":
				matriz2 = input("Ingrese una posicion válida: ")
			resta = Matrices.restaMatrices(MATRICES[int(matriz1) - 1], MATRICES[int(matriz2) - 1])
			print()
			print("RESULTADO:")
			Matrices.dibujar_matriz(resta)


			guardar_resultado = input("¿Desea guardar el resultado? Escriba SI o NO: ")
			while guardar_resultado != "SI" and guardar_resultado != "NO":
				guardar_resultado = input("Escriba SI o NO, cualquier otra entrada es inválida: ")
			if guardar_resultado == "SI":
				print()
				espacio_segunda_memoria=input("¿En que espacio de la segunda memoria desea guardar la matriz? Ingrese un número del 1 al 10: ")
				print()
				while espacio_segunda_memoria!="1" and espacio_segunda_memoria!="2" and espacio_segunda_memoria!="3" and espacio_segunda_memoria!="4" and espacio_segunda_memoria!="5" and espacio_segunda_memoria!="6" and espacio_segunda_memoria!="7" and espacio_segunda_memoria!="8" and espacio_segunda_memoria!="9" and espacio_segunda_memoria!="10":
					espacio_segunda_memoria=input("Numero inválida, ingrese un número del 1 al 10: ")
				RESULTADOS[int(espacio_segunda_memoria)-1] = resta
				print("GUARDADO.")

		if opcion2 == "3":
			print()
			print("Elija las posiciones de memoria de las matrices que quiere Multiplicar ")
			print()
			matriz1 = input("Ingrese posicion de la primera matriz: ")
			while matriz1 != "1" and matriz1 != "2" and matriz1 != "3" and matriz1 != "4" and matriz1 != "5" and matriz1 != "6" and matriz1 != "7" and matriz1 != "8" and matriz1 != "9" and matriz1 != "10":
				matriz1 = input("Ingrese una posicion válida: ")
			print()
			matriz2 = input("Ingrese posicion de la segunda matriz: ")
			while matriz2 != "1" and matriz2 != "2" and matriz2 != "3" and matriz2 != "4" and matriz2 != "5" and matriz2 != "6" and matriz2 != "7" and matriz2 != "8" and matriz2 != "9" and matriz2 != "10":
				matriz2 = input("Ingrese una posicion válida: ")
			multiplicacion = Matrices.multiplicacion_matrices(MATRICES[int(matriz1) - 1], MATRICES[int(matriz2) - 1])
			print()
			print("RESULTADO:")
			Matrices.dibujar_matriz(multiplicacion)
    
			guardar_resultado = input("¿Desea guardar el resultado? Escriba SI o NO: ")
			while guardar_resultado != "SI" and guardar_resultado != "NO":
				guardar_resultado = input("Escriba SI o NO, cualquier otra entrada es inválida: ")
			if guardar_resultado == "SI":
				print()
				espacio_segunda_memoria = input("¿En que espacio de la segunda memoria desea guardar la matriz? Ingrese un número del 1 al 10: ")
				print()
				while espacio_segunda_memoria != "1" and espacio_segunda_memoria != "2" and espacio_segunda_memoria != "3" and espacio_segunda_memoria != "4" and espacio_segunda_memoria != "5" and espacio_segunda_memoria != "6" and espacio_segunda_memoria != "7" and espacio_segunda_memoria != "8" and espacio_segunda_memoria != "9" and espacio_segunda_memoria != "10":
					espacio_segunda_memoria = input("Numero inválida, ingrese un número del 1 al 10: ")
				RESULTADOS[int(espacio_segunda_memoria) - 1] = multiplicacion
				print("GUARDADO.")

		if opcion2 == "4":
			print()
			print("Elija la posicion de memoria de la matriz que quiere Multiplicar Por un Escalar ")
			print()
			matriz1 = input("Ingrese posicion de la primera matriz: ")
			while matriz1 != "1" and matriz1 != "2" and matriz1 != "3" and matriz1 != "4" and matriz1 != "5" and matriz1 != "6" and matriz1 != "7" and matriz1 != "8" and matriz1 != "9" and matriz1 != "10":
				matriz1 = input("Ingrese una posicion válida: ")
			print()
			escalar = Matrices.OK(input("Ingrese el numero que va a multiplicar a la matriz: "))
			multiplicacion_escalar = Matrices.multi_escalar(MATRICES[int(matriz1) - 1],escalar)
			print()
			print("RESULTADO:")
			Matrices.dibujar_matriz(multiplicacion_escalar)


			guardar_resultado = input("¿Desea guardar el resultado? Escriba SI o NO: ")
			while guardar_resultado != "SI" and guardar_resultado != "NO":
				guardar_resultado = input("Escriba SI o NO, cualquier otra entrada es inválida: ")
			if guardar_resultado == "SI":
				print()
				espacio_segunda_memoria=input("¿En que espacio de la segunda memoria desea guardar la matriz? Ingrese un número del 1 al 10: ")
				print()
				while espacio_segunda_memoria!="1" and espacio_segunda_memoria!="2" and espacio_segunda_memoria!="3" and espacio_segunda_memoria!="4" and espacio_segunda_memoria!="5" and espacio_segunda_memoria!="6" and espacio_segunda_memoria!="7" and espacio_segunda_memoria!="8" and espacio_segunda_memoria!="9" and espacio_segunda_memoria!="10":
					espacio_segunda_memoria=input("Numero inválida, ingrese un número del 1 al 10: ")
				RESULTADOS[int(espacio_segunda_memoria)-1] = multiplicacion_escalar
				print("GUARDADO.")

		if opcion2 == "5":
			print()
			print("Elija la posicion de memoria de la matriz la cual quiere obtener su Traspuesta ")
			print()
			matriz1 = input("Ingrese posicion de la primera matriz: ")
			while matriz1 != "1" and matriz1 != "2" and matriz1 != "3" and matriz1 != "4" and matriz1 != "5" and matriz1 != "6" and matriz1 != "7" and matriz1 != "8" and matriz1 != "9" and matriz1 != "10":
				matriz1 = input("Ingrese una posicion válida: ")
			print()
			traspuesta = Matrices.trasponer(MATRICES[int(matriz1) - 1])
			print()
			print("RESULTADO:")
			Matrices.dibujar_matriz(traspuesta)


			guardar_resultado = input("¿Desea guardar el resultado? Escriba SI o NO: ")
			while guardar_resultado != "SI" and guardar_resultado != "NO":
				guardar_resultado = input("Escriba SI o NO, cualquier otra entrada es inválida: ")
			if guardar_resultado == "SI":
				print()
				espacio_segunda_memoria=input("¿En que espacio de la segunda memoria desea guardar la matriz? Ingrese un número del 1 al 10: ")
				print()
				while espacio_segunda_memoria!="1" and espacio_segunda_memoria!="2" and espacio_segunda_memoria!="3" and espacio_segunda_memoria!="4" and espacio_segunda_memoria!="5" and espacio_segunda_memoria!="6" and espacio_segunda_memoria!="7" and espacio_segunda_memoria!="8" and espacio_segunda_memoria!="9" and espacio_segunda_memoria!="10":
					espacio_segunda_memoria=input("Numero inválida, ingrese un número del 1 al 10: ")
				RESULTADOS[int(espacio_segunda_memoria)-1] = traspuesta
				print("GUARDADO.")

		if opcion2 == '6':
			print()
			print("Elija posicion de memoria de matriz de la cual quiera resolver el laberinto: ")
			print()
			m1 = input("Ingrese posicion de la matriz: ")
			while m1 != "1" and m1 != "2" and m1 != "3" and m1 != "4" and m1 != "5" and m1 != "6" and m1 != "7" and m1 != "8" and m1 != "9" and m1 != "10":
				m1 = input("Ingrese una posicion válida: ")
			print()
			m_laberinto = Matrices.resolver_laberinto(MATRICES[int(m1)-1])
			print()

			guardar_resultado = input("¿Desea guardar el resultado? Escriba SI o NO: ")
			while guardar_resultado != "SI" and guardar_resultado != "NO":
				guardar_resultado = input("Escriba SI o NO, cualquier otra entrada es inválida: ")
			if guardar_resultado == "SI":
				print()
				espacio_segunda_memoria=input("¿En que espacio de la segunda memoria desea guardar la matriz? Ingrese un número del 1 al 10: ")
				print()
				while espacio_segunda_memoria!="1" and espacio_segunda_memoria!="2" and espacio_segunda_memoria!="3" and espacio_segunda_memoria!="4" and espacio_segunda_memoria!="5" and espacio_segunda_memoria!="6" and espacio_segunda_memoria!="7" and espacio_segunda_memoria!="8" and espacio_segunda_memoria!="9" and espacio_segunda_memoria!="10":
					espacio_segunda_memoria=input("Numero inválida, ingrese un número del 1 al 10: ")
				RESULTADOS[int(espacio_segunda_memoria)-1] = m_laberinto
				print("GUARDADO.")

	if opcion == "3":
		print()
		print("MATRICES GUARDADAS EN PRIMERA MEMORIA: ")
		print()
		for i in range(10):
			print(f"Matriz {i+1}")
			try:
				Matrices.dibujar_matriz(MATRICES[i])
			except TypeError:
				None 
			print()

		print()
		print("MATRICES GUARDADAS EN SEGUNDA MEMORIA: ")
		print()
		for i in range(10):
			print(f"Matriz {i+1}")
			try:
				Matrices.dibujar_matriz(RESULTADOS[i])
			except TypeError:
				None 
			print()

	if opcion == "4":
		break

with open("memoria.json","w") as f:
    json.dump(DICCIONARIO,f)

