def minimumBribes(q):
    res = 0
    while True:
        for i, (x, y) in enumerate(zip(q, q[1:]), 1):
            if (x - y) > 2:
                return "Too chaotic"  
            if x > y:
                res += 1
                q[i], q[i-1] = q[i-1], q[i]
                break
        else:
            return res            
    
    return res

#print(minimumBribes([2, 1, 5, 3, 4]))
#3
print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))
7
#print(minimumBribes([2, 5, 1, 3, 4]))
#"Too chaotic"