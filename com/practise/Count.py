def count(sequence,item):
    c=0
    for i in sequence:
       if i==item:
           c+=1
    return c
print count([1,2],1)
