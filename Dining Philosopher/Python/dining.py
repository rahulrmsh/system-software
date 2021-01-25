# Dining Philosopher - Python

class Condition:
    Thinking = 0
    Eating = 1
    Hungry = 2

n = int(input("Enter number of philosophers: "))
state = []
for i in range(n):
    state.append(Condition.Thinking)
while(1):
    res = int(input("| Choose from below : \n|1. Start Eating\n|2. Stop Eating\n|3. Exit\n| Enter Response : "))
    if res == 3:
        exit(0)
    elif res > 3:
        print("|\n| WRONG INPUT\n|\n");
        continue();