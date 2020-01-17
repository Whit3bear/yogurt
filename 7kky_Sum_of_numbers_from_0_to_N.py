def show_sequence(n):
    d = [i for i in range(0, n+1)]
    if not d:
        return f"{n}<0"
    elif len(d) == 1:
        return "0=0"
    else:    
        return f"{'+'.join(map(str, d))} = {sum(d)}"