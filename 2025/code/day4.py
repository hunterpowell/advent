

def day4pt1():
    text = open("2025/data/day4.txt")
    lines = text.read().strip().split('\n')

    lines.insert(0, "." * 136)
    lines.append("." * 136)

    # lines = ["..@@.@@@@.",
    #         "@@@.@.@.@@",
    #         "@@@@@.@.@@",
    #         "@.@@@@..@.",
    #         "@@.@@@@.@@",
    #         ".@@@@@@@.@",
    #         ".@.@.@.@@@",
    #         "@.@@@.@@@@",
    #         ".@@@@@@@@.",
    #         "@.@.@@@.@."]
    
    # lines.insert(0, "." * 10)
    # lines.append("." * 10)

    # love python
    lines = ["." + line + "." for line in lines]
    
    # print(lines)

    rows = len(lines)
    cols = len(lines[0])
    # print(rows, cols)

    valid = 0
    time_since_last = 0
    while time_since_last < (rows-2) * (cols-2):
        # print("bump")
        for i in range(1, rows-1):
            for j in range(1, cols-1):
                if lines[i][j] == '.':
                    continue
                total = 0
                if lines[i-1][j-1] == '@':
                    total += 1
                if lines[i][j-1] == '@':
                    total += 1
                if lines[i+1][j-1] == '@':
                    total += 1
                if lines[i-1][j] == '@':
                    total += 1
                if lines[i+1][j] == '@':
                    total += 1
                if lines[i-1][j+1] == '@':
                    total += 1
                if lines[i][j+1] == '@':
                    total += 1
                if lines[i+1][j+1] == '@':
                    total += 1
                
                if total < 4:
                    valid += 1
                    line_list = list(lines[i])
                    line_list[j] = '.'
                    lines[i] = ''.join(line_list)
                    time_since_last = 0
                    # print(f"removed {i}, {j}")
                time_since_last += 1

    return valid
    # for i in range(1, rows):
    #     for j in range(1, cols):


if __name__ == "__main__":
    print(day4pt1())
