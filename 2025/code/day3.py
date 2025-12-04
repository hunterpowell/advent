

def day3pt1(lines):

    total = 0

    for line in lines:
        max = 0
        for i, digit in enumerate(line):
            for j in range(i+1, len(line)):
                if int(line[i] + line[j]) > max:
                    max = int(line[i] + line[j])
                    print(f"new max: {max}")
        total += max

    return total
        


if __name__ == "__main__":

    text = open("2025/data/day3.txt")
    lines = text.readlines()

    print(day3pt1(lines))
