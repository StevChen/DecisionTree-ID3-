import sys
import numpy
import pandas as pd

def Entropy(attributes):
    S = 0
    total = float(sum(attributes))
    for attr in attributes:
        S += -1*(float(attr)/total)*(numpy.log2(float(attr)/total))
    return S

def InfoGain(dataset, overallEntropy):
    attrGroup = dataset.groupby('attribute')
    mlist = dataset['result'].unique()
    gain = 0

    for key, value in attrGroup:
        attributes = list()
        homo = False
        for m in mlist:
            A = value.loc[value['result'] == m]['result'].count()
            if(A == 0):
                homo = True       
                break
            attributes.append(A)
        if(not homo): # zero entropy for homogenous sample
            gain += value['result'].count()/dataset['result'].count() * Entropy(attributes)
    return gain

        # S.columns = ['freq']
        # total = S['freq'].sum()
        # print(S)
        # print(total)
        
    

    # for key, value in attrGroup:
    #      A = value.loc[value['result'] == 'T']
    #      print(A)

# load the data
'''
df = pandas.read_csv('train.csv')
print(df.shape)
print(df['Survived'].describe())

df = df.drop(columns='Name')
df = df.drop(columns='Ticket')
'''

# df = pandas.read_csv("haberman.data")
# df.columns = ["age", "operation", "pnodes", "Survival"]

# print(len(df['age'].unique()))
# for age in df['age'].unique():
#     # print(age)
#     print(age, df.groupby('age').get_group(age))


# for key, item in df.groupby("age"):
#     print(key, item)

# for key, item in df.groupby("operation"):
#     print(key, item)

# for key, item in df.groupby("pnodes"):
#     print(key, item)


# df_1 = df[['age', 'Survival']]
# df_1_2 = df_1.loc[df['Survival'] == 1]
# df_1_1 = df_1.loc[df['Survival'] == 2]


# df_1_2 = len((df.groupby('age').get_group(30).loc[df['Survival'] == 2]).index)
# print(df_1_2)
# ages = df.age
# print(df.groupby('age').get_group(30)['Survival'])
# print(df.groupby('operation'))
# ages = ages.groupby('age').count()
# print(ages)


#frequency_set = df_1.groupby('age')['Survival'].count()
#print(frequency_set)
# print(df_1.age)
# for i in df_1.age:
#     print(i)
# print(df_1_1)
# print(df_1_2)

#for age in df['age']:
#    print(age)

#print(df['age'])


nstretch = pd.read_csv('adult-stretch.data')
nstretch.columns = ["color", "size", "mode", "person", "result"]
resultColumn = nstretch.result
nstretch_no_result = nstretch.drop('result', axis = 1)

mlist = resultColumn.unique()
attributes = list()
for value in mlist:
    S = resultColumn.loc[resultColumn == value].count()
    print(type(S), S)
    attributes.append(S)
overallEntropy = Entropy(attributes)
print(overallEntropy)


for column in nstretch_no_result.columns:
    print("==============================")
    print(column)
    dataset = nstretch[[column, 'result']]
    dataset.columns = ["attribute", "result"]
    infoGain = InfoGain(dataset, overallEntropy)
    print(infoGain)

    # S = cal_Entropy(group, column, 'result', mlist)
    # print("Entropy({}): {}".format(column, S))

# colorGroups = nstretch.groupby('color')
# sizeGroups = nstretch.groupby('size')
# modeGroups = nstretch.groupby('mode')
# personGroups = nstretch.groupby('person')
# mlist = ['T', 'F']
# S = cal_Entropy(colorGroups, 'color', 'result', mlist)
# print("Entropy(color): ", S)

# S = cal_Entropy(sizeGroups, 'size', 'result', mlist)
# print('Entropy(size): ', S)

# S = cal_Entropy(modeGroups, 'mode', 'result', mlist)
# print('Entropy(mode): ', S)

# S = cal_Entropy(personGroups, 'person', 'result', mlist)
# print('Entropy(person): ', S)


# print(nstretch.groupby('color').get_group('YELLOW'))
# print(nstretch.groupby(''))
# print(pstretch)