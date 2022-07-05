#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#
import sys
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    ckey = None
    total = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == ckey:
            total += val
        else:
            if ckey is not None:
                sys.stdout.write("{}\t{}\n".format(ckey, total))
            ckey = key
            total = val

    sys.stdout.write("{}\t{}\n".format(ckey, total))
