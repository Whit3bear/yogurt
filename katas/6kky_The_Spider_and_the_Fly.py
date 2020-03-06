from math import sqrt, cos, radians
def spider_to_fly(spider, fly):    
    coordinates = {'A': 0, 'B': 45, 'C': 90, 'D': 135, 'E': 180, 'F': 225, 'G': 270, 'H': 315}
    angle = coordinates[spider[0]] - coordinates[fly[0]]     
    s, f = int(spider[1]), int(fly[1])
    return sqrt(s**2 + f**2 - 2*s*f*cos(radians(angle)))
 