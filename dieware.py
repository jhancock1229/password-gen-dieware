with open("dieware_list.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[int(key)] = val