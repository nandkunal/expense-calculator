def is_prime(x):
    if x<0:
        return False
    if x==0:
        return False
    if x==1:
        return False
    if x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
    else:
        return True
print is_prime(-7)
