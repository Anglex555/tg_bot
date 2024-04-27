import time
import sys
import random
import itertools

def progress_bar():
    for i in range(51):
        sys.stdout.write('\r')
        sys.stdout.write("[%-50s] %d%%" % ('='*i, 2*i))
        sys.stdout.flush()
        time.sleep(0.1)


def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def spinner():
    while True:
        for cursor in '|/-\\':
            sys.stdout.write('\r{}'.format(cursor))
            sys.stdout.flush()
            time.sleep(0.1)

def matrix_code():
    symbols = ['0', '1']
    width, height = 80, 40
    matrix = [[random.choice(symbols) for _ in range(width)] for _ in range(height)]
    while True:
        for row in matrix:
            sys.stdout.write(''.join(row) + '\n')
        matrix = [[random.choice(symbols) if random.random() > 0.1 else char for char in row] for row in matrix]
        time.sleep(0.05)

def digital_clock():
    while True:
        current_time = time.strftime("%H:%M:%S")
        sys.stdout.write('\r{}'.format(current_time))
        sys.stdout.flush()
        time.sleep(1)

import time

# Define the animation frames
frames = [
    """
    ╭────────╮
    │        │
    │  ○     │
    │        │
    ╰────────╯
    """,
    """
    ╭────────╮
    │        │
    │     ○  │
    │        │
    ╰────────╯
    """,
    """
    ╭────────╮
    │        │
    │  ○     │
    │        │
    ╰────────╯
    """,
    """
    ╭────────╮
    │        │
    │  ○     │
    │        │
    ╰────────╯
    """
]

# Define the animation function
def animation():
    while True:
        for frame in frames:
            print(frame)
            time.sleep(0.2)
            print("\033[H\033[J", end="") # clear the console

def bouncing_ball():
    width = 25
    position = 0
    direction = 1
    while True:
        sys.stdout.write('\r')
        sys.stdout.write(' ' * position + 'o' + ' ' * (width - position - 1))
        sys.stdout.flush()
        position += direction
        if position == width - 1 or position == 0:
            direction *= -1
        time.sleep(0.1)

def falling_snowflakes():
    width, height = 80, 40
    snowflakes = []
    while True:
        for i in range(random.randint(1, 4)):
            snowflakes.append([random.randint(0, width), 0])
        for flake in snowflakes:
            sys.stdout.write('\033[{};{}H'.format(flake[1], flake[0]))
            sys.stdout.write('*')
            flake[1] += 1
        snowflakes = [flake for flake in snowflakes if flake[1] < height]
        sys.stdout.flush()
        time.sleep(0.1)

def starry_night():
    width, height = 80, 40
    stars = []
    while True:
        for i in range(random.randint(1, 4)):
            stars.append([random.randint(0, width), random.randint(0, height)])
        for star in stars:
            sys.stdout.write('\033[{};{}H'.format(star[1], star[0]))
            sys.stdout.write('*')
        stars = [[star[0], star[1] + 1] for star in stars if star[1] < height]
        sys.stdout.flush()
        time.sleep(0.1)


def rainbow_spinner():
    while True:
        for c in itertools.cycle(['\033[1;31m|\033[1;m', '\033[1;33m/\033[1;m', '\033[1;32m-\033[1;m', '\033[1;34m\\\033[1;m']):
            sys.stdout.write('\r{}'.format(c))
            sys.stdout.flush()
            time.sleep(0.1)

def matrix_rain():
    width, height = 80, 40
    columns = []
    for i in range(width):
        column = []
        for j in range(random.randint(5, height)):
            column.append(random.choice(['\033[1;32m{}\033[1;m'.format(chr(random.randint(65, 90))), ' ']))
        columns.append(column)
    while True:
        for i in range(width):
            sys.stdout.write('\033[{};{}H'.format(1, i + 1))
            sys.stdout.write('\n'.join(columns[i]))
            for j in range(random.randint(1, 3)):
                columns[i].insert(0, random.choice(['\033[1;32m{}\033[1;m'.format(chr(random.randint(65, 90))), ' ']))
                columns[i].pop()
        sys.stdout.flush()
        time.sleep(0.1)

matrix_rain()
rainbow_spinner()
starry_night()
# Call the animation function
falling_snowflakes()
bouncing_ball()
animation()
# spinner()
typewriter_effect("text so so big text")
progress_bar()
# matrix_code()
digital_clock()