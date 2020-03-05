""" A series or sequence of numbers is usually the product of a function and can either be infinite or finite.

In this kata we will only consider finite series and you are required to return a code according to the type of sequence:
Code 	Type 	Example
0
	
unordered
	
[3,5,8,1,14,3]
1
	
strictly increasing
	
[3,5,8,9,14,23]
2
	
not decreasing
	
[3,5,8,8,14,14]
3
	
strictly decreasing
	
[14,9,8,5,3,1]
4
	
not increasing
	
[14,14,8,8,5,3]
5
	
constant
	
[8,8,8,8,8,8]

You can expect all the inputs to be non-empty and completely numerical arrays/lists - no need to validate the data; do not go for sloppy code, as rather large inputs might be tested.

Try to achieve a good solution that runs in linear time; also, do it functionally, meaning you need to build a pure function or, in even poorer words, do NOT modify the initial input!
 """

def sequence_classifier(arr):
    incr = False
    decr = False
    dupl = False

    for i in range(1, len(arr)):                
        if arr[i-1]<arr[i]:
            incr = True
        elif arr[i-1]>arr[i]:
            decr = True
        elif arr[i-1] == arr[i]:
            dupl = True

    if incr and decr:
        return 0
    elif incr and not dupl:
        return 1
    elif incr and dupl:
        return 2
    elif decr and not dupl:
        return 3
    elif decr and dupl:
        return 4
    elif dupl and not incr and not decr:
        return 5
        


print(sequence_classifier([3,5,8,1,14,3]))
# 0
# Test.assert_equals(sequence_classifier([3,5,8,9,14,23]),1)
# Test.assert_equals(sequence_classifier([3,5,8,8,14,14]),2)
# Test.assert_equals(sequence_classifier([14,9,8,5,3,1]),3)
# Test.assert_equals(sequence_classifier([14,14,8,8,5,3]),4)
# Test.assert_equals(sequence_classifier([8,8,8,8,8,8]),5)
# Test.assert_equals(sequence_classifier([8,9]),1)
# Test.assert_equals(sequence_classifier([8,8,8,8,8,9]),2)
# Test.assert_equals(sequence_classifier([9,8]),3)
# Test.assert_equals(sequence_classifier([9,9,9,8,8,8]),4)