def next_smaller(n):
    # идем циклом по числу с конца, ищем цифру которая больше предыдущей, если не находим, возвращаем -1
    # если находим, то делаем выход из цикла в i содержится индекс элемента с которого нужно делать перестановку 
    lst = [int(x) for x in str(n)]
    for i in range(len(lst)-1, 0, -1):      
        if lst[i-1] > lst[i]:                        
            break
    # ничего не найдено
    else:        
        return -1

    smallest = i    
    # в правой части списка, сравним элементы и найдем наименьший элемент, поменяем значением
    for j in range(i, len(lst)):        
        if lst[j] < lst[i-1] and lst[j] < lst[i]:
            smallest = j
    
    lst[smallest], lst[i-1] = lst[i-1], lst[smallest]

    #сортируем
    newlst = lst[:smallest] + sorted(lst[smallest:], reverse=True)
    return newlst   

    # 24135 свапаем 4 и 1, 21435 находим наименьший номер, с которым меняемся значением, далее сортируем после 4 последние две цифры по убыванию, 21453
    # 24325


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
print(next_smaller(1234567908))
#1234567890
