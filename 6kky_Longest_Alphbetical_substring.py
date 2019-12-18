def longest(s):
    m = s[0]
    res = ''
    for i in range(1, len(s)):        
        if s[i] < s[i-1]:
            if len(m) > len(res):
                res = m
                m = ''
        m += s[i]
    if len(m) > len(res):
        res = m
    return res

#print(longest('asd'))
#'as'
print(longest('nab'))
#'ab'
# Test.assert_equals(longest('abcdeapbcdef'), 'abcde')
# Test.assert_equals(longest('asdfaaaabbbbcttavvfffffdf'), 'aaaabbbbctt')
# Test.assert_equals(longest('asdfbyfgiklag'), 'fgikl')
# Test.assert_equals(longest('z'), 'z')
# Test.assert_equals(longest('zyba'), 'z')