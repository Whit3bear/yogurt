""" pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ] """

def pyramid(n):
    result = []
    
    for i in range(n):
        result.append([1])
        for j in range(i):
            result[i].append(1)              

    return result

