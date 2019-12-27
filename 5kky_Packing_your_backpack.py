""" You're about to go on a trip around the world! On this trip you're bringing your trusted backpack, that anything fits into. The bad news is that the airline has informed you, that your luggage cannot exceed a certain amount of weight.

To make sure you're bringing your most valuable items on this journey you've decided to give all your items a score that represents how valuable this item is to you. It's your job to pack you bag so that you get the most value out of the items that you decide to bring.

Your input will consist of two arrays, one for the scores and one for the weights. You input will always be valid lists of equal length, so you don't have to worry about verifying your input.

You'll also be given a maximum weight. This is the weight that your backpack cannot exceed.

For instance, given these inputs:

scores = [15, 10, 9, 5]
weights = [1, 5, 3, 4]
capacity = 8

The maximum score will be 29. This number comes from bringing items 1, 3 and 4.

Note: Your solution will have to be efficient as the running time of your algorithm will be put to a test.
 """
def pack_bagpack(scores, weights, capacity):
    n = len(scores)
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(scores[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][capacity]

print(pack_bagpack([15, 10, 9, 5], [1, 5, 3, 4], 8))
#29
#print(pack_bagpack([20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4], 10))
#60
#print(pack_bagpack([13, 11, 8, 16, 3, 13, 14], [2, 2, 1, 4, 3, 2, 3], 13))
#67

#item_weights = [0, 2, 10, 3, 6, 18]
#item_values = [0, 1, 20, 3, 14, 100]
#print(pack_bagpack(item_values, item_weights, 15))