import sys
import numpy
import pandas

def Entropy(A, B):
    return A/B*numpy.log2(A/B)


def cal_Entropy(dataset):
    S = 0
    for result in dataset:
        A = len(dataset.loc[[df['Survival'] == 1]])/len(dataset.index)      #size of yes type for dataset 
        B = len(dataset.loc[[df['Survival'] == 2]])/len(dataset.index)
        S -= Entropy(A, B)
    return S

def cal_InfoGain():
    pass

# load the data
'''
df = pandas.read_csv('train.csv')
print(df.shape)
print(df['Survived'].describe())

df = df.drop(columns='Name')
df = df.drop(columns='Ticket')
'''

df = pandas.read_csv("haberman.data")
df.columns = ["age", "operation", "pnodes", "Survival"]

print(len(df['age'].unique()))
for age in df['age'].unique():
    # print(age)
    print(age, df.groupby('age').get_group(age))


# for key, item in df.groupby("age"):
#     print(key, item)

# for key, item in df.groupby("operation"):
#     print(key, item)

# for key, item in df.groupby("pnodes"):
#     print(key, item)


df_1 = df[['age', 'Survival']]
df_1_2 = df_1.loc[df['Survival'] == 1]
df_1_1 = df_1.loc[df['Survival'] == 2]


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
