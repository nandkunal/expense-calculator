def reverse(x):
  if len(x)==1:
      return x
  return reverse(x[1:])+x[0]
print reverse("abcd")
