def PrimerMenu():
  print("MENU PRINCIPAL","[1] Ingresar Matrices","[2] Operar Matrices","[3] Mostrar Matrices","[4] Salir",sep='\n')
  opcion = input("Seleccione opción: ")
  if opcion in "1234":
    return opcion
  else:
    print("Opción incorrecta, intente nuevamente")
    return 0

def IngresarMatrices():
    while True:
        print("[1] Ingresar una matriz a una de memoria de matriz especificada","[2] Ingresar una matriz a una memoria libre","[3] Salir",sep='\n')
        opcion = input("Seleccione opción: ")
        if opcion in "123":
            return opcion
        else:
            print("Opción incorrecta, intente nuevamente")

def OperarMatrices():
    while True:
        print("OPERAR MATRICES","[1] Suma de matrices","[2] Resta de matrices","[3] Multiplicación de matrices","[4] Trasposición de matriz","[5] Multiplicación por un escalar","[6] Salir",sep='\n')
        opcion = input("Seleccione opción: ")
        if opcion in "123456":
            return opcion
        else:
            print("Opción incorrecta, intente nuevamente")
    return

def MostrarMatrices():
    while True:
        print("MOSTRAR MATRICES","[1] Lista de matrices guardadas","[2] Mostrar contenido de una matriz","[3] Salir",sep='\n')
        opcion = input("Seleccione opción: ")
        if opcion in "123":
            return opcion
        else:
            print("Opción incorrecta, intente nuevamente")
    return

def CrearMatriz(MM,n = 0, opcion_escogida = 0):
    f = lee_entero("Filas: ")
    c = lee_entero("Columnas: ")
    matriz = [[0] * c for i in range(f)]
    for i in range(f):
        for j in range(c):
          matriz[i][j] = int(input(f"M[{i+1}][{j+1}] = "))
    if(opcion_escogida ==0 ):
      pos = lee_entero("Ingrese posición de memoria: ")
    else :
      for i in range(n):
        if MM[i]:
          pass
        else:
          pos = i
    MM[pos] = matriz
    return matriz

def lee_entero(mensaje):
  n = input(mensaje)
  try:
      n = int(n)
      return n
  except ValueError:
      print("La entrada es incorrecta, vuelva a intentarlo")

def dibujar_matriz(m):
    for fila in m:
        for valor in fila:
            print("\t", valor, end=" ")
        print()