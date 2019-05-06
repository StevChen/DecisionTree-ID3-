from modules.util import findMostFrequentClass, findBestAttribute
from modules.Node import Node

class DecisionTree:
    def __init__(self, dataset, target, category = None, attribute = None):
        self.dataset = dataset
        self.target = target
        self.category = category
        self.attribute = attribute

    def build_Tree(self):
        self.root = Node(self.dataset)

        if(len(self.dataset[self.target].unique()) == 1): # The result is unique
            # print("There is only one type of target for {}, set label = {}".format(self.category, self.dataset[self.target].iloc[0]))
            # self.root.setName(self.category)
            self.root.setValue(self.dataset[self.target].iloc[0])
            return self.root
        if(len(self.dataset.columns) <= 2):  # There is only one attribute left
            # print("There is only one attribute, set label = ", findMostFrequentLabel(self.dataset[self.target]))
            # self.root.setName(self.category)
            self.root.setValue(findMostFrequentClass(self.dataset[self.target]))
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

    def getRoot(self):
        return self.root