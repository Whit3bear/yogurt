def vert_mirror(s):
    return '\n'.join(map(lambda x: x[::-1], s.split('\n')))    
def hor_mirror(s):
    return '\n'.join(reversed(s.split('\n')))
def oper(fct, s):
    return fct(s)

#print(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
#"QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw"
print(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"))
#"yeCt\nCSbg\nJVhv\nlVHt")