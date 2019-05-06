import sys
sys.path.append("..")

import pandas as pd

from modules.DecisionTreeID3 import DecisionTree
from modules.DecisionTreeC45 import DecisionTreeC45
from modules.Graph import Graph

from modules.util import test, prune

def main():
    # load dataset
    # dataset = pd.read_csv('../../Data/breast-cancer.data', header=None)
    # dataset.columns = ['class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat']
    # target = 'class'

    train_set_1 = pd.read_csv('train.csv')
    train_set_2 = pd.read_csv('train_numeric.csv')
    target = 'class'

    # print(dataset.describe())
    # train_set = dataset.sample(frac=0.5, random_state=1)
    # train_set.to_csv('train.csv', index=False)
    # dataset = dataset.drop(train_set.index)
    # valid_set = dataset.sample(frac=0.5, random_state=1)
    # valid_set.to_csv('validation.csv', index=False)
    # test_set = dataset.drop(valid_set.index)
    # test_set.to_csv('test.csv', index=False)

# ================================ID3=====================================
    # id3tree = DecisionTree(train_set_2, target)
    # id3tree.build_Tree()

    # D = Graph('ID3 Decision Tree')
    # D.printTree(id3tree.getRoot())
    # D.draw('id3_numerical.dot', 'id3_numerical.png', font_size=7, node_size=50, label_size=7)

# ================================c4.5=====================================

    c45tree = DecisionTreeC45(train_set_2, target)
    c45tree.build_Tree()
    
    D = Graph('c4.5 Decision Tree')
    D.printTree(c45tree.getRoot())
    D.draw('c45.dot', 'c45.png', font_size=7, node_size=50, label_size=7)


if __name__ == '__main__':
    main()