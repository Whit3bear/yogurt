""" For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty

Have fun coding it and please don't forget to vote and rank this kata! :-)
 """
from itertools import zip_longest
def decrypt(encrypted_text, n):    
    counter = 0
    result = encrypted_text    
    while n > counter:
        c_evens = result[len(result)//2:]
        c_odds = result[:len(result)//2]
        
        result = ''.join(x+y for x, y in zip_longest(c_evens, c_odds, fillvalue=''))
        counter += 1
    return result

def encrypt(text, n):
    counter = 0
    result = text
    while n > counter:
        c_evens = ''
        c_odds = ''
        for x in range(len(result)):
            if x % 2:
                c_odds += result[x]                
            else:
                c_evens += result[x]
        result = c_odds + c_evens
        counter += 1
    return result

#print(encrypt("This is a test!", 0))
#"This is a test!"
#print(encrypt("This is a test!", 1))
#"hsi  etTi sats!"
#print(encrypt("This is a test!", 2))
#"s eT ashi tist!"
#print(encrypt("This is a test!", 3)) 
#" Tah itse sits!"
#print(encrypt("This is a test!", 4))
#"This is a test!"
#print(encrypt("This is a test!", -1))
#"This is a test!"
#print(encrypt("This kata is very interesting!", 1))
#"hskt svr neetn!Ti aai eyitrsig"

#print(decrypt("This is a test!", 0))
#"This is a test!"
#print(decrypt("hsi  etTi sats!", 1))
#"This is a test!"
print(decrypt("s eT ashi tist!", 2))
#"This is a test!"
#print(decrypt(" Tah itse sits!", 3))
#"This is a test!"
#print(decrypt("This is a test!", 4))
#"This is a test!"
#print(decrypt("This is a test!", -1))
#"This is a test!"
#print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))
#"This kata is very interesting!")

#print(encrypt("", 0))
#""
#print(decrypt("", 0)
#""
#print(encrypt(None, 0))
#None
#print(decrypt(None, 0))
#None