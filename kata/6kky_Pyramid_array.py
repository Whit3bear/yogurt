""" pyramid(0) => [ ]
pyramid(1) => [ [1] ]
pyramid(2) => [ [1], [1, 1] ]
pyramid(3) => [ [1], [1, 1], [1, 1, 1] ] """

def pyramid(n):
    return [[1]*x for x in range(1, n+1)]

