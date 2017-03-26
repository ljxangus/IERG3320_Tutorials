# Tokenize the text

from nltk import word_tokenize,sent_tokenize

with open('test.txt', mode='r') as file_in:
    test_txt = file_in.read()

sent_tokens = sent_tokenize(test_txt)

word_tokens = []

for sent in sent_tokens:
    word_token = word_tokenize(sent)
    word_tokens.append(word_token)

print word_tokens
