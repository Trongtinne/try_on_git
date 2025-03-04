import nltk
from nltk.corpus import stopwords
def remove_stopwords(text):
    stop=stopwords.words("english")
    word_token=nltk.word_tokenize(text)
    for word in word_token:
        if word not in stop:
            #[ 'a','is','the','and','of','to','with']:
            output.append(word)
    return output
text="This is a sample text with many stop words like the, and, of, to, etc."
output=[]
remove_stopwords(text)
print(" ".join(output))