import sys
import numpy as np
import pandas as pd

def findBest(dictionary_):
    # find best information gain or gain ratio in the dictionary
    best = list(dictionary_.keys())[0]
    for key, value in dictionary_.items():
        if(value > dictionary_[best]):
            best = key
    return best


def count(series, label):
    count = 0
    for item in series:
        if(item == label):
            count+=1
    return count

def Entropy(dataset, target):
    S = 0
    total_sample_size = dataset[target].count()
    for result in dataset[target].unique():
        result_size = count(dataset[target], result)
        S -= (result_size/total_sample_size) * np.log2(result_size/total_sample_size)
    return S

def InfoGain(dataset, attribute, target):
    EntropyS = Entropy(dataset, target)
    attribute_dataset = dataset.groupby(attribute)
    EntropySA = 0
    for category, categoryData in attribute_dataset:
         # print(categoryData[attribute], attribute)
         attribute_size = categoryData[attribute].count()
         sample_size = dataset[attribute].count()
         EntropySA += attribute_size/sample_size * Entropy(categoryData, target)

    return EntropyS - EntropySA
    
def splitInfo(dataset, attribute, target):
    splitInfo = 0
    attribute_dataset = dataset.groupby(attribute)
    for category, categoryData in attribute_dataset:
        attribute_size = categoryData[attribute].count()
        sample_size = dataset[attribute].count()
        # print(attribute, category, attribute_size, sample_size)
        splitInfo += -attribute_size/sample_size * np.log2(attribute_size/sample_size)
    return splitInfo

def findMostFrequentClass(dataset):
    try:
        return dataset.value_counts().idxmax()
    except Exception as e:
        print("Error(findMostFrequentClass) {}".format(e))
        sys.exit()

def findBestAttribute(dataset, target):
    attrOnly = dataset.drop(target, axis = 1)
    Attribute_Gain = dict()
    for attr in attrOnly.columns:
        Attribute_Gain[attr] = InfoGain(dataset, attr, target)

    return findBest(Attribute_Gain)

def findBestGainRatio(dataset, attr, target):
    # find the best gain ratio for numeric value
    EntropyS = Entropy(dataset, target)
    dataset = dataset.sort_values(by=attr)
    # print(dataset)
    gain = dict()
    for value in dataset[attr].unique():
        greater_set = dataset[dataset[attr] > value]
        if(greater_set.empty):  # there is not greater
            continue

        lower_set = dataset[dataset[attr] <= value]
        greater_ratio = greater_set[attr].count()/dataset[attr].count()
        lower_ratio = lower_set[attr].count()/dataset[attr].count()

        entropy_greater_set = Entropy(greater_set, target)
        entropy_lower_set = Entropy(lower_set, target)

        info_gain = EntropyS - greater_ratio * entropy_greater_set - lower_ratio * entropy_lower_set
        print(value, info_gain)

        gain[value] = info_gain

    best_value = findBest(gain)
    print('selected value: ', best_value)
    return gain[best_value], best_value

    
def findBestAttributeRatio(dataset, target):
    attrOnly = dataset.drop(target, axis = 1)
    Attribute_GainRatio = dict()
    for attr in attrOnly.columns:

        if(np.issubdtype(dataset[attr].dtype, np.number)): #numeric column
            info_gain, best_value = findBestGainRatio(dataset[[attr, target]], attr, target)
            dataset[attr] = dataset[attr] > best_value
            # print(dataset)
            new_name = attr + '>'+str(best_value)
            dataset = dataset.rename(columns={attr: new_name})
            attr = new_name
            # gain ratio instead of info gain
            Attribute_GainRatio[new_name] = info_gain/splitInfo(dataset, attr, target)
            
            # print('best value ', best_value)
        # print(attr, InfoGain(dataset, attr, target)/splitInfo(dataset, attr, target))
        else:
            split = splitInfo(dataset, attr, target)
            if(split == 0): # there are only one class in this attribute
                Attribute_GainRatio[attr] = 0
            else:
                gain = InfoGain(dataset, attr, target)
                # print(split, gain)
                Attribute_GainRatio[attr] = InfoGain(dataset, attr, target)/splitInfo(dataset, attr, target)

    return dataset, findBest(Attribute_GainRatio)

def MostCommenClass(node):
    children = node.getBranch()
    for key, value in children:
        print(value.count())


def predict(root, row_data, target):
    try:
        Node = root.getBranch()[row_data[root.getName()]]
    except:
        return root.getDataset()[target].value_counts().idxmax()

    if(Node.getValue() is not None): # reach a terminal node
        return Node.getValue()
    else:
        return predict(Node, row_data, target)

def test(root, dataset, target):
    result = list()
    for row in dataset.iterrows():
        result.append(predict(root, row[1], target))
    
    true_result = list(dataset[target])
    match = 0
    for i in range(0, len(true_result)):
        if(true_result[i] == result[i]):
            match+=1
    # return accuracy rate
    # print(match, len(true_result))
    return match/len(true_result)

# def MostCommenClass(node):
#     children = node.getBranch()
#     for key, value in children:
#         print(value.count())

def prune(tree, node, valid_set, target):
    # print(type(tree))
    if(len(node.getBranch()) == 0):
            return
    if(len(valid_set) == 0):
            return
    original_acc_rate = test(tree.getRoot(), valid_set, target)
    for child in node.getBranch():
        prune(tree, node.getBranch()[child], valid_set, target)
        # print(node.getDataset()[target].value_counts().idxmax())
        temp_name = node.getBranch()[child].getName()
        # temp_children = node.getBranch()
        # print(node.getDataset()[target].value_counts().idxmax())
        node.getBranch()[child].setValue(node.getBranch()[child].getDataset()[target].value_counts().idxmax())
        node.getBranch()[child].setName(None)

        new_acc_rate = test(tree.getRoot(), valid_set, target)
        # print(new_acc_rate, original_acc_rate)
        if(new_acc_rate < original_acc_rate):
            # new accuracy is lower than orignal, no prune
            node.getBranch()[child].setValue(value = None)
            node.getBranch()[child].setName(temp_name)

        # print(node)
    return