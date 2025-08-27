import sys
import time
import msvcrt
import shutil
import os

def input_clignotant(prompt="Your message: "):
    RESET = "\033[0m"
    prompt_color = "\033[92m"
    sys.stdout.write(f"{prompt_color}{prompt}{RESET}")
    sys.stdout.flush()
    user_input = []
    blink = True
    last_time = time.time()
    while True:
        if time.time() - last_time > 0.5:
            last_time = time.time()
            cursor = "|" if blink else " "
            blink = not blink
            sys.stdout.write(f"\r{prompt_color}{prompt}{RESET}\033[93m{''.join(user_input)}{RESET}{cursor}")
            sys.stdout.flush()
        if msvcrt.kbhit():
            c = msvcrt.getwch()
            if c in ("\r", "\n"):
                break
            elif c == "\b" and user_input:
                user_input.pop()
            elif c not in ("\x00", "\xe0"):
                user_input.append(c)
        time.sleep(0.01)
    sys.stdout.write(f"\r{prompt_color}{prompt}{RESET}\033[93m{''.join(user_input)}{RESET} \n")
    sys.stdout.flush()
    return ''.join(user_input)

def print_centered(message):
    width = shutil.get_terminal_size().columns
    print(message.center(width))

def print_download_progress(iteration, total, length=50):
    percent = int((iteration / total) * 100)
    filled_length = int(length * iteration // total)
    bar = "\\" * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\rDownloading: \033[91m{bar}\033[0m {percent}%")
    sys.stdout.flush()

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
