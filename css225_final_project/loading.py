import time
import sys

def loading_bar(iteration, total, length=50):
    percent = (iteration / total)
    filled_length = int(length * percent)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent:.2%}')
    sys.stdout.flush()

## Example usage.
if __name__ == "__main__":
    total = 100
    for i in range(total + 1):
        loading_bar(i, total)
        time.sleep(0.1)  ## Simulates some work being done.
    print()  ## Moves to the next line after loading complete.
