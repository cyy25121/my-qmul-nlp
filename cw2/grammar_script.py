import nltk
from nltk.corpus import treebank

# here we load in the sentences
sentence22 = treebank.parsed_sents('wsj_0003.mrg')[21]
sentence7 = treebank.parsed_sents('wsj_0003.mrg')[6]
sentence13 = treebank.parsed_sents('wsj_0004.mrg')[12]

# here we define a grammar
# grammar = nltk.CFG.fromstring("""
# S -> NP VP
# NP -> Det N | 'NLP' | 'I'
# VP -> V NP
# Det -> 'the'
# N -> 'students' | 'subject'
# V -> 'like' | 'love'
# # """)
grammar = nltk.CFG.fromstring("""
S -> NP VP
S -> Aux NP VP
S -> VP
NP -> Pronoun
NP -> Proper-Noun
NP -> Det Nominal
Nominal -> N
Nominal -> N N
Nominal -> N PP
VP -> V
VP -> V NP
VP -> V NP PP
VP -> V PP
VP -> VP PP
PP -> Preposition NP
S -> IVP
IVP -> IVerb NP NP
IVP -> IVerb NP NP PP
IVerb -> 'show'
Det -> 'that' | 'this' | 'the' | 'a'
N -> 'book' | 'flight' | 'meal' | 'money' | 'show' | 'meals' | 'flights'
V -> 'book' | 'include' | 'prefer' | 'show'
Pronoun -> 'I' | 'she' | 'me'
Proper-Noun -> 'Houston' | 'NWA' | 'sf'
Aux -> 'does'
Preposition -> 'from' | 'to' | 'on' | 'near' | 'through'
NP -> NP PP
""")
# here we let nltk construct a chart parser from our grammar
parser = nltk.ChartParser(grammar)
#print(parser.grammar())
# input: a list of words
# returns all the parses of a sentence
def allParses(sentenceList):
	return parser.parse(sentenceList)

# input: a list of parse trees
# prints all the parse trees
def printParses(parses):
	for tree in parses:
		print(tree)
		tree.draw()

# input: a sentence as a string or as a list of words
# prints a sentence, then parses it and prints all the parse trees
def processSentence(sentence):
	sentenceList = sentence
	if isinstance(sentence,str):
		sentenceList = sentence.split(' ')
	print 'Original sentence: ' + ' '.join(sentenceList)
	printParses(allParses(sentenceList))

def mainScript():
	#processSentence('I like NLP')
	#processSentence('the students love the subject')
	processSentence('Show me the meals on the flight from SF'.lower())



if __name__ == '__main__':
	mainScript()
