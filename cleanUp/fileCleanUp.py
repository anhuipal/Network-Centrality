#Removes any words that are undisaired from a file and creates a new "clean" file

bad_words = ['limit']

with open('tweets2.txt') as oldfile, open('tweets.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
