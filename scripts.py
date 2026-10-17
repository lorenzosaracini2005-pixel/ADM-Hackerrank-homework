# ==============================================================================
# ALGORITHMIC METHODS OF DATA MINING - HOMEWORK 1
# Student: Lorenzo Saracini
# ==============================================================================


# ==============================================================================
# PROBLEM 1: HACKERRANK PYTHON
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Strings: Merge the Tools!
# ------------------------------------------------------------------------------
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        blocco = string[i:i + k]
        risultato = "".join(dict.fromkeys(blocco))
        print(risultato)

if __name__ == '__main__':
    # string, k = input(), int(input())
    # merge_the_tools(string, k)
    pass


# ------------------------------------------------------------------------------
# 2. Sets: The Captain's Room
# ------------------------------------------------------------------------------
def solve_captains_room():
    k = int(input())
    rooms = list(map(int, input().split()))
    unique_rooms = set(rooms)
    captains_room = (k * sum(unique_rooms) - sum(rooms)) // (k - 1)
    print(captains_room)


# ------------------------------------------------------------------------------
# 3. Collections: Company Logo
# ------------------------------------------------------------------------------
from collections import Counter

def solve_company_logo():
    s = input()
    counts = Counter(s)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for char, count in sorted_items[:3]:
        print(char, count)


# ------------------------------------------------------------------------------
# 4. Date and Time: Time Delta
# ------------------------------------------------------------------------------
from datetime import datetime

def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, time_format)
    dt2 = datetime.strptime(t2, time_format)
    diff_seconds = abs(int((dt1 - dt2).total_seconds()))
    return str(diff_seconds)


# ------------------------------------------------------------------------------
# 5. Built-ins: ginortS
# ------------------------------------------------------------------------------
def solve_ginorts():
    s = input()

    def sort_key(c):
        if c.islower():
            return (1, c)
        elif c.isupper():
            return (2, c)
        elif c.isdigit() and int(c) % 2 != 0:
            return (3, c)
        else:
            return (4, c)

    print("".join(sorted(s, key=sort_key)))


# ------------------------------------------------------------------------------
# 6. Functional Programming: Map and Lambda Function
# ------------------------------------------------------------------------------
cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


# ------------------------------------------------------------------------------
# 7. Regex and Parsing: Re.findall() & Re.finditer()
# ------------------------------------------------------------------------------
import re

def solve_regex_findall():
    vowels = "aeiouAEIOU"
    consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
    pattern = rf"(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])"
    matches = re.findall(pattern, input())

    if matches:
        for m in matches:
            print(m)
    else: 
        print(-1)


# ------------------------------------------------------------------------------
# 8. Closures and Decorators: Standardize Mobile Number Using Decorators
# ------------------------------------------------------------------------------
def wrapper(f):
    def fun(l):
        f([f"+91 {c[-10:-5]} {c[-5:]}" for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


# ==============================================================================
# PROBLEM 2: HACKERRANK ALGORITHMS
# ==============================================================================

# ------------------------------------------------------------------------------
# 9. Recursion: Recursive Digit Sum
# ------------------------------------------------------------------------------
def superDigit(n, k):
    total = sum(int(c) for c in n) * k
    return 9 if total % 9 == 0 else total % 9


# ------------------------------------------------------------------------------
# 10. Sorting: Insertion Sort - Part 1
# ------------------------------------------------------------------------------
def insertionSort1(n, arr):
    target = arr[-1]
    i = n - 2
    
    while i >= 0 and arr[i] > target:
        arr[i + 1] = arr[i]
        print(*(arr))
        i -= 1
        
    arr[i + 1] = target
    print(*(arr))


# ==============================================================================
# NOTE ON SUBMISSION SCOPE
# ==============================================================================
"""
Please note: Due to time constraints regarding manual export and code formatting, 
a representative selection of 10 completed problems (covering the various core 
sections of Problem 1 and Problem 2) has been aggregated in this script.

All of the remaining assigned challenges (~70 exercises) have been successfully 
solved and passed with 'Accepted' status. Their completion is fully documented 
and certified via the submission printouts available in the 'printouts/' folder 
of this repository. If required, I am readily available to provide the full 
source code or demonstrate live access directly through my HackerRank profile.
"""
