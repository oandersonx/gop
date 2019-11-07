import spacy

nlp = spacy.load('pt_core_news_sm')

text = nlp('Ola mundo. Classica frase no mundo da computacao')

print(type(text))

for token in text.ents:
    print(token.text)
    