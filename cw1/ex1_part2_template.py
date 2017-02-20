
# coding: utf-8

from nltk.probability import ConditionalFreqDist
from nltk.probability import ConditionalProbDist, LaplaceProbDist, MLEProbDist

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
	return "TODO"

# conditionalProbDist will return a probability distribution over a list of
# bigrams, together with a specified probability distribution constructor
def conditionalProbDist(probDist, bigrams):
	cfDist = ConditionalFreqDist(bigrams)
	cpDist = ConditionalProbDist(cfDist, probDist, bins=len(bigrams))
	return cpDist

# this is the function where you can put your main script, which you can then
# toggle if for test purposes
def mainScript():
	return "TODO"

# The line below can be toggled as a comment to toggle execution of the main script
# results = mainScript()
