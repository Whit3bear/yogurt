""" Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
 """
def namelist(names):
    arr = [x['name'] for x in names]
    return ', '.join(arr)[::-1].replace(' ,', ' & ', 1)[::-1]

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
#'Bart, Lisa, Maggie, Homer & Marge'
print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]))
#'Bart, Lisa & Maggie'
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
#'Bart & Lisa'
print(namelist([{'name': 'Bart'}]))
#'Bart'