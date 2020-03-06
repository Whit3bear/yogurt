def solve(s):
    vowels = 'aeoui'
    count = 0
    max_count = 0
    for char in s:
        if char in vowels:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

    return max_count       

print(solve("codewarriors"))
# 2