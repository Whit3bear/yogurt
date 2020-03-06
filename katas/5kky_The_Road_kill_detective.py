import re
#print('\n'.join(ANIMALS))

def road_kill(photo):
    ANIMALS = ['hyena', 'penguin', 'bear', 'alligator']        
    photo = photo.replace('=','')
    if not photo:
        return '??'            

    for animal in ANIMALS:
        mystr = '^'+'+'.join(char for char in animal) + '+$'
        if re.match(mystr, animal) or re.match(mystr, animal[::-1]):
            return animal               
    return '??'

         
        
 