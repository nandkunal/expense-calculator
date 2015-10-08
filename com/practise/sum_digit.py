def sum_digit(x):
 num=x
 sum=0
 while num!=0:
     sum+=num%10
     num=num/10
 return sum
sum_digit(434)
