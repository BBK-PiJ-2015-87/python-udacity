import sys

def printOne():
    print("one")

def printTwo():
    print("two")


def main():
    print(dir(sys))
    print(sys.argv)
    printOne()
    printTwo()
    sys.exit(1)

if __name__ == '__main__':
    main()

# example of map function
list1 = [1,2,3]
def sqr2(x): return x**2
print(list(map(sqr2,list1)))