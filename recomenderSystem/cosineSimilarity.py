import pickle
import itertools

def jaccard(set_1, set_2):
    if float(len(set_1.union(set_2))) != 0:
        return len(set_1.intersection(set_2)) / float(len(set_1.union(set_2)))
    else:
        return 0

with open('files/CommunitiesTextbyUser.p', 'rb') as comMembersFile, open('files/jaccardSimilarityContent.p', 'wb') as resultsFile, open('files/CommunityMembers.p','rb') as checkFile:

    communities = pickle.load(comMembersFile)
    dict = {}
    results = {}
    p = 0
    for community in communities:
        members = communities[community]
        print(len(members))
        print(community)
        #print(members)
        for pair in itertools.product(members, repeat=2):
            p += 1
            if pair[0] != pair[1]:
                value = round(jaccard(communities[community][pair[0]], communities[community][pair[1]]),2)
                results[pair[0] + ',' + pair[1]] = value
    print(p)
    pickle._dump(results,resultsFile)
