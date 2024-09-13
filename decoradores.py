import time

def decorador_tiempo(funcion): #creamos el decorador para tiempo con la funcion envolutra
    def envoltura(*args, **kwargs):
        inicio_tiempo = time.time()
        resultado = funcion(*args, **kwargs)
        fin_tiempo = time.time()
        tiempo_transcurrido = fin_tiempo - inicio_tiempo
        print(f"Tiempo de ejecución de {funcion.__name__}: {tiempo_transcurrido:.6f} segundos")
        return resultado
    return envoltura
