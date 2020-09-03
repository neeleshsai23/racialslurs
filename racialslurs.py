file = open('tweets.txt','r')
words = ['array of racial words']
tweetnum = 0
counter = 0
for line in file:
    tweetnum+=1
    for n in range(len(words)):
        if(words[n-1].lower() in line.lower()):
            counter+=1
    print('Tweet '+tweetnum+'has '+counter+' racism words')