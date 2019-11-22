#from collections import OrderedDict
def torrent(files):     
    res = dict()
    for file in files:        
        name, size, speed = file.values()
        time = size * 1000 * 8 / speed
        res[name] = time

    lst = sorted(res.items(), key=lambda kv: (kv[1], kv[0]))     
    
    return [x[0] for x in lst], int(max(res.values()))

file_1 = {"name": "alien", "size_GB": 38, "speed_Mbps": 38}
file_2 = {"name": "predator", "size_GB": 38, "speed_Mbps": 2}
file_3 = {"name": "terminator", "size_GB": 5, "speed_Mbps": 25}
file_4 = {"name": "zombieland", "size_GB": 38, "speed_Mbps": 38}

# Basic 
#files = [file_1, file_2, file_3]
files = [{'name': 'alien prometheus', 'size_GB': 160, 'speed_Mbps': 80}, {'name': 'alien vs predator', 'size_GB': 40, 'speed_Mbps': 80}]

print(torrent(files))
#(["terminator", "alien", "predator"], 152000))


#['alien vs predator', 'alien prometheus']