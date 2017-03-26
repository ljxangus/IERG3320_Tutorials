from nltk.corpus import wordnet

# WordList contains the word we need to build the dictionary
word_dict = {'good':1,'bad':-1,'like':1,'hate':-1}
seed_dict = dict()

for o_word in word_dict:
    
    # Finding the synonyms and antonyms for this word 
    synonyms = []
    antonyms = []
    score = word_dict[o_word]
    
    for syn in wordnet.synsets(o_word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
                
    # Appending the words into the dictionary if it does not exist, with its score
    # We assume that positive words get +1 and negative get -1
    synonyms.append(o_word)
    
    for word in synonyms:
        seed_dict[word] = score
        
    for word in antonyms:
        seed_dict[word] = -score
                  
print(seed_dict)


