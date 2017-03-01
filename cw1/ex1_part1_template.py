# coding: utf-8

import unicodecsv			# csv reader
from sklearn.svm import LinearSVC
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
from nltk.classify import SklearnClassifier
from random import shuffle
from datetime import datetime
from datetime import timedelta


# DATA LOADING AND PARSING

# convert line from input file into a datetime/string pair
def parseTweet(tweetLine):
    dt = datetime.strptime(tweetLine[1], '%Y-%m-%d %H:%M:%S')
    s = tweetLine[4]
    # should return a pair of a datetime object and a string containing the tweet message
    return (dt, s)

# load data from a file and append it to the tweetData
def loadData(path, label, tweet=None):
    with open(path, 'rb') as f:
        reader = unicodecsv.reader(f, encoding='utf-8')
        reader.next()
        for line in reader:
            (dt,tweet) = parseTweet(line)
            tweetData.append((dt,preProcess(tweet),label))
            trainData.append((toFeatureVector(preProcess(tweet)),label))

# load application data
def loadApplicationData(path):
    with open(path, 'rb') as f:
        reader = unicodecsv.reader(f, encoding='utf-8')
        reader.next()
        for line in reader:
            londonTweetData.append(parseTweet(line))

# TEXT PREPROCESSING AND FEATURE VECTORIZATION

# input: a string of one tweet
def preProcess(text):
    # should return a list of tokens
    s = text.split(' ')
    return s

# input: a tokenised sequence
# you can optionally keep track of a global feature list that is a list of all the features (or words) that you encounter while going through the dataset
# featureList = {} 
def toFeatureVector(words):
    featureVector = {}
    for w in words:
        if w in featureVector:
            #featureVector[w] = featureVector[w] + 1
            pass
        else:
            featureVector[w] = 1
    # return a dictionary 'featureVect' where the keys are the tokens in 'words' and the values are the number of occurrences of the tokens
    return featureVector
    # return {w: 1, 0 for w in words}

# TRAINING AND VALIDATING OUR CLASSIFIER

def trainClassifier(trainData):
    print "Training Classifier..."
    return SklearnClassifier(LinearSVC()).train(trainData)

def crossValidate(dataset, folds):
    shuffle(dataset)
    results = []
    foldSize = len(dataset)/folds
    for i in range(0,len(dataset),foldSize):
        clf = trainClassifier(dataset[:i] + dataset[i+foldSize:])
        pLabel = predictLabels(dataset[i:i+foldSize], clf)
        yLabel = [ l[1] for l in dataset[i:i+foldSize]]
        results.append((accuracy_score(yLabel, pLabel), precision_recall_fscore_support(yLabel, pLabel)))
        # insert code here that trains and tests on the 10 folds of data in the dataset
    return results

# PREDICTING LABELS GIVEN A CLASSIFIER

def predictLabels(tweetData, classifier):
    test = map(lambda t: t[0], tweetData)
    #return classifier.classify_many(map(lambda t: toFeatureVector(preProcess(t[1])), tweetData))
    return classifier.classify_many(test)

def predictLabel(text, classifier):
    return classifier.classify(toFeatureVector(preProcess(text)))

# COMPUTING ANGER LEVEL ON A SET OF TWEETS

def findAngerLevels(tweetData, classifier):
    # should return a list of anger level for a period of time
    sorttweetData = sorted(tweetData)
    hist = []
    i = 0
    for s in sorttweetData:
        i = i + 1
        pLabel = predictLabel(s[1], classifier)
        hist.append((s[0], pLabel))

    initD = hist[0][0]
    delta = timedelta(1)
    idxD = initD + delta
    new_hist = []
    count = {'angry':0, 'happy':0}
    print(idxD)
    for h in hist:
        while h[0] >= idxD:
            idxD = idxD + delta
            new_hist.extend(count)
            count['angry'] = 0
            count['happy'] = 0
        if h[1] == 'happy':
            count['happy'] = count['happy'] + 1
        else:
            count['angry'] = count['angry'] + 1

    return new_hist

# MAIN

# loading tweets
# tweets will have one feature, which is going to be a numerical value

tweetData = []
trainData = []
londonTweetData = []

# the output classes
angryLabel = 'angry'
happyLabel = 'happy'

# references to the data files
datasetPath = 'dataset/tweets/'
angryPath = datasetPath + 'angry_tweets.csv'
happyPath = datasetPath + 'happy_tweets.csv'
londonPath = datasetPath + 'london_2017_tweets.csv'


## In order to test the code in this
##
# do the actual stuff
print "Loading happy tweets..."
loadData(happyPath, happyLabel)
print "Loading angry tweets..."
loadData(angryPath, angryLabel)
#print 'number of words: ' + str(len(featureDict))
cv_results = crossValidate(trainData, 10)
print cv_results
#classifier = trainClassifier(trainData)
print "Loading London data"
#loadApplicationData(londonPath)
print "Computing anger levels!"
#angerLevels = findAngerLevels(londonTweetData, classifier)
#anger_peaks = None
#print anger_peaks
