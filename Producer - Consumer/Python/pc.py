# Producer-Consumer - Python

def wait(x):
    while(x<=0):
        pass
    return --x

def signal(x):
    return ++x

def produce(empty, s, x, full):
    empty = wait(empty)
    s = wait(s)
    x = (x + 1) % 10
    print("\nProducer produced item : {}\n".format(x))
    full = signal(full)
    s = signal(s)
    return empty, s, x, full

def consume(empty, s, y, full):
    full = wait(full)
    s = wait(s)
    print("\nConsumer consumed 1 item, total consumption : {}\n".format(y))
    y = (y + 1) % 10
    empty = signal(empty)
    s = signal(s)
    return empty, s, x, full

x = 0
y = 1
s = 1
empty = 10
full = 4
while(True):
    print("\n1.Produce \n2.Consume \n3.Exit\n")
    op = int(input("\nEnter choice : "))
    if op == 1:
        if s == 1 and empty != 0:
            empty, s, x, full = produce(empty, s, x, full)
        else:
            print("\nBuffer is full\n")
    elif op == 2:
        if s == 1 and full != 0:
            empty, s, x, full = consume(empty, s, x, full)
    elif op == 3:
        exit(0)