# Producer-Consumer - Python

x= 0, y = 1, s = 1, empty = 0, full = 10

def wait(x):
    while(x<=0):
        pass
    return --x

def signal(x):
    return ++x

def produce():
    global empty, s, x, full
    empty = wait(empty)
    s = wait(s)
    x = (x + 1) % 5
    print("\nProducer produced item : {}\n".format(x))
    full = signal(full)
    s = signal(s)

def consume():
    global empty, s, y, full
    full = wait(full)
    s = wait(s)
    print("\nConsumer consumed 1 item, total consumption : {}\n".format(y))
    y = (y + 1) % 5
    empty = signal(empty)
    s = signal(s)

while(True):
    print("\n1.Produce \n2.Consume \n3.Exit\n")
    op = int(input("\nEnter choice : "))
    if op == 1:
        if s > 0 and empty != 0:
            produce()
        else:
            print("\nBuffer is full\n")
    elif op == 2:
        if s > 0 and full != 0:
            consume()