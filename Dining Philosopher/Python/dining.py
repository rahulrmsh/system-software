# Dining Philosopher - Python

n = 0
state = []
class Condition:
    Thinking = 0
    Eating = 1
    Hungry = 2

def eat(x):
    state[x] = Condition.Hungry;
    if(state[(x + 4) % 5] == Condition.Thinking and state[(x - 1) % 5] == Condition.Thinking and state[x] == Condition.Hungry):
        state[x] = Condition.Eating;
        print("| {} is now eating.\n".format(x));
    else:
        print("| {} should wait\n".format(x));
    

int(input("Enter number of philosophers: "))
for i in range(n):
    state.append(Condition.Thinking)
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