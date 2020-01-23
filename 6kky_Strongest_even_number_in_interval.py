""" A strongness of an even number is the number of times we can successively divide by 2 until we reach an odd number starting with an even number n.

For example, if n = 12, then

12 / 2 = 6

6 / 2 = 3

we divided successively 2 times and we reached 3, so the strongness of 12 is 2.

If n = 16 then

16 / 2 = 8

8 / 2 = 4

4 / 2 = 2

2 / 2 = 1

we divided successively 4 times and we reached 1, so the strongness of 16 is 4
Task

Given a closed interval [n, m], return the even number that is the strongest in the interval. If multiple solutions exist return the smallest strongest even number.

Note that programs must run within the alloted server time; a naive solution will probably time out.
Constraints

1 <= n < m <= INT_MAX
Examples

for the input [1, 2] return 2 (1 has strongness 0, 2 has strongness 1)

for the input [5, 10] return 8 (5, 7, 9 have strongness 0; 6, 10 have strongness 1; 8 has strongness 2)

for the input [48, 56] return 48
 """
def strongest_even(n, m):    
    result = 0
    max_counter = 0    

    for i in range(n, m+1):
        if i % 2:
            continue        
        counter = 0    
        x = i
        while x % 2 == 0:
            x = x // 2
            counter += 1
        if counter > max_counter:
            max_counter = counter
            result = i
    
    return result
        
        
    
    

#print(strongest_even(1, 2))
# 2
#print(strongest_even(5, 10))
# 8
#print(strongest_even(48, 56))
# 48
#print(strongest_even(129, 193))
# 192
print(strongest_even(3, 310))
# 256
print(strongest_even(33, 40))
# 40