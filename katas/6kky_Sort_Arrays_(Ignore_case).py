def sortme(words):    
    arr = sorted(x.lower() for x in words)
    res = []
    for i in arr:
        for j in words:
            if j.lower() == i:
                res.append(j)

    return res

print(sortme(["Hello", "there", "I'm", "fine"]))
# ["fine", "Hello", "I'm", "there"]
#Test.assert_equals(sortme(["C", "d", "a", "B"]), ["a", "B", "C", "d"])
#Test.assert_equals(sortme(["CodeWars"]), ["CodeWars"])