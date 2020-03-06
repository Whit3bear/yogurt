def div_con(x):
    res = 0
    for c in x:
        if isinstance(c, int):
            res += c 
        else:
            res -= int(c)
    return res

# test.assert_equals(div_con([9, 3, '7', '3']), 2)
# test.assert_equals(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 14)
# test.assert_equals(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 13) 
# test.assert_equals(div_con(['1', '5', '8', 8, 9, 9, 2, '3']), 11)
# test.assert_equals(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61) 