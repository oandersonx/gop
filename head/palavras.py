import nltk
from nltk.corpus import wordnet
#nltk.download('tagsets')
text = nltk.word_tokenize("Hi, my name is You, I want to print the 1) outstanding invoice")
a = nltk.pos_tag(text)
print(a)
print(nltk.help.upenn_tagset('NNP'))


for i in a:
    print(i[1])
    if(i[1] == None):
        print('Palavra Errada...\n')
        print(i[i])