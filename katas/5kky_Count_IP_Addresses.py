def ips_between(start, end):
    start_arr = start.split('.')    
    end_arr = end.split('.')
    res = 0
    m = 1
    for i in range(3, -1, -1):        
        res += (int(end_arr[i]) - int(start_arr[i])) * m
        m *= 256                
        
    return res

#print(ips_between("10.0.0.0", "10.0.0.50"))
# 50
# print(ips_between("10.0.0.0", "10.0.1.0"))
# 256 
print(ips_between("20.0.0.10", "20.0.1.0"))
# 246