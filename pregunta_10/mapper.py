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

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
        col_a = line.split()[0].zfill(2)
        letters = line.split()[1]

        for letter in letters.split(","):

            #
            # escribe al flujo estandar de salida
            #
            sys.stdout.write("{}\t{}\n".format(letter, col_a))