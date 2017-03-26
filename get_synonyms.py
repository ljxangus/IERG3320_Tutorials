from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name());
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print "The synonyms are:"
print(set(synonyms))
print "The antonyms are:"
print(set(antonyms))
