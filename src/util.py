import sys
from numpy import log2

def count(series, label):
    count = 0
    for item in series:
        if(item == label):
            count+=1
    return count

def Entropy(dataset, target):
    S = 0
    total_sample = dataset[target].count()
    for label in dataset[target].unique():
        num_label = count(dataset[target], label)
        S -= (num_label/total_sample) * log2(num_label/total_sample)
    return S

def InfoGain(dataset, attribute, target):
    EntropyS = Entropy(dataset, target)
    attribute_dataset = dataset.groupby(attribute)
    EntropySA = 0
    for category, categoryData in attribute_dataset:
         attribute_size = categoryData[attribute].count()
         sample_size = dataset[attribute].count()
         EntropySA += attribute_size/sample_size * Entropy(categoryData, target)

    return EntropyS - EntropySA

def findMostFrequentLabel(dataset):
    try:
        return dataset.value_counts().idxmax()
    except Exception as e:
        print("Error(findMostFrequentLabel) {}".format(e))
        sys.exit()

def findBestAttribute(dataset, target):
    attrOnly = dataset.drop(target, axis = 1)
    Attribute_Gain = dict()
    for attr in attrOnly.columns:
        Attribute_Gain[attr] = InfoGain(dataset, attr, target)

    def findBest(dictionary_):
        best = list(dictionary_.keys())[0]
        for key, value in dictionary_.items():
            if(value > dictionary_[best]):
                best = key
        return best

    return findBest(Attribute_Gain)