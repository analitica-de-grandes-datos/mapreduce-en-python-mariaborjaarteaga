#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    ckey = None
    total = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = val.strip()
        if key == ckey:
            n = n + "," + str(int(val))
        else:
            if ckey is not None:
                sys.stdout.write("{}\t{}\n".format(ckey, n))
            ckey = key
            n = str(int(val))

    sys.stdout.write("{}\t{}\n".format(ckey, n))
