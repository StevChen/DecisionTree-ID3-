import pandas as pd

from modules.DecisionTreeID3 import DecisionTree
from modules.DecisionTreeC45 import DecisionTreeC45
from modules.Graph import Graph
from modules.util import test, prune

def main():
    # load dataset
    # mushroom data
    # dataset = pd.read_csv('../Data/mushrooms.csv')
    # target = 'class'

    # car data
    dataset = pd.read_csv('../Data/breast-cancer.data', header=None)
    dataset.columns = ['class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps', 'deg-malig', 'breast', 'breast-quad', 'irradiat']
    target = 'class'

    # TTT data
    # dataset = pd.read_csv('../Data/tic-tac-toe.data', header=None)
    # dataset.columns = ['tls', 'tms', 'trs', 'mls', 'mms', 'mrs', 'lls', 'lms', 'lrs', 'class']
    # target = 'class'

    print(dataset.describe())
    train_set = dataset.sample(frac=0.5, random_state=1)
    # train_set.to_csv('train.csv', index=False)
    dataset = dataset.drop(train_set.index)
    valid_set = dataset.sample(frac=0.5, random_state=1)
    # valid_set.to_csv('validation.csv', index=False)
    test_set = dataset.drop(valid_set.index)
    # test_set.to_csv('test.csv', index=False)

    # train_set = pd.read_csv('train.csv')
    # valid_set = pd.read_csv('validation.csv')
    # test_set = pd.read_csv('test.csv')
    # target = 'class'

    # print(test_set.describe())
    # test_set = dataset.sample(frac=0.3)
    # dataset = dataset.drop(test_set.index)
    # print(dataset.describe())

    # dataset.columns = ['Outlook', 'Temp', 'Humidity', 'Windy', 'target']
    # print(dataset)

    # create decision tree object and run it
    # c45tree = DecisionTreeC45(train_set, target)
    # c45tree.build_Tree()
    # print('building...')
    # prune(c45tree.getRoot(), valid_set, target)
    # print('pruning...')

    id3tree = DecisionTree(train_set, target)
    id3tree.build_Tree()

    accuracy_rate_1 = test(id3tree.getRoot(), test_set, target)
    # accuracy_rate_2 = test(c45tree.getRoot(), test_set, target)
    print('before prune', accuracy_rate_1)   

    prune(id3tree, id3tree.getRoot(), valid_set, target)
    accuracy_rate_1 = test(id3tree.getRoot(), test_set, target)
    print('after prune', accuracy_rate_1)
    # id3tree.prune(id3tree.getRoot(), valid_set)

    # view the decision tree
    # G = Graph('C4.5 Decision Tree')
    # G.printTree(c45tree.getRoot())
    # G.draw('../output/c45.dot', '../output/c45.png', font_size=3, node_size=50, label_size=3)
    
    D = Graph('ID3 Decision Tree')
    D.printTree(id3tree.getRoot())
    D.draw('../output/id3.dot', '../output/id3.png', font_size=3, node_size=50, label_size=3)


    # accuracy_rate_1 = test(id3tree.getRoot(), test_set, target)
    # # accuracy_rate_2 = test(c45tree.getRoot(), test_set, target)
    # print(accuracy_rate_1)    

    # test the decision tree
    # print(valid_set.iloc[0])
    # result = id3tree.predict(id3tree.getRoot(), valid_set.iloc[0])
    # result = id3tree.test(valid_set)


if __name__ == '__main__':
    main()