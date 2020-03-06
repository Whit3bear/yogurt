def odd_one(arr):
    for idx, item in enumerate(arr):
        if item % 2 != 0:
            return idx
    else:
        return -1
            

