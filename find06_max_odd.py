def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i=0
    n=0
    a=data[0]
    while n<len(data):
        if a<data[n]:
            a=data[n] 
        if a%2==0:
            a=data[n]
        n=n+1
    return a
print(find_max_odd([1, 4, 3, 8, 5]))