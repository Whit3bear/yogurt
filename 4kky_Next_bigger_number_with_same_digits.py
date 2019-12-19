""" You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

12 ==> 21
513 ==> 531
2017 ==> 2071

If no bigger number can be composed using those digits, return -1:

9 ==> -1
111 ==> -1
531 ==> -1

 """

def next_bigger(n):
    arr = [x for x in str(n)]
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > arr[i-1]:
            break
    else:
        return -1

    # дойти до замены, потом отсортировать срез по возрастанию
    # swap = i
    # for j in range(i, len(arr)):                   
    #     if arr[j] > arr[i-1] and arr[j] > arr[i]:
    #         swap = j 

    arr[i-1], arr[i] = arr[i], arr[i-1]
    
    newlst = arr[:i] + sorted(arr[i:])

    return newlst
        # if arr[j]
            
        #     arr[i], arr[i-1] = arr[i-1], arr[i]
        #     return int(''.join(arr))       
    
print(next_bigger(698488273))
# 698488327
#print(next_bigger(12))
# 21
#print(next_bigger(513))
# 531
#print(next_bigger(2017))
# 2071
#print(next_bigger(9876543210))
# -1
#print(next_bigger(1234567890))
# 1234567908
# Test.assert_equals(next_bigger(414),441)
# Test.assert_equals(next_bigger(144),414)