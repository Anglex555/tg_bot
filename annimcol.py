import colorama
import random
import time
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
# Initialize colorama
colorama.init()

# Animation 1: Rainbow text
def rainbow_text(text):
    colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN,
              colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN]
    while True:
        colored_text = ''
        for char in text:
            colored_text += random.choice(colors) + char
        print(colored_text)
        time.sleep(0.1)

# Animation 2: Color fade
def color_fade():
    colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN,
              colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN]
    color_idx = 0
    while True:
        print(colors[color_idx % len(colors)] + 'Hello, world!')
        color_idx += 1
        time.sleep(0.1)

# Animation 3: Color wheel
def color_wheel():
    colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN,
              colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN]
    color_idx = 0
    while True:
        print(colors[color_idx % len(colors)] + 'Hello, world!')
        color_idx += 1
        time.sleep(0.1)

# Animation 4: Blinking text
def blinking_text(text):
    while True:
        print(colorama.Style.BRIGHT + colorama.Fore.RED + text)
        time.sleep(0.5)
        print(colorama.Style.NORMAL + colorama.Fore.WHITE + text)
        time.sleep(0.5)

# Animation 5: Matrix rain
def matrix_rain():
    while True:
        columns = [chr(random.randint(0, 126)) for i in range(100)]
        print(''.join([random.choice([colorama.Fore.GREEN, colorama.Fore.MAGENTA]) + c for c in columns]))
        time.sleep(0.05)

# Animation 6: Fire
def fire():
    palette = [colorama.Fore.BLACK, colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.WHITE]
    while True:
        pixels = [random.choice(palette) + '░' for i in range(100)]
        for i in range(0, len(pixels), 10):
            row = pixels[i:i+10]
            print(''.join(row))
        time.sleep(0.05)

# Animation 7: Starfield
def starfield():
    while True:
        stars = ['.' for i in range(100)]
        for i in range(10):
            idx = random.randint(0, 99)
            stars[idx] = '*'
        print(''.join(stars))
        time.sleep(0.1)

# Animation 8: Colorful circles
def colorful_circles():
    while True:
        colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN,
                  colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN]
        for i in range(6):
            circle = ' ' * i + 'O' * (6-i)
            print(colors[i] + circle)
        time.sleep(0.2)



def rainbow_animation():
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    while True:
        for color in colors:
            print(color + "Rainbow")
            time.sleep(0.2)

# Animation 2: Bouncing ball
def bouncing_ball_animation():
    ball_char = "O"
    screen_width = 80
    ball_pos = 0
    ball_dir = 1
    while True:
        ball_pos += ball_dir
        if ball_pos == screen_width-1:
            ball_dir = -1
        elif ball_pos == 0:
            ball_dir = 1
        print(" "*ball_pos + ball_char)
        time.sleep(0.1)

# Animation 3: Colorful text
def colorful_text_animation():
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    text = "Colorful text"
    while True:
        for color in colors:
            print(color + text)
            time.sleep(0.2)

# Animation 4: Blinking text
def blinking_text_animation():
    text = "Blinking text"
    while True:
        print(Fore.RED + Back.WHITE + Style.BRIGHT + text, end="\r")
        time.sleep(0.5)
        print(" "*len(text), end="\r")
        time.sleep(0.5)

# Animation 5: Colorful bouncing ball
def colorful_bouncing_ball_animation():
    ball_char = "O"
    screen_width = 80
    ball_pos = 0
    ball_dir = 1
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    while True:
        ball_pos += ball_dir
        if ball_pos == screen_width-1:
            ball_dir = -1
        elif ball_pos == 0:
            ball_dir = 1
        color = colors[ball_pos % len(colors)]
        print(color + " "*ball_pos + ball_char)
        time.sleep(0.1)

# Animation 6: Rainbow bouncing ball
def rainbow_bouncing_ball_animation():
    ball_char = "O"
    screen_width = 80
    ball_pos = 0
    ball_dir = 1
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    while True:
        ball_pos += ball_dir
        if ball_pos == screen_width-1:
            ball_dir = -1
        elif ball_pos == 0:
            ball_dir = 1
        color = colors[ball_pos % len(colors)]
        print(color + " "*ball_pos + ball_char)
        time.sleep(0.1)

# Animation 7: Gradient background
def gradient_background_animation():
    colors = [Back.RED, Back.YELLOW, Back.GREEN, Back.BLUE, Back.MAGENTA, Back.CYAN]
    while True:
        for i in range(len(colors)):
            print(colors[i] + " "*80)
            time.sleep(0.2)


#rainbow_text("text liaj dhao ajfp")
#color_fade()
#colorful_circles()
#starfield()
#fire()
#matrix_rain()
#blinking_text("text sadfas sadsad sadsaf af safef eg ew")
#color_wheel()
#rainbow_animation()
#bouncing_ball_animation()
#colorful_text_animation()
#blinking_text_animation()
#colorful_bouncing_ball_animation()
#rainbow_bouncing_ball_animation()
#gradient_background_animation()
matrix_rain()