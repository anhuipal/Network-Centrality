import pickle
import re

#this function splits the line according to the charcters in the object list

def splitLine(line,list):
    for item in list:
        ln = line.split(item)
    return ln

#Data structures used
dict = {}
userNameList = []

with open('files/CommuntiesClusters.txt', 'r', encoding='utf-8') as f, open('files/top10Com.txt' ,'r') as checkFile:

    fileLines = f.readlines()
    checkFileLines = checkFile.readlines()

    for i,text in enumerate(checkFileLines):
        text = str(text)
        checkFileLines[i] = text.rstrip()
        print(checkFileLines)
    for line in fileLines:
        ln = line.replace('\t', " ")
        ln = ln.split(' ')
        print(ln)
        if ln[0] in(checkFileLines):

            #userName = re.sub('[0-9]','',ln[1])
            userName = ln[2]
            userName = userName.replace('"','')
            userName = userName.lstrip()
            print(ln[2])
            if ln[0] in dict:
                dict[ln[0]].append(userName)
            else:
                dict[ln[0]] = [userName]
    with open('files/CommunityMembers.p', 'wb') as members:
        pickle.dump(dict, members)