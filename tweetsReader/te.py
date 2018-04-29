import pickle

f = pickle.load(open('files/userText.p','rb'))

for key in f:
    print(key,f[key])