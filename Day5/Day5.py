# read input
def read_input():
    with open('input.txt') as input:
        data = input.readlines()
        data = [line.strip() for line in data]

        return data

def part_one(data):
    ids = []

    for board_pass in data:
        #  divive input points
        row = board_pass[:7]
        col = board_pass[7:]

        # get row, col
        row_num = get_row(row)
        col_num = get_col(col)

        # mult row by 8 and add col
        seat_id = (row_num * 8) + col_num

        ids.append(seat_id)
    
    # get highest id
    # return max(ids)

    # part2
    for id in ids:
        if id+1 not in ids and id+2 in ids:
            return id+1

def get_row(row):
    low = 0
    high = 127
    for i in row:
        
        middle = (low + high) // 2

        # low
        if i == 'F':
            high = middle

        # high
        elif i == 'B':
            low = middle + 1

    if row[len(row) - 1] == 'F':
        return low
    else:
        return high
    
def get_col(col):
    low = 0
    high = 7

    for i in col:
        middle = (low + high) // 2

        # low 
        if i == 'L':
            high = middle
        # high 
        elif i == 'R':
            low = middle + 1
    
    if col[len(col) - 1] == 'L':
        return low
    else:
        return high
print(part_one(read_input()))