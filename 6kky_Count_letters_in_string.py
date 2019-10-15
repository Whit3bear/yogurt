def letter_count(s):
    chars = set(s)  
    return {c: s.count(c) for c in sorted(chars)}
