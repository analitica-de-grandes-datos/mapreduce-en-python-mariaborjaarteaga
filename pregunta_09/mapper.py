#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        columnas = line.split("   ")
        columna3 = line.split("   ")[2].strip()
        columna3 = columna3.zfill(4)
        sys.stdout.write("{}   {}   {}\n".format(columna3, columnas[0], columnas[1]))