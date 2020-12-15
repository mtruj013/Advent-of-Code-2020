# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# How many passwords are valid according to their policies?
import csv

# read input
def part_one():
    with open('input.csv') as input:
        reader = csv.reader(input, delimiter=' ')

        count = 0
        # extract needed data
        for line in reader:
            print(line)
            nums, letter, password = line[0], line[1][0], line[2]

            # extract num range
            i = nums.index('-')
            min = int(nums[:i])
            max = int(nums[i+1:])

            # initiate word count
            word_count = password.count(letter)

            # check pw constraints (part 1)
            if word_count >= min and word_count <= max:
                count += 1

        return count


def part_two():
    # read input
    with open('input.csv') as input:
        reader = csv.reader(input, delimiter=' ')
        
        count = 0

        for line in reader:
            # print(line)
            pos_nums, letter, password = line[0], line[1][0], line[2]

            # extract position nums
            i = pos_nums.index('-')
            pos_a = int(pos_nums[:i])
            pos_b = int(pos_nums[i+1:])

            if (password[pos_a - 1] == letter and password[pos_b - 1] != letter) or (password[pos_a - 1] != letter and password[pos_b - 1] == letter):
                count += 1
            
        return count

            

            
print(part_two())
