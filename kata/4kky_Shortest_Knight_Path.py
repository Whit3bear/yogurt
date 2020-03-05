class cell:
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y = y
        self.dist = dist

def isInside(x, y):
    if (x >= 1 and x <= 8 and y >= 1 and y <= 8):
        return True
    return False

def knight(p1, p2):
        arr_p1 = [ord(p1[0])-96, int(p1[1])]
        arr_p2 = [ord(p2[0])-96, int(p2[1])]         
        
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]

        queue = []

        queue.append(cell(arr_p1[0], arr_p1[1], 0))

        visited = [[False for i in range(9)] for j in range(9)]

        visited[arr_p1[0]][arr_p1[1]] = True

        while(len(queue) > 0):
            t = queue[0]
            queue.pop(0)

            if(t.x == arr_p2[0] and t.y == arr_p2[1]):
                return t.dist

            for i in range(8):
                x = t.x + dx[i]
                y = t.y + dy[i]

                if (isInside(x, y) and not visited[x][y]):
                    visited[x][y] = True
                    queue.append(cell(x, y, t.dist + 1))

print(knight('a1','c1'))