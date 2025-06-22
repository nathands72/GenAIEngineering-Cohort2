import sys

def add(a,b):
    print("Adding %d + %d = %d" % (a, b, a+b))
    
if __name__ == "__main__":
    add(int(sys.argv[1]), int(sys.argv[2]))