#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/ python3

#
# Esta es la funcion que mapea la entrada a parejas (clave, valor)
#
import sys 
 
if __name__ == "__main__": 
    for line in sys.stdin: 
        # se separan las columnas separadas 
        lista = line.split(" ") 
        # se genera la salida del dato llamando la columna objetivo 
        sys.stdout.write("{},1\n".format(lista[0]))