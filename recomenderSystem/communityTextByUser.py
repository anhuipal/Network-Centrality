import pickle
import re
#This script writes the top users Text to a new file

dictNew = {}
dictMember = {}
wordsSet = set()

with open('files/userText.p', 'rb') as userTextF, open('files/CommunitiesTextbyUser.p','wb') as newfile, open('files/CommunityMembers.p','rb') as checkFile:
    dictMembers = pickle.load(checkFile)
    dictText = pickle.load(userTextF)

    for key in dictMembers:
        membersList = dictMembers[key]
        print(membersList)
        for member in membersList:
            for keyT in dictText:
                if (keyT in member):
                    print(True, keyT,member)
                    for words in dictText[keyT]:
                        for word in words:
                            wordsSet.add(word)
                    dictMember[member] = wordsSet
                    wordsSet = set()
        dictNew[key] = dictMember
        dictMember = {}

    pickle.dump(dictNew,newfile)