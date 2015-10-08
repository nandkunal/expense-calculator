def purify(data):
    new_list=list()
    for i in data:
        if i%2==0:
            new_list.append(i)
    return new_list