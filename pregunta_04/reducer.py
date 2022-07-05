#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    ckey = None
    total = 0
    for line in sys.stdin:
        key, val = line.split(",")
        val = int(val)
        if key == ckey:
            total += val
        else:
            if ckey is not None:
                sys.stdout.write("{},{}\n".format(ckey, total))
            ckey = key
            total = val

    sys.stdout.write("{},{}\n".format(ckey, total))
