# Dining Philosopher - Python

n = 0
arr = []
class Condition:
    Thinking = 0
    Eating = 1
    Hungry = 2

def eat(x):
    arr[x] = Condition.Hungry;
    if(arr[(x + 4) % n] == Condition.Thinking and arr[(x - 1) % n] == Condition.Thinking and arr[x] == Condition.Hungry):
        arr[x] = Condition.Eating;
        print("| {} is now eating.\n".format(x));
    else:
        print("| {} should wait\n".format(x));
    
def think(x):
    arr[x] = Condition.Thinking;
    eat((x-1)%5);
    eat((x+4)%5);
    print("| {} stopped eating.".format(x));

int(input("Enter number of philosophers: "))
for i in range(n):
    arr.append(0)
print(arr)
while(1):
    res = int(input("| Choose from below : \n|1. Start Eating\n|2. Stop Eating\n|3. Exit\n| Enter Response : "))
    if res == 3:
        exit(0)
    elif res > 3:
        print("|\n| WRONG INPUT\n|\n");
        continue;
    id = int(input("| Enter philosopher id : "))
    if res == 1:
        eat(id)
    elif res == 2:
        think(2)