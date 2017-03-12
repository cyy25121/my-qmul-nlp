import nltk
from nltk import tree, Nonterminal, induce_pcfg
from nltk.draw.tree import TreeView


def loadData(path):
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data


def getTreeData(data):
    return map(lambda s: tree.Tree.fromstring(s), data)


# Main script
rules = list()
print "loading data.."
data = loadData('parseTrees.txt')
print "generating trees.."
treeData = getTreeData(data)
print "gathering rules"
for t in treeData:
    rules.extend(t.productions())
print("Number of rules: " + str(len(rules)))
print "constructing PCFG"
S = Nonterminal('S')
grammar = induce_pcfg(S, rules)
print "PCFG:"
print(grammar)

sentense = "show me the meals on the flight from Phoenix".split()

print "parsing with Viterbi parser..."
viterbi_parser = nltk.ViterbiParser(grammar)
# viterbi_parser.trace(3)
for tree in viterbi_parser.parse(sentense):
    print(tree)
print "parsing with InsideChart parser..."
inside_parser = nltk.InsideChartParser(grammar)
viterbi_parser.trace(3)
idx = 0
for tree in inside_parser.parse(sentense):
    print(tree)
    TreeView(tree)._cframe.print_to_file('output' + str(idx) + '.ps')
    idx = idx + 1
print "done!"
