def remove_duplicates(data):
    new_list=list()
    for i in data:
      if not i in new_list:
          new_list.append(i)
    return new_list
print remove_duplicates([1,2,3,1,4])