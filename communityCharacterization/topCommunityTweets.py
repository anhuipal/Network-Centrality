import pickle

#This script writes the top users Text to a new file

dictNew = {}

with open('files/userText.p', 'rb') as userTextF, open('files/topUserCommunitiesText.p','wb') as newfile, open('files/CommunityMembers.p','rb') as checkFile:
    dictMembers = pickle.load(checkFile)
    dictText = pickle.load(userTextF)

    for key in dictMembers:

        for keyT in dictText:
            membersList = dictMembers[key]

            for member in membersList:

                member = member.rstrip()

                if (keyT in member):

                    if key in dictNew:
                        dictNew[key].append(dictText[keyT])
                    else:
                        dictNew[key] = [dictText[keyT]]

    pickle.dump(dictNew,newfile)