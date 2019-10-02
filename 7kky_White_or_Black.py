# Complete the function that returns the color of the given square on a normal, 8x8 chess board:

def square_color(file, rank):
    if (ord(file) + rank) % 2 == 0:
        return 'black'
    return 'white'

