import math

def part_one(down, right):
    # read input 
    with open('input.txt') as input:
        map = input.readlines()
        # format
        map = [line.strip() for line in map]

     
        length = len(map)
        tree = "#"
        slope = right
        count = 0
        down_count = down
  

        while down < length:
            space = map[down][right % len(map[down])]
            if space == tree:
                count += 1
                right += slope
            else:
                right += slope
            down+=down_count
        return count

def part_two():
    nums = []
    # # r1, d1
    nums.append(part_one(1,1)) 
    # r3, d1
    nums.append(part_one(1,3))
    # # r5, d1
    nums.append(part_one(1,5))
    # # r7, d1
    nums.append(part_one(1,7))
    # # r1, d2
    nums.append(part_one(2,1))
    return math.prod(nums)
print(part_two())