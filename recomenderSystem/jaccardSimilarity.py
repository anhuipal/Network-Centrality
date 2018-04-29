import pickle
import itertools

def jaccard(set_1, set_2):
    return len(set_1.intersection(set_2)) / float(len(set_1.union(set_2)))

with open('files/edgeList.txt','r', encoding='utf-8') as edgeListFile, open('files/CommunityMembers.p', 'rb') as comMembersFile, open('files/jaccardSimilarityStructural.p', 'wb') as resultsFile:
    members = pickle.load(comMembersFile)

    dict = {}
    results = {}
    edgeList = edgeListFile.readlines()

    for key in members:
        for member in members[key]:
            for user in edgeList:
                userList = user.split(',')
                if userList[0] in member:
                    if member in dict:
                        dict[member].add(userList[1])
                    else:
                        dict[member] = {userList[1]}
    p = 0
    members = dict.keys()
    for pair in itertools.product(members, repeat=2):
        p +=1
        if pair[0] != pair[1]:
            value = round(jaccard(dict[pair[0]], dict[pair[1]]), 2)
            #print(pair,value)
            results[pair[0] + ',' + pair[1]] = value
    print(p)
    pickle._dump(results,resultsFile)
