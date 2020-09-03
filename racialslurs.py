tweets = open('tweets.txt','r')
wordsfile = open('words.txt','r')

words = []
#appending words from file into list
for word in wordsfile:
    words.append(word)

tweetnum = 0
counter = 0

for line in tweets:
    tweetnum+=1
    for n in range(len(words)):
        if(words[n-1].lower() in line.lower()):
            counter+=1
    print('Tweet '+tweetnum+'has '+counter+' racism words')