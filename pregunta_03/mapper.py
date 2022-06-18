#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/ python3

#
# Esta es la funcion que mapea la entrada a parejas (clave, valor)
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    for line in sys.stdin:

        col_a = line.strip().split(",")[0]
        col_b = line.strip().split(",")[1]
        sys.stdout.write("{},{}\n".format(col_b,col_a))