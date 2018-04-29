import pickle

#This script writes the top users Text to a new file

dictNew = {}
with open('files/userText.p', 'rb') as userTextF, open('files/topUserTextDegree.p','wb') as newfile, open('files/top10UsersDegreeCentrality.txt','r',encoding='utf-8') as checkFile:
    users = checkFile.read().splitlines()
    dict = pickle.load(userTextF)
    for key in dict:
        if (key in users):
            dictNew[key] = dict[key]
    pickle.dump(dictNew,newfile)