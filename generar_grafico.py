
import matplotlib.pyplot as plt
import time
from caminos_pcb import CaminosPCB

def generar_grafico():
    tamanos = [5, 6, 7, 8, 9, 10]
    tiempos_dinamico = []
    tiempos_recursivo = []

    for tamano in tamanos:
        pcb = CaminosPCB(tamano, tamano)

        #medir tiempos de ejecución de ambas soluciones
        inicio = time.time()
        pcb.contar_caminos_dinamico()
        fin = time.time()
        tiempos_dinamico.append(fin - inicio)

        inicio = time.time()
        pcb.contar_caminos_recursivo()
        fin = time.time()
        tiempos_recursivo.append(fin - inicio)

    #graficar los tiempos de ejecución con todo lo soliitado
    plt.plot(tamanos, tiempos_dinamico, label='Programación Dinámica', marker='o')
    plt.plot(tamanos, tiempos_recursivo, label='Recursivo', marker='o')
    plt.xlabel('N x N')
    plt.ylabel('[s]')
    plt.title('Comparativa de tiempos de ejecución')
    plt.legend()
    plt.grid(True)
    plt.savefig("tiempos_de_ejecución_erecursivo_vs_PD", format='svg') #guardamos en svg
    plt.show()
