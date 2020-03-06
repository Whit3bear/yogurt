""" Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.
Examples

"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  "" """

def clean_string(s):    
    arr = [x for x in s]
    res = []
    for i in arr:        
        if i == '#':
            if res:
                res.pop()
            else:
                continue
        else:
            res.append(i)                
    return ''.join(res)

print(clean_string('abc#d##c'))
#"ac"
print(clean_string('abc####d##c#'))
#"" 
print(clean_string("#######"))
#"" 
print(clean_string(""))
#"" 