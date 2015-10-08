def ant_vowel(text):
    s=""
    for c in text:
        if not is_vowel(c):
           s+=c
    return s.strip()
def is_vowel(p):
    if p=='A'or p=='a'or p=='E'or p=='e'or p=='I'or p=='i'or p=='O'or p=='o'or p=='U'or p=='u':
        return True
    else:
        return False
print ant_vowel("Hi Yay")