

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
        
def day3pt2(lines):

    total = 0

    for line in lines:
        result = []
        digits_needed = 12
        for i in range(len(line)):
            digits_remaining = len(line) - i

            while (result and result[-1] < line[i] and len(result) + digits_remaining > digits_needed):
                result.pop()
            
            if len(result) < digits_needed:
                result.append(line[i])
        total += int(''.join(result))

    return total


# 2444352216545122355224492942447515152244455161432542324549291845752525553324354454533245436254745426 

if __name__ == "__main__":

    text = open("2025/data/day3.txt")
    lines = text.read().strip().split('\n')

    # print(day3pt1(lines))
    print(day3pt2(lines))
