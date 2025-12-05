

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
        
        num_arr = []
        unsorted_num_arr = []
        new_num_stack = []
        for i in range(len(line)-1):
            num_arr.append(int(line[i]))
            unsorted_num_arr.append(int(line[i]))
        # print(num_arr)
        num_arr.sort(reverse=True)
        # print(num_arr)

        for i in range(12):
            new_num_stack.append(num_arr[i])
        # print(new_num_stack)

        max_num = []
        for digit in reversed(unsorted_num_arr):
            if digit in new_num_stack:
                max_num.append(digit)
                new_num_stack.remove(digit)
        # print(max_num)

        result = 0
        while max_num:
            result *= 10
            result += max_num.pop()
        
        total += result
    return total


# 2444352216545122355224492942447515152244455161432542324549291845752525553324354454533245436254745426 

if __name__ == "__main__":

    text = open("2025/data/day3.txt")
    lines = text.readlines()

    # print(day3pt1(lines))
    print(day3pt2(lines))
