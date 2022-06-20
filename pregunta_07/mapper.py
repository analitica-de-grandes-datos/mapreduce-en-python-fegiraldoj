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

        col_a = line.split()[0]
        col_b = line.split()[1]
        col_c = line.split()[2].zfill(3)

        sys.stdout.write("{}\t{}\t{}\n".format(col_a,col_c,col_b))