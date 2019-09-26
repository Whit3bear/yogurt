def high(x):
    scores = {
        'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
        }
    arr = x.split()
    max_score, score, position = 0, 0, 0

    for idx, item in enumerate(arr):
        for j in item:
            score += scores.get(j)
        if score > max_score:
            position, max_score = idx, score           

        score = 0    
    return arr[position]
    

    
    
print(high('man i need a taxi up to ubud'))
   #'taxi'


