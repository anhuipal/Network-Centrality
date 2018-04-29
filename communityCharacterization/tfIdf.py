import math
import pickle

def tf(word, blob):
    return blob.count(word) / len(blob)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

dict = pickle.load(open('files/topUserCommunitiesText.p','rb'))
bloblist = []
b = []

for key in dict:
    for wordList in dict[key]:
        for words in wordList:
            for text in words:
                b.append(text)
    bloblist.append(b)
    b = []

keyList = list(dict.keys())

with open('files/tfidfCom.txt','w',encoding='utf-8') as f:
    for i, blob in enumerate(bloblist):
        print (blob)
        f.write("Top words in document for cluster:  {} \n".format(keyList[i]))
        print("Top words in document for cluster:  {}".format(keyList[i]))
        scores = {word: tfidf(word, blob, bloblist) for word in blob}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:3]:
            f.write("Word: {}, TF-IDF: {} \n".format(word, round(score, 5)))
            print("Word: {}, TF-IDF: {} ".format(word, round(score, 5)))