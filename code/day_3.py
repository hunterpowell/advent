import re

def Part1():

    with open("data\day_3.txt") as file:
        infile = file.read()

    for i, lines in enumerate(infile.split("\n")):
        # print(lines)
        for j in lines:
            print(j)


    
Part1()