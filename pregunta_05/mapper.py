#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        columnas = line.split(" ")
        sys.stdout.write("{},1\n".format(columnas[3].split("-")[1]))