#/usr/bin/python

import nltk

#parser=nltk.load_parser('semGrammarFOLE.fcfg')
parser=nltk.load_parser('semGrammarSimple.fcfg')

def semParse(sentence):
    print "Parsing \"" + sentence + "\":"
    tree_generator = parser.parse(sentence.split())
    for tree in tree_generator: 
        #print "  type:", tree.label()['SEM'].type
        print "    LF:", tree.label()['SEM']
        # for subtree in tree.subtrees():
        #     print subtree.label()['SEM'].type, subtree.label()['SEM']

semParse("show me the meals")
semParse("show me the meals on the flights to Phoenix")
