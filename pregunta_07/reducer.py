#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    for line in sys.stdin:
        columnas = line.split(" ")
        sys.stdout.write("{}   {}   {}\n".format(columnas[0], columnas[2].strip(), int(columnas[1])))