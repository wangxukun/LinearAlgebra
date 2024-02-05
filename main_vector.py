import sys
from playLA.Vector import Vector
import playLA.module1

if __name__ == '__main__':
    vec = Vector([5, 2])
    print(vec)
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero2 = Vector.zero(2)
    print(zero2)
    print("{} + {} = {}".format(vec, zero2, vec + zero2))

    print("Printer print : ")
    playLA.module1.printer(2025)


def demo():
    contents = sys.stdin.read()
    sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))


"""运行程序：python main_vector.py zero @ <./001.txt> outfile.txt"""
demo()
