import itertools
import threading
import time
import sys, os

loaded = False

loading_animations = [
    '\u250F\u2513        \n\u2517\u251B        \n\n\n\n',
    '  \u250F\u2513      \n  \u2517\u251B      \n\n\n\n',
    '    \u250F\u2513    \n    \u2517\u251B    \n\n\n\n',
    '      \u250F\u2513  \n      \u2517\u251B  \n\n\n\n',
    '        \u250F\u2513\n        \u2517\u251B\n\n\n\n',
    '\n        \u250F\u2513\n        \u2517\u251B\n\n\n',
    '\n\n        \u250F\u2513\n        \u2517\u251B\n\n',
    '\n\n\n        \u250F\u2513\n        \u2517\u251B\n',
    '\n\n\n\n        \u250F\u2513\n        \u2517\u251B',
    '\n\n\n\n      \u250F\u2513  \n      \u2517\u251B  ',
    '\n\n\n\n    \u250F\u2513    \n    \u2517\u251B    ',
    '\n\n\n\n  \u250F\u2513      \n  \u2517\u251B      ',
    '\n\n\n\n\u250F\u2513        \n\u2517\u251B        ',
    '\n\n\n\u250F\u2513        \n\u2517\u251B        \n',
    '\n\n\u250F\u2513        \n\u2517\u251B        \n\n',
    '\n\u250F\u2513        \n\u2517\u251B        \n\n\n'
]

def loading():
    for c in itertools.cycle(loading_animations):
        if loaded:
            break
        sys.stdout.write(c)
        time.sleep(0.1)
        for i in range(5):
            sys.stdout.write("\033[F")
        sys.stdout.flush()
        os.system('clear')
    print('Loading complete!')

os.system('clear')
t = threading.Thread(target=loading)
sys.stdout.write("\033[?25l")
t.start()
time.sleep(10)
loaded = True
t.join()
sys.stdout.write("\033[?25h")