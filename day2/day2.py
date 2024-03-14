import re
import math


with open("day2\day2.txt") as file:
    lines = file.read()


def Part1(lines):
    
    total = 0
    valid = {'red': 12,
            'green': 13,
            'blue': 14
            }
    
    # iterates through file line by line, saving game number in i
    for i, game in enumerate(lines.split("\n"), start=1):
        # iterates through each line comparing number of dice to valid numbers
        for j, color in re.findall('(\d+) (red|green|blue)', game):
            if valid[color] < int(j):
                break
        else:
            # sum of valid game numbers
            total += i
    
    return total

def Part2(lines):

    total = 0

    # iterates through the file by line, saving the game number in i
    for i, game in enumerate(lines.split("\n"), start=1):
        max_number = {'red': 0, 'green': 0, 'blue': 0}
        # iterates through each line finding the max of each color
        for j, color in re.findall('(\d+) (red|green|blue)', game):
            max_number[color] = max(int(j), max_number[color])

        # all max numbers multiplied together per line, and added to a running total
        total += math.prod(max_number.values())
    return total
        
print("Part 1: ", Part1(lines))
print("Part 2: ", Part2(lines))