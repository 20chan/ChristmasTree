import sys
from time import sleep


def sprint(*s):
    sys.stdout.write(''.join(s))
    sys.stdout.flush()


def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()

def tree(start, end, indent = 0, char = '*'):
    print('\n'.join([' ' * (indent + end - i) + char * (2*i-1) for i in range(start, end)]))


if __name__ == '__main__':
    tree(0, 10, indent=5)
    tree(6, 15)
    print('\n'.join([' ' * 9 + '*' * 10] * 5))