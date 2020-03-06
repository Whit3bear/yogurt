class omnibool:         
    def __eq__(self, other):        
        return True    

omnibool = omnibool()

print(omnibool == True)
print(omnibool == False)