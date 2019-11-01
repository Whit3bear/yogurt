def knight(p1, p2):
    currentpos_x = p1[0]
    currentpos_y = p1[1]

    counter = 0

    if p1 == p2:
        return counter
    else:
        counter += 1   
           
    nextposition_x = ord(currentpos_x) + 1
    nextposition_y = int(currentpos_y) + 2

    if 96 < nextposition_x < 103 and 0 < nextposition_y < 9:
        return knight(chr(nextposition_x) + str(nextposition_y), p2)

    nextposition_x = ord(currentpos_x) + 2
    nextposition_y = int(currentpos_y) + 1

    if 96 < nextposition_x < 103 and 0 < nextposition_y < 9:
        return knight(chr(nextposition_x) + str(nextposition_y), p2)

    nextposition_x = ord(currentpos_x) - 1
    nextposition_y = int(currentpos_y) - 2

    if 96 < nextposition_x < 103 and 0 < nextposition_y < 9:
        return knight(chr(nextposition_x) + str(nextposition_y), p2)

    nextposition_x = ord(currentpos_x) - 2
    nextposition_y = int(currentpos_y) - 1

    if 96 < nextposition_x < 103 and 0 < nextposition_y < 9:
        return knight(chr(nextposition_x) + str(nextposition_y), p2)   
    

#arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
print(knight('a1','b1'))