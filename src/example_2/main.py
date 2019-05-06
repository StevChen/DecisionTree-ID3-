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

    train_set = pd.read_csv('train.csv')
    valid_set = pd.read_csv('validation.csv')
    test_set = pd.read_csv('test.csv')
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
    id3tree = DecisionTree(train_set, target)
    id3tree.build_Tree()

    D = Graph('ID3 Decision Tree')
    D.printTree(id3tree.getRoot())
    D.draw('id3_before_prune.dot', 'id3_before_prune.png', font_size=3, node_size=50, label_size=3)

    accuracy_rate_1 = test(id3tree.getRoot(), test_set, target)
    print('id3 before prune', accuracy_rate_1)

    prune(id3tree, id3tree.getRoot(), valid_set, target)
    accuracy_rate_1 = test(id3tree.getRoot(), test_set, target)
    print('id3 after prune', accuracy_rate_1)
    
    D = Graph('ID3 Decision Tree')
    D.printTree(id3tree.getRoot())
    D.draw('id3.dot', 'id3.png', font_size=3, node_size=50, label_size=3)

# ================================c4.5=====================================

    c45tree = DecisionTreeC45(train_set, target)
    c45tree.build_Tree()

    D = Graph('c4.5 Decision Tree')
    D.printTree(c45tree.getRoot())
    D.draw('c45_before_prune.dot', 'c45_before_prune.png', font_size=3, node_size=50, label_size=3)

    accuracy_rate_1 = test(c45tree.getRoot(), test_set, target)
    print('c45 before prune', accuracy_rate_1)   

    prune(c45tree, c45tree.getRoot(), valid_set, target)
    accuracy_rate_1 = test(c45tree.getRoot(), test_set, target)
    print('c45 after prune', accuracy_rate_1)
    
    D = Graph('c4.5 Decision Tree')
    D.printTree(c45tree.getRoot())
    D.draw('c45.dot', 'c45.png', font_size=3, node_size=50, label_size=3)


if __name__ == '__main__':
    main()