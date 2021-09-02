import os
import sys
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge, nlargest, nsmallest
from custom_modules.StatusMessenger import custom

LINE = "\n" + custom("__________________________________________________________________________________") + "\n"
DASH = "\n" + custom("----------------------------------------------------------------------------------") + "\n"
BRK = "\n"
TAB = "\t"


# Generate password
def generate_password(to_file=False):
    #  -E +\<\>\;:\|\\\^\'\",\.\={}*\-[]\`\~\)\(\/
    if to_file:
        os.system(
            'apg -a 1 -M Sncl -m 19 -n 1 -E \<+\\\'\>\;.:~\(\)\[\]\{^=-*\|\},\\"\\?\!\`\\/ > generated-password.txt')
    else:
        os.system(
            'apg -a 1 -M Sncl -m 19 -n 1 -E \<+\\\'\>\;.:~\(\)\[\]\{^=-*\|\},\\"\\?\!\`\\/')


# Clear the console


def cls(): os.system('clear')


# Strip all but first argument


def strip_args():
    ARGS = sys.argv
    ARGS_COUNT = len(ARGS)
    if ARGS_COUNT > 1:
        return True, ARGS[1:], len(ARGS[1:])
    else:
        return False, None, 0


# Function for nth Fibonacci number


def fibonacci(n):

    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)
