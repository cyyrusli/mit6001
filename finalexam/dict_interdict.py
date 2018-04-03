# function f depends on the question
def f(a,b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference = {}
    for key in d1:
        if key in d2:
            difference[key] = f(d1[key],d2[key])
        else:
            intersect[key] = d1[key]
    for key in d2:
        if key not in d1:
           intersect[key] = d2[key]
    tuple_interdiff = (difference, intersect)
    return tuple_interdiff