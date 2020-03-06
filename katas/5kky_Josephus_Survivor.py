""" In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation.

Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:

josephus_survivor(7,3) => means 7 people in a circle;
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!

The above link about the "base" kata description will give you a more thorough insight about the origin of this kind of permutation, but basically that's all that there is to know to solve this kata.

Notes and tips: using the solution to the other kata to check your function may be helpful, but as much larger numbers will be used, using an array/list to compute the number of the survivor may be too slow; you may assume that both n and k will always be >=1.
 """
def josephus_survivor(n,k):
    seq = [x for x in range(1, n+1)]
    idx = 0
    while len(seq)>1:
        idx = (idx + k - 1) % len(seq)
        seq.pop(idx)        
    return seq[0]

#2 = (0 + 3 - 1) % 7
#4 = (2 + 3 - 1) % 6
#1 = (4 + 3 - 1) % 5
#3 = (1 + 3 - 1) % 4
#2 = (3 + 3 - 1) % 3
#0 = (2 + 3 - 1) % 2
print(josephus_survivor(7,3))
#4
#Test.assert_equals(josephus_survivor(11,19),10)
#Test.assert_equals(josephus_survivor(1,300),1)
#Test.assert_equals(josephus_survivor(14,2),13)
#Test.assert_equals(josephus_survivor(100,1),100)