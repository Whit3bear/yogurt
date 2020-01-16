""" Let us take a string composed of decimal digits: "10111213". We want to code this string as a string of 0 and 1 and after that be able to decode it.

We decompose the given string in its decimal digits 1 0 1 1 1 2 1 3 and we will code each.
Coding process to code a number n expressed in base 10:

a) Let k be the number of bits of n

b) Put k-1 times the digit 0 followed by the digit 1

c) Put number n in binary

d) Concat the result of b) and c)

So we code 0 as 10, 1 as 11 ... etc...

Repeating this process with the initial string

"10111213" becomes : "11101111110110110111" resulting of concatenation of 11 10 11 11 11 0110 11 0111 .
Task:

    Given strng a string of digits representing a decimal number the function code(strng) should return the coding of strng as explained above.

    Given a string strng resulting from the previous coding, decode it to get the corresponding decimal string.

Examples:

code("77338855") --> "001111001111011101110001100000011000001101001101"
code("77338")  --> "0011110011110111011100011000"
code("0011121314") --> "1010111111011011011111001100"

decode("001111001111011101110001100000011000001101001101") -> "77338855"
decode("0011110011110111011100011000") -> "77338"
decode("1010111111011011011111001100") -> "0011121314"

Note

Please could you ask before translating : some translations are already written.
 """
def code(strng):
    return ''.join(f"{(int(x).bit_length() - 1) * '0' + '1'}{int(x):b}" for x in strng)
    
def decode(strng, result = []):
    if not strng:
        ans = ''.join(str(x) for x in result)
        result.clear()        
        return ans 

    start_idx = strng.index('1')
    length = len(strng[:start_idx]) + 1
    result.append(int(strng[start_idx + 1:start_idx + length + 1], 2))
    return decode(strng[start_idx + length + 1:], result)

    

    # result = []
    # length = 0
    # start_idx = 0
    # for i in range(len(strng)):        
    #     if start_idx > len(strng) - 1:
    #         break

    #     if strng[i] == '1' and i >= start_idx:
    #         length = len(strng[start_idx:i])
    #         result.append(int(strng[i+1:i+2+length], 2))
    #         start_idx = i + 3 + length
    # return result




#print(code("62"))
#"0011100110"
#code("55337700")
#"001101001101011101110011110011111010"
#code("1119441933000055")
#"1111110001100100110000110011000110010111011110101010001101001101")
#code("69")
#"00111000011001"
#code("86")
#"00011000001110")

#print(decode('0011100110'))
#"62"
#print(decode("10001111"))
#"07"
print(decode("01110111110001100100011000000110000011110011110111011100110000110001100110"))
#"33198877334422"
