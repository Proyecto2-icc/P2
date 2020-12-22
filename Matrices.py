def OK(n):
    try:
        n = float(n)
    except:
        n = OK(input("Caracter no valido: "))
    return n

def OKI(n):
    try:
        n = int(n)
    except:
        n = OKI(input("Caracter no valido: "))
    return n

def Crear_Matriz():
    matriz = list()
    filas = OKI(input("Filas: "))
    columnas = OKI(input("Columnas: "))
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor = OK(input(f"Ingrese la componente ({i + 1},{j + 1}): "))
            matriz[i].append(valor)
    return matriz

def dibujar_matriz(m):
    for fila in m:
        for valor in fila:
            print("\t", valor, end=" ")
        print()




def sumaMatrices(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        suma = []
        for i in range(len(m1)):
            suma.append([])
            for j in range(len(m1[0])):
                suma[i].append(m1[i][j] + m2[i][j])
        return suma
    else:
        return "No se pueden sumar debido a que no son de la misma dimensión"

def restaMatrices(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        resta = []
        for i in range(len(m1)):
            resta.append([])
            for j in range(len(m1[0])):
                resta[i].append(m1[i][j] - m2[i][j]) 
        return resta
    else:
        return "No se pueden restar debido a que no son de la misma dimensión"

def multiplicacion_matrices(m1, m2):
    if len(m1[0]) == len(m2):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)

        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]
        return m3
    else:
        return "No se pueden multiplicar debido a que el numero de columnas de la primera matriz es diferente del numero de filas de la segunda matriz."
 
def multi_escalar(m, numero):
    matriz = list()
    for i in range(len(m)):
        matriz.append([])
        for j in range(len(m)):
            matriz[i].append(m[i][j]*numero)

    return matriz

def trasponer(m):
    matriz_traspuesta = []
    for i in range(len(m[0])):
        matriz_traspuesta.append([])
        for j in range(len(m)):
            matriz_traspuesta[i].append(m[j][i])
    return matriz_traspuesta

def resolver_laberinto(maze):
    N = len(maze)
    MatrizSolucion = [[0] * N for _ in range(N)]   # lista para almacenar la matriz solucion
    def solvemaze(r, c):  # r - row, c - columns
        if (r == N - 1) and (c == N - 1):  # destino de la ultima celda(maze[SIZE-1][SIZE-1])
            MatrizSolucion[r][c] = 1
            return True                    # Comprobar si podemos visitar esta celda o no
        if r >= 0 and c >= 0 and r < N and c < N and MatrizSolucion[r][c] == 0 and maze[r][c] == 0:  #asegurarse de que la celda no está bloqueado
            MatrizSolucion[r][c] = 1  #si es seguro de visitar, usar celda
            if solvemaze(r + 1, c):   #abajo
                return True
            if solvemaze(r, c + 1):   #derecha
                return True
            if solvemaze(r - 1, c):   #arriba
                return True
            if solvemaze(r, c - 1):   #izquierda
                return True
            MatrizSolucion[r][c] = 0 #backtracking
            return False
        return 0
    if (solvemaze(0, 0)):
        for i in MatrizSolucion:
            print(i)
    else:
        print("Error! La matriz no define un laberinto válido")