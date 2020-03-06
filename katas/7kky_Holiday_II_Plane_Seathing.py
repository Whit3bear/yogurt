""" Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.

To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters 'I' and 'J' from their seat naming system.

the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter, A-K with the exclusions mentioned above.

Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

Given a seat number, your task is to return the seat location in the following format:

'2B' would return 'Front-Left'.

If the number is over 60, or the letter is not valid, return 'No Seat!!'.
 """
def plane_seat(a):
    num = int(a[:-1])
    l = a[-1]
    res = ''
    if 1 <= num <= 20:
        res +='Front'
    elif 21 <= num <= 40:
        res += 'Middle'
    elif 41 <= num <= 60:
        res += 'Back'
    else:
        return 'No Seat!!'

    if l in 'ABC':
        res += '-Left'
    elif l in 'DEF':
        res += '-Middle'
    elif l in 'GHK':
        res += '-Right'
    else: 
        return 'No Seat!!'

    return res
     

print(plane_seat('2B'))
#'Front-Left'
print(plane_seat('20B'))
#'Front-Left'
print(plane_seat('58I'))
#'No Seat!!'