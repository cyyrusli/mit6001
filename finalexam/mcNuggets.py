def McNuggets(n):
    """
    n is an int
    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    packages = (6, 9, 20)
    a = packages[0]
    b = packages[1]
    c = packages[2]
    for x in range(0, n):
        for y in range(0, n):
            for z in range(0, n):
                if a*x + b*y + c*z == n:
                     return True
    return False

print (McNuggets(15))