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
#print(next_smaller(513))
# 351
#print(next_smaller(907))
#790
#print(next_smaller(5311))
#5131
#print(next_smaller(135))
#-1
#print(next_smaller(2071))
#2017
#print(next_smaller(2415))
#2154
#print(next_smaller(415))
#154
#print(next_smaller(123456798))
#123456789
#next_smaller(123456789)
#-1)
#print(next_smaller(1234567908))
#1234567890
