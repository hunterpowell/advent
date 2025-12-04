
def day1():
    text = open("2025/data/day1.txt")
    lines = text.readlines()

    nums = []

    # test case
    tmp = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

    for i, word in enumerate(lines):
        if word[0] == 'R':
            nums.append(int(word[1:-1]))
        else:
            nums.append(-1 * (int(word[1:-1])))

    total = 50
    zeroes = 0

    for x in nums:

        if x > 0:
            if total != 0:
                dist_to_zero = (100 - total)  
            else:
                dist_to_zero = 100
            if x >= dist_to_zero:
                zeroes += 1 + (x - dist_to_zero) // 100
        else:
            if total != 0:
                dist_to_zero = total  
            else:
                dist_to_zero = 100
                
            if abs(x) >= dist_to_zero:
                zeroes += 1 + (abs(x) - dist_to_zero) // 100
        
        total = (total + x) % 100

        # total += x
        # if total > 99 or total < 0:
        #     zeroes += 1
        # total %= 100

        # if total == 0:
        #     zeroes += 1
        # print(total)

    return zeroes

print(day1())
