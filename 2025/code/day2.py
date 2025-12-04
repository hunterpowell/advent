
def day2pt1(text):

    pt1 = 0

    # pt 1
    for nums in text:
        nums_range = nums.split('-')
        # print(nums_range)
        lower = int(nums_range[0])
        upper = int(nums_range[1])
        
        for x in range(lower, upper+1):
            num = str(x)
            length = len(num)
            # only check for even length nums, odd ones auto fail
            if length % 2 == 0:
                if num[:length//2] == num[length//2:]:
                    pt1 += x

    return pt1

def day2pt2(text):
    pt2 = set()

    for nums in text:
        nums_range = nums.split('-')
        # print(nums_range)
        lower = int(nums_range[0])
        upper = int(nums_range[1])

        # print(f"lims: {lower}, {upper}")

        for x in range(lower, upper+1):
            
            number = str(x)
            # print(number)j
            """
            every subsequence and div length of num by length of subsequence
            then check if that subsequence * quotient = number
            if so, add to the set of invalid ids
            """
            for i in range(1, len(number)//2+1):
                # print(i, digit)
                length_num = len(number)
                # print(number[:i])
                length_substr = len(number[:i])
                mult = length_num//length_substr
                # print(f"lengths: {length_num, length_substr, mult}")
                if number[:i] * mult == number:
                    # set to avoid duplicates
                    pt2.add(int(number))
                    # print(f"added: {number}")
    # sum all invalid ids
    return sum(pt2)

if __name__ == "__main__":
    text = open("2025/data/day2.txt").read()

    text = text.split(",")

    tmp = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    tmp = tmp.split(",")

    print(f"1: {day2pt1(text)}")
    print(f"2: {day2pt2(text)}")
