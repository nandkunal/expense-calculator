
def median(data):
    data=sorted(data)
    length=len(data)
    m=length/2
    if length%2==0:
        #print data
        #print data[m],data[m-1]
        return (data[m-1]+float(data[m]))/2
    else:
        return data[m]

print median([4,5,5,4])
#4,4,5,5