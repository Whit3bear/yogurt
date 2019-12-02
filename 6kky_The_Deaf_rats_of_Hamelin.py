""" Story

The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!
Kata Task

How many deaf rats are there?
Legend

    P = The Pied Piper
    O~ = Rat going left
    ~O = Rat going right

Example

    ex1 ~O~O~O~O P has 0 deaf rats

    ex2 P O~ O~ ~O O~ has 1 deaf rat

    ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats """

def count_deaf_rats(town):    
    rats = 0
    town = town.replace(' ', '')    
    s1, s2 = town.split('P')    
    
    for i in range(0, len(s1)-1, 2):
        if s1[i] == 'O' and s1[i+1] == '~':
            rats += 1
    for i in range(0, len(s2)-1, 2):
        if s2[i] == '~' and s2[i+1] == 'O':
            rats += 1

    return rats 


print(count_deaf_rats("~O~O~O~O P"))
#0  
print(count_deaf_rats("P O~ O~ ~O O~"))
#1 
print(count_deaf_rats("~O~O~O~OP~O~OO~"))
#2
