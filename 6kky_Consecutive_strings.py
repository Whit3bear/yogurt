def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''    
    res = ''
    s = ''
    for x in range(n - k + 1):
        res = ''.join(strarr[x:x+k])
        if len(res) > max_len:
            max_len = len(res)
            ans = res
    return ans

#print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
#"abigailtheta")
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
#"oocccffuucccjjjkkkjyyyeehh"
# testing(longest_consec([], 3), "")
# testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
# testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
# testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")