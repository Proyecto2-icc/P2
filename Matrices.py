def sumaMatrices(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        suma = []
        for i in range(len(m1)):
            suma.append([])
            for j in range(len(m1[0])):
                suma[i].append(m1[i][j] + m2[i][j])
        return suma
    else:
        print("No se pueden sumar")

def restaMatrices(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        resta = []
        for i in range(len(m1)):
            resta.append([])
            for j in range(len(m1[0])):
                resta[i].append(m1[i][j] - m2[i][j])
        return resta
    else:
        print("No se pueden restar")

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
        
      for fila in m3:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")
    else:
        print("No se pueden multiplicar.")
    

def trasponer(m):
	matriz_traspuesta = []
	for i in range(len(m[0])):
		matriz_traspuesta.append([])
		for j in range(len(m)):
			matriz_traspuesta[i].append(m[j][i])
	for linea in matriz_traspuesta:
		print("[", end=" ")
		for elemento in linea:
			print(elemento, end=" ")
		print("]")

def multi_escalar(m, numero):
    matriz = list()
    for i in range(len(m)):
        matriz.append([])
        for j in range(len(m)):
            matriz[i].append(m[i][j]*numero)
    return matriz

def resolver_laberinto(maze):
    N = len(maze)
    maze = [
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0, 0, 1, 1]
    ]
    # lista para almacenar la matriz solucion
    MatrizSolucion = [[0] * N for _ in range(N)]
    def solvemaze(r, c):
        # r - row, c - columns
        # si se alcanza el destino, el laberinto se resuelve
        # destino de la ultima celda(maze[SIZE-1][SIZE-1])
        if (r == N - 1) and (c == N - 1):
            MatrizSolucion[r][c] = 1
            return True
        # Comprobar si podemos visitar en esta celda o no
        # los índices de la celda deben estar en (0,N-1) y la MatrizSolution [r] [c] == 0 es asegurarse de que la celda no esté ya visitada
        # maze[r][c] == 0 es asegurarse de que la celda no está bloqueado
        if r >= 0 and c >= 0 and r < N and c < N and MatrizSolucion[r][c] == 0 and maze[r][c] == 0:
            # si es seguro de visitar, usar celda
            MatrizSolucion[r][c] = 1
            # abajo
            if solvemaze(r + 1, c):
                return True
            # derecha
            if solvemaze(r, c + 1):
                return True
            # arriba
            if solvemaze(r - 1, c):
                return True
            # izquierda
            if solvemaze(r, c - 1):
                return True
            # backtracking
            MatrizSolucion[r][c] = 0
            return False
        return 0
    if (solvemaze(0, 0)):
        for i in MatrizSolucion:
            print(i)
    else:
        print("Error! La matriz no define un laberinto válido")