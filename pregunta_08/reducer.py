#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    ckey = None
    suma = 0
    conteo = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = float(val)
        if key == ckey:
            suma = suma + val
            conteo = conteo + 1

        else:
            if ckey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(ckey, suma,suma / conteo))
            ckey = key
            suma = val
            conteo = 1

    sys.stdout.write("{}\t{}\t{}\n".format(ckey, suma, suma / conteo))
