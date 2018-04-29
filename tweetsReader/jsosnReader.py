from nltk.corpus import stopwords
import json
import sys
import pickle

class JSONParser():

    usersTweets = {}
    edgeList = {}
    cleanUserTweets = {}

    try:
        with open('tweetsReader/tweets.txt', 'r') as f:
            p = 0
            for line in f:
                if line.strip():
                    tweet = json.loads(line)
                    #print(json.dumps(tweet, indent=4)) #Prints the json file with the tweets
                    if tweet['in_reply_to_user_id_str']:
                        tweetText = tweet['text']
                        # slits the text into a list for further processing
                        wordList = tweetText.split()
                        # The following line cleans the text from stop words and links
                        cleanText = [word for word in wordList if word not in stopwords.words('english') and len(word) >= 3]
                        #Creates the network
                        if tweet['user']['screen_name'] in edgeList:
                            edgeList[tweet['user']['screen_name']].append(tweet['in_reply_to_screen_name'])
                        else:
                            edgeList[tweet['user']['screen_name']] = [tweet['in_reply_to_screen_name']]
                        #edgeList[tweet['user']['screen_name']] = tweet['in_reply_to_screen_name']
                        # adds the clean list to a user
                        if tweet['user']['screen_name'] in usersTweets:
                            usersTweets[tweet['user']['screen_name']].append(cleanText)
                        else:
                            usersTweets[tweet['user']['screen_name']] = [cleanText]
                else:
                    #print('Empty Line') # The file contains an empty line
                    True
            print(usersTweets)
            with open('files/edgeList.txt','w') as edgeListF:
                for key, value in edgeList.items():
                    if isinstance(value,list):
                        for user in value:
                            edgeListF.write('%s,%s\n' % (key, user))
                    else:
                        edgeListF.write('%s,%s\n' % (key, user))
            with open('files/userText.p','wb') as userTextF:
                pickle.dump(usersTweets,userTextF)
    except:
        print
        "Unexpected error:", sys.exc_info()[0]
        raise