#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin python3

import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    top_n = 6
    cant = 0

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        val1, key, val2 = line.split("\t")
        key = key.strip()
        val1 = val1.strip()
        val2 = val2.strip()
        
        if val1 == '000':
            val1 = '0'
        else:    
            val1 = val1.lstrip('0')

        sys.stdout.write("{}   {}   {}\n".format(key, val2, val1))
        cant += 1
        if cant == top_n: break