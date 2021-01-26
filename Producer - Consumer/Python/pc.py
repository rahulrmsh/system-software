# Producer-Consumer - Python

x= 0, y = 1, s = 1, empty = 0, full = 10
def wait(x):
    while(x<=0):
        pass
    return --x

def signal(x):
    return ++x

while(True):
    print("\n1.Produce \n2.Consume \n3.Exit\n")
    op = int(input("\nEnter choice : "))