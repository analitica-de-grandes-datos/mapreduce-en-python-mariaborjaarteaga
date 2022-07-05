#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    total = 0
    for line in sys.stdin:
        columnas = line.split("   ")
        sys.stdout.write(
            "{}   {}   {}\n".format(columnas[1], columnas[2].strip(), int(columnas[0]))
        )
        if total >= 5:
            break
        total = total+ 1