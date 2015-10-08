def censor(text,word):
    text_list=text.split(" ")
    new_list=list()
    for element in text_list:
        if element.lower()==word.lower():
          new_list.append("*"*len(element))
        else:
            new_list.append(element)
    return " ".join(new_list)


print censor("this is india","is")