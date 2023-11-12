RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

for i in range(11):
    if i == 5:
        print(f'{WHITE}{"  " * (7)}{RED}{"  " * (7)}{WHITE}{"  " * (7)}{END}')
    elif i == 4 or i == 6:
        print(f'{WHITE}{"  " * (8)}{RED}{"  " * (5)}{WHITE}{"  " * (8)}{END}')
    elif i == 3 or i == 7:
        print(f'{WHITE}{"  " * (9)}{RED}{"  " * (3)}{WHITE}{"  " * (9)}{END}')
    else:
        print(f'{WHITE}{"  " * (21)}{END}')

for i in range(10):
    if i == 2 or i == 8:
        print(f'{WHITE}{"  " * (5)}{BLUE}{"  " * (1)}{WHITE}{"  " * (5)}{BLUE}{"  " * (1)}{WHITE}{"  " * (5)}{END}')
    elif i == 3 or i == 7:
        print(f'{WHITE}{"  " * (4)}{BLUE}{"  " * (1)}{WHITE}{"  " * (1)}{BLUE}{"  " * (1)}{WHITE}{"  " * (3)}{BLUE}{"  " * (1)}{WHITE}{"  " * (1)}{BLUE}{"  " * (1)}{WHITE}{"  " * (4)}{END}')
    elif i == 4 or i == 6:
        print(f'{WHITE}{"  " * (3)}{BLUE}{"  " * (1)}{WHITE}{"  " * (3)}{BLUE}{"  " * (1)}{WHITE}{"  " * (1)}{BLUE}{"  " * (1)}{WHITE}{"  " * (3)}{BLUE}{"  " * (1)}{WHITE}{"  " * (3)}{END}')
    elif i == 5:
        print(f'{WHITE}{"  " * (2)}{BLUE}{"  " * (1)}{WHITE}{"  " * (5)}{BLUE}{"  " * (1)}{WHITE}{"  " * (5)}{BLUE}{"  " * (1)}{WHITE}{"  " * (2)}{END}')
    else:
        print(f'{WHITE}{"  " * (17)}{END}')


import math

def y(x):
    return -3 * x

x_min = -10
x_max = 10
step = 0.1

for x in range(int(x_min * 10), int(x_max * 10), int(step * 10)):
    x_val = x / 10
    y_val = int(y(x_val))
    print("\033[94m" + "\033[4m" + " " * (y_val + 10) + "*" + "\033[0m")

f = open('sequence.txt')
d = [float(x[1:-1]) if x[0] != "-" else -1 * float(x[1:-1]) for x in f]
count = 0
for i in range(0, len(d)):
    if d[i] != -5.0 and d[i]<0:
        count += 1
print((count/len(d)) * 100)
