""" Example

Run simulation for 10 time units

Input

    road = "C...R............G......"
    n = 10

Result

[
  "C...R............G......", // 0 initial state as passed
  ".C..R............G......", // 1
  "..C.R............G......", // 2
  "...CR............G......", // 3
  "...CR............G......", // 4
  "....C............O......", // 5 show the car, not the light
  "....GC...........R......", // 6
  "....G.C..........R......", // 7
  "....G..C.........R......", // 8
  "....G...C........R......", // 9
  "....O....C.......R......"  // 10
] """

def traffic_lights(road, n):
    result = []
    car = 0    
    newlst = list(road) 
    replace_G = False
    result.append(''.join(newlst))

    countdown = 0    
    for i in range(1, n+1):          

        countdown = i % 11
        for idx, color in enumerate(newlst):                       
            if countdown == 0 and color == 'O':
                newlst[idx] = 'R' 
            elif countdown == 0 and color == 'R':                         
                newlst[idx] = 'G'
            elif countdown == 5 and color == 'R':
                newlst[idx] = 'G'                
            elif countdown == 5 and color == 'G':
                newlst[idx] = 'O'  
            elif countdown == 6 and color == 'O':                         
                newlst[idx] = 'R'
            elif countdown == 10 and color == 'G':
                newlst[idx] = 'O'

        if car > (len(newlst) - 1):            
            result.append(''.join(newlst))
            continue
        elif car == (len(newlst) - 1):
            newlst[car] = '.'
            result.append(''.join(newlst))
            continue               
        
        if newlst[car+1] == 'R':            
            result.append(''.join(newlst))
            continue
        elif replace_G:
            newlst[car], newlst[car+1] = 'G', newlst[car]             
            result.append(''.join(newlst))
            replace_G = False        
        elif newlst[car+1] == 'G':
            newlst[car], newlst[car+1] = '.', newlst[car]             
            result.append(''.join(newlst))
            replace_G = True                        
        else:             
            newlst[car], newlst[car+1] = newlst[car+1], newlst[car]
            result.append(''.join(newlst))
        car += 1                                        
       
    return result

print(traffic_lights('C...R............G......', 35))
