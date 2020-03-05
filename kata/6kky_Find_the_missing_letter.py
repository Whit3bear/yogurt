def find_missing_letter(chars):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    

    for i in letters[letters.index(chars[0]):letters.index(chars[0]) + len(chars)]:
        if i not in chars:
            return i
    
