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

        key, val1, val2 = line.split("\t")

        if val1 == '000':
            val1 = '0'
        else:    
            val1 = val1.lstrip('0')
            
        val2 = val2.strip()

        sys.stdout.write("{}\t{}\t{}\n".format(key, val2, val1))