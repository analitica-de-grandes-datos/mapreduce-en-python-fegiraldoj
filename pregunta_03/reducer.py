#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin python3

import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':   

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        val, key = line.strip().split(",")
        val = int(val)

        sys.stdout.write("{},{}\n".format(key, val))