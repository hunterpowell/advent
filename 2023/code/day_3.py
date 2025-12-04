import numpy as np

def Part1():

    schematic = np.genfromtxt('data/day_3.txt', dtype=str, comments='a')

    np.pad(schematic, pad_width=1, mode='constant')

    symbols = {'@', '#', '$', '%', '&', '*', '/', '+', '-', '='}
    height = len(schematic)
    width = 140
    total = 0
    for i in range(height):
        print(schematic[i])

    # for i in range(height):
    #     for j in range(width):
    #         if schematic[i][j].isdigit():
    #             print(schematic[i][j])
                # if (schematic[i-1][j-1] in symbols) | \
                # (schematic[i-1][j] in symbols) | \
                # (schematic[i-1][j+1] in symbols) | \
                # (schematic[i][j-1] in symbols) | \
                # (schematic[i][j+1] in symbols) | \
                # (schematic[i+1][j-1] in symbols) | \
                # (schematic[i+1][j] in symbols) | \
                # (schematic[i+1][j+1] in symbols):
                #     total += int(schematic[i][j])

    print(total)



    
Part1()