def next_smaller(n):  
    
    lst = [int(x) for x in str(n)]
    for i in range(len(lst)-1, 0, -1):     
        
        if lst[i-1] > lst[i]:                        
            break
    # ничего не найдено это минимальное число
    else:        
        return -1

    swap = i    
    # цикл по срезу правой части списка, ищем элемент который меньше числа не по порядку, но больше числа идущего за ним в списке   
    for j in range(i, len(lst)):        
        if lst[j] < lst[i-1] and lst[j] > lst[i]:        
            swap = j
    
    # выполняем замену
    lst[swap], lst[i-1] = lst[i-1], lst[swap]

    #сортируем
    newlst = lst[:i] + sorted(lst[i:], reverse=True)
    return newlst

    # 24135 свапаем 4 и 1, 21435 находим наименьший номер, с которым меняемся значением, далее сортируем после 4 последние две цифры по убыванию, 21453
    # 24325

# ноль нужно игнорировать, брать предыдущее значение
print(next_smaller(1027))
# -1
# должно быть меньше 5 [i-1] но больше 1 [i]
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
