def primes_list(N):
    '''
    N: an integer
    '''
    # Your code here
    L = []
    for num in range(2,N+1):
        prime = True
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
            L.append(num)
    return L