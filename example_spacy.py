import spacy

sp = spacy.load('pt')
sentence = sp(u'Filipe está com muita fome em Lisboa, pois ainda não comeu bolacha hoje.')
for word in sentence:
    pass
    # print(word.text, word.pos_, word.dep_)

for entity in sentence.ents:
    pass
    # print(entity.text + ' - ' + entity.label_ + ' - ' + str(spacy.explain(entity.label_)))

for noun in sentence.noun_chunks:
    print(noun.text)