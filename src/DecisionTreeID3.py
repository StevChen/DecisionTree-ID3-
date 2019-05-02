from util import findMostFrequentLabel, findBestAttribute
from Node import Node

class DecisionTree:
    def __init__(self, dataset, target, category = None, attribute = None):
        self.dataset = dataset
        self.target = target
        self.category = category
        self.attribute = attribute

    def build_Tree(self):
        self.root = Node(self.dataset)

        if(len(self.dataset[self.target].unique()) == 1): # The result is unique
            print("There is only one type of target for {}, set label = {}".format(self.category, self.dataset[self.target].iloc[0]))
            self.root.setName(self.category)
            self.root.setValue(self.dataset[self.target].iloc[0])
            return self.root
        if(len(self.dataset.columns) <= 2):  # There is only one attribute left
            print("There is only one attribute, set label = ", findMostFrequentLabel(self.dataset[self.target]))
            self.root.setName(self.category)
            self.root.setValue(findMostFrequentLabel(self.dataset[self.target]))
            return self.root

        else:
            # find the best attribute
            best_attribute = findBestAttribute(self.dataset, self.target) 
            print("Chosen best Attribute ", best_attribute)
            self.root.setName(best_attribute)
            best_attribute_dataGroup = self.dataset.groupby(best_attribute)

            # iterate categories of the best attribute, add branches to the root
            for category, data in best_attribute_dataGroup:
                data = data.drop(best_attribute, axis = 1)
                subtree = DecisionTree(data, self.target, category, best_attribute)
                self.root.addBranch(category, subtree.build_Tree())
        return self.root

    def predict(self, root, row_data):
        Node = root.getBranch()[row_data[root.getName()]]
        if(Node.getValue() is not None): # reach a terminal node
            return Node.getValue()
        else:
            return self.predict(Node, row_data)

    def test(self, dataset):
        result = list()
        for row in dataset.iterrows():
            result.append(self.predict(self.root, row[1]))
        return result

    def getRoot(self):
        return self.root