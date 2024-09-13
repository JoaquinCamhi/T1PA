

from decoradores import decorador_tiempo

class CaminosPCB:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas

    @decorador_tiempo #utilizamos el decorador
    def contar_caminos_dinamico(self):
        tabla = [[0] * self.columnas for _ in range(self.filas)]
        
        #se inicializar la primera fila y primera columna
        for i in range(self.filas):
            tabla[i][0] = 1
        for j in range(self.columnas):
            tabla[0][j] = 1
        
        #se rellenar la tabla con las sumas de los caminos posibles
        for i in range(1, self.filas):
            for j in range(1, self.columnas):
                tabla[i][j] = tabla[i-1][j] + tabla[i][j-1]
        
        return tabla[self.filas - 1][self.columnas - 1]

    @decorador_tiempo 
    def contar_caminos_recursivo(self, fila=0, columna=0):
        if fila == self.filas - 1 and columna == self.columnas - 1:
            return 1
        if fila >= self.filas or columna >= self.columnas:
            return 0
        return self.contar_caminos_recursivo(fila + 1, columna) + self.contar_caminos_recursivo(fila, columna + 1)
