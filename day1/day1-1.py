# the goal here is to read all the data from day1.txt and replace the spelled out numbers with digits
# then take the first and last digit of each string to create a two digit number
# and finally sum them all

# open file
input = open("day1\day1.txt")
lines = input.readlines()

# valid nums, weird format to account for overlapping strings. i.e eightwo 
valid_num = {"one":"o1e",
             "two":"t2o",
             "three":"t3e",
             "four":"f4r",
             "five":"f5e",
             "six":"s6x",
             "seven":"s7n",
             "eight":"e8t",
             "nine":"n9e",
             }

# yeah
sum = 0
new_lines = []

#populates new_lines with our updated list
for line in lines:
    for i in valid_num:
        if i in line:
            line = line.replace(i, valid_num[i])
    new_lines.append(line)

# main loop
for i in new_lines:
    # finds first number
    for j in range(len(i)):
        if i[j].isdigit():
            tmp1 = int(i[j])
            break
    # finds last
    for k in range(len(i)-1, -1, -1):
        if i[k].isdigit():
            tmp2 = int(i[k])
            break
    # first number in 10s place
    tmp1 *= 10
    sum += (tmp1 + tmp2)

print("sum = ", sum)

input.close()