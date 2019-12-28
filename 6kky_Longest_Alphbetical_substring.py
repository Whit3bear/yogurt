""" Find the longest substring in alphabetical order.

Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".

There are tests with strings up to 10 000 characters long so your code will need to be efficient.

The input will only consist of lowercase characters and will be at least one letter long.

If there are multiple solutions, return the one that appears first.

Good luck :)
 """

def longest(s):
    if s <= 1:
        return s
    
    arr = []
    prev = 0    
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            arr.append(s[prev:i])
            prev = i
        if i == len(s)-1:
            arr.append(s[prev:])
    
    return max(arr, key=len)
        


#print(longest('asd'))
#'as'
#print(longest('nabc'))
#'ab'
#print(longest('abcdeapbcdef'))
#'abcde'
# Test.assert_equals(longest('asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')
# Test.assert_equals(longest('asdfbyfgiklag'), 'fgikl')
print(longest('z'))
#'z'
# Test.assert_equals(longest('zyba'), 'z')