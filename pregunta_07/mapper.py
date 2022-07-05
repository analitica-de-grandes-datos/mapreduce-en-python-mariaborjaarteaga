#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        columna3 = line.split("   ")[2].strip()
        columna3 = columna3.zfill(4)
        sys.stdout.write("{} {} {}\n".format(str(line.split("   ")[0]), columna3, line.split("   ")[1]))