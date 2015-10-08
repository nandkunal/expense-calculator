def is_int(x):
 if type(x)==int:
     return True
 else:
     diff=x-int(x)
     if diff==0:
         return True
     else:
         return False

x=4.00
print is_int(x)