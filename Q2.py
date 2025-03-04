import nltk
def count_element(text):
    count=0
    words=text.split()
    print(f"Number of words:{len(words)}")
    for i in text:
        if i in [f"'","."]:
            count+=1
        else:
            count+=1
    print(f"Number of characters:{count+1}")
    sentences=nltk.sent_tokenize(text)
    print(f"Number of sentences:{len(sentences)}")
    print(f"Average word length:{len(words)/len(sentences)}")
text="This is a sample text. It's a simple example"
count_element(text)