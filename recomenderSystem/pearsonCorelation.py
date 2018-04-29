#import numpy
import pickle
import numpy

with open('files/jaccardSimilarityStructural.p', 'rb') as structuralFile, open('files/jaccardSimilarityContent.p', 'rb') as contentFile, open('files/CommunityMembers.p','rb') as comMembers:

    structuralDict = {}
    contentDict = {}
    contentList = []
    structuralList = []
    resultsStruct = {}
    resultsCon = {}

    structuralDict = pickle.load(structuralFile)
    contentDict = pickle.load(contentFile)
    comMembers = pickle.load(comMembers)

    keyStructural = set(structuralDict.keys())
    keyContent = set(contentDict.keys())

    intersection = keyStructural & keyContent

    for item in intersection:
        structuralList.append(structuralDict[item])
        contentList.append(contentDict[item])

    print(round(numpy.corrcoef(structuralList, contentList)[0, 1], 2))