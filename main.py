import sys
import os
from time import sleep
from random import randint

height, width = os.popen('stty size', 'r').read().split()
width, height = int(width), int(height)


tree = '''
             /\\
            <  >
             \/
             /\\
            /  \\
           /++++\\
          /  ()  \\
          /      \\
         /~`~`~`~`\\
        /  ()  ()  \\
        /          \\
       /*&*&*&*&*&*&\\
      /  ()  ()  ()  \\
      /              \\
     /++++++++++++++++\\
    /  ()  ()  ()  ()  \\
    /                  \\
   /~`~`~`~`~`~`~`~`~`~`\\
  /  ()  ()  ()  ()  ()  \\
  /*&*&*&*&*&*&*&*&*&*&*&\\
 /                        \\
/,.,.,.,.,.,.,.,.,.,.,.,.,.\\
           |   |
          |`````|
          \_____/
'''
tree = '\n'.join([' ' * (width //2 - 20) + s for s in tree.split('\n')])

def print_there(y, x, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()


def randchr():
    i = randint(0, 100)
    if i < 50:
        return '*'
    elif i < 70:
        return '@'
    elif i < 80:
        return '☆'
    elif i > 85:
        return '❄'
    else:
        return '❅'


snows = []
count = 40
for _ in range(count):
    snows.append((randint(1, width - 1), randint(1, height - 2), randchr()))


def snowoverlay():
    for i in range(count):
        snows[i] = snows[i][0], snows[i][1] + 1, snows[i][2]
        if snows[i][1] == height + 3:
            snows[i] = randint(0, width - 1), 1, snows[i][2]
        print_there(*snows[i])

if __name__ == '__main__':
    while True:
        os.system('clear')
        print(tree)
        snowoverlay()
        sleep(1)
