""" Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
 """
def snail(snail_map):
    l = len(snail_map)
    if l <= 1:
        return snail_map[-1]
    result = []

    Right = True
    Left = False    
    Up = False
    Down = False

    r_idx = 0
    d_idx = l
    l_idx = l
    u_idx = 0

    while True:        
        if Right:
            for i in range(r_idx, d_idx):
                result.append(snail_map[r_idx][i])
            r_idx += 1
            Right = False
            Down = True
        elif Down:                               
            for i in range(r_idx, d_idx):
                result.append(snail_map[i][d_idx-1])
            d_idx -= 1            
            Down = False
            Left = True
        elif Left:
            for i in range(d_idx-1, u_idx-1, -1):
                result.append(snail_map[d_idx][i])
            l_idx -= 1
            Left = False
            Up = True
        elif Up:
            for i in range(l_idx-1, u_idx, -1):
                result.append(snail_map[i][u_idx])
            u_idx += 1
            Up = False
            Right = True

        if r_idx == l_idx or u_idx == d_idx:
            return result                  
        

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
#expected = [1,2,3,6,9,8,7,4,5]
print(snail(array))
#expected

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# expected = [1,2,3,4,5,6,7,8,9]
# test.assert_equals(snail(array), expected)