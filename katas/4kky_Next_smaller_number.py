def next_smaller(n):  
    lst = [int(x) for x in str(n)]    
    for i in range(len(lst)-1, 0, -1):                            
        if lst[i-1] > lst[i]:                        
            break            
    else:        
        return -1

    swap = i        
    for j in range(i, len(lst)):        
        if lst[j] < lst[i-1] and lst[j] > lst[i]:        
            swap = j
        
    lst[swap], lst[i-1] = lst[i-1], lst[swap]           
    
    newlst = lst[:i] + sorted(lst[i:], reverse=True)
    
    if newlst[0] == 0:
        return -1
    
    return int(''.join([str(x) for x in newlst]))

#print(next_smaller(1207))
# 1072
print(next_smaller(1027))
# -1
