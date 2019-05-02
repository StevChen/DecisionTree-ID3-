import pandas as pd

from DecisionTreeID3 import DecisionTree
from Graph import Graph


def main():
    # load dataset
    dataset = pd.read_csv('../Data/play.data', header = None)
    dataset.columns = ['Outlook', 'Temp', 'Humidity', 'Windy', 'target']
    # print(dataset)

    # create decision tree object is run it
    dtree = DecisionTree(dataset, 'target')
    dtree.build_Tree()

    # view the decision tree
    G = Graph('ID3 Decision Tree')
    G.printTree(dtree.getRoot())
    G.draw('../output/tree.dot', '../output/tree.png')
    
    # test the decision tree

if __name__ == '__main__':
    main()