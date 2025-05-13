def word_frequencies(text):
    count={}
    words=text.split()
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))