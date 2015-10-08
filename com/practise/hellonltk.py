import nltk
from nltk.tokenize import sent_tokenize,word_tokenize


example_text="Hello Mr.Smith,how are you doing today.How's life? The weather is great and Python is awesome."
print sent_tokenize(example_text)
print word_tokenize(example_text,'english')
for word in word_tokenize(example_text,'english'):
    print word