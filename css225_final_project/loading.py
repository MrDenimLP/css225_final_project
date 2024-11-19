###################################################################################################################################
## Author: Michael Nickins                                                                                                       ##
## Last Edited: 10NOV2024                                                                                                        ##
## This file creates a loading bar in the command line to simulate more engaging content when playing games in the CLI/Terminal. ##
###################################################################################################################################



## Imports Python's 'time' and 'sys' modules.
import time
import sys

## Defines a function to manage the creation of the loading bar.
## Takes the following parameters:
## - iteration: The current step or progess.
## - total: The total number of steps.
## - length (optional): The length of the loading bar, with a default value of 50.
def loading_bar(iteration, total, length=50):
    percent = (iteration / total) ## Defines a variable called 'percent' that calculates the current progress as a decimal.
    filled_length = int(length * percent) ## Defines a variable called 'filled_length' that determines how much of the progess bar should be 'filled' with solid characters.
    bar = '█' * filled_length + '-' * (length - filled_length) ## Defines a variable called 'bar' that does the following:
                                                               ## - Part 1: Repeats the solid character "filled_length" times to represent progess.
                                                               ## - Part 2: Fills the remaining space with "-" characters to represent incomplete progress.
                                                               ## Combines the two parts to form the full progress bar and stores it in the 'bar' variable.
    sys.stdout.write(f'\r|{bar}| {percent:.2%}') ## Writes the progress bar to the console in a single line.
    sys.stdout.flush() ## Ensures the output is immediately displayed in the console, even if buffering is enabled.

## Example usage.
if __name__ == "__main__":
    total = 100
    for i in range(total + 1):
        loading_bar(i, total)
        time.sleep(0.1)  ## Simulates some work being done.
    print()  ## Moves to the next line after loading complete.
