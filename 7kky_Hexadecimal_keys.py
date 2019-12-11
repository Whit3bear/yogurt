""" Hector the hacker has stolen some information, but it is encrypted. In order to decrypt it, he needs to write a function that will generate a decryption key from the encryption key which he stole (it is in hexadecimal). To do this, he has to determine the two prime factors P, and Q of the encyption key, and return the product (P - 1)x(Q - 1).

For example if the encryption key is "47b", it is 1147 in base ten. this factors to 31x37, so the key Hector needs is 1080 (30x36).
"""
def find_key(encryption_key):    
    base = int(encryption_key, 16)        
    for x in range(2, base):
        if base % x == 0:
            return (base // x - 1)*(x - 1)
    
        

print(find_key("2533"))
# 9328
print(find_key("1ba9"))
# 6912


