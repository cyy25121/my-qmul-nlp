
# coding: utf-8

from nltk.probability import ConditionalFreqDist
from nltk.probability import ConditionalProbDist, LaplaceProbDist, MLEProbDist

from datetime import datetime
from datetime import timedelta

from ex1_part1_template import loadApplicationData
from ex1_part1_template import preProcess


##############
### PART B ###
##############

####
## A bigram model using the NLTK built-in functions
####

# given a list of lists of preprocessed tweets,
# getBigrams should return a list of pairs containing all the bigrams that
# are observed in the list.

def getBigrams(tweets):
    newT = []
    for T in tweets:
        first = True
        for t in T:
            if first is True:
                pre = t
                first = False
            else:
                cur = t
                newT.append((pre, cur))
                pre = cur
    return newT

# conditionalProbDist will return a probability distribution over a list of
# bigrams, together with a specified probability distribution constructor
def conditionalProbDist(probDist, bigrams):
    cfDist = ConditionalFreqDist(bigrams)
    cpDist = ConditionalProbDist(cfDist, probDist, bins=len(bigrams))
    return cpDist

# this is the function where you can put your main script, which you can then
# toggle if for test purposes
def mainScript():

    londonTweetData = []
    datasetPath = 'dataset/tweets/'
    londonPath = datasetPath + 'london_2017_tweets.csv'

    loadApplicationData(londonPath)
    sorted(londonTweetData)

    londonallData = []
    london5thData = []
    london9thData = []

    for d in londonTweetData:
        if d[0] >= datetime(2017, 1, 5) and d[0] < datetime(2017, 1, 6):
            london5thData.append(preProcess(d[1]))
        elif d[0] >= datetime(2017, 1, 9) and d[0] < datetime(2017, 1, 10):
            london9thData.append(preProcess(d[1]))
        londonallData.append(preProcess(d[1]))

    s = getBigrams(london5thData)

    return s

# The line below can be toggled as a comment to toggle execution of the main script
results = mainScript()
print results
