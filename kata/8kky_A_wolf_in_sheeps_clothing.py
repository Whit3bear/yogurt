def warn_the_sheep(queue):        
    r = queue[::-1]   
    for idx in range(len(r)):
        if idx == 0 and r[0] == 'wolf':
            return 'Pls go away and stop eating my sheep'
        elif r[idx] == 'wolf':
            return "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(idx)
           
            
            
print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))
# 'Oi! Sheep number 2! You are about to be eaten by a wolf!')