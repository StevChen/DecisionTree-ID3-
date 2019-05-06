import pandas as pd

dataset = pd.read_csv('./Data/mushrooms.csv')

train = dataset.sample(frac=0.2, random_state=1)
train.to_csv('train.csv', index=False)

dataset = dataset.drop(train.index)
validation = dataset.sample(frac=0.5, random_state=1)
validation.to_csv('validation.csv', index=False)

test = dataset.drop(validation.index)
test.to_csv('test.csv', index=False)

# dataset = pd.read_csv('./Data/mushrooms.csv')
# dataset = dataset.drop(['PassengerId', 'Name', 'Ticket', 'Fare'], axis=1)
# v = dataset.sample(frac=0.2, random_state=1)
# v.to_csv('validation.csv')
# dataset = dataset.drop(v.index)
# dataset.to_csv('train.csv', index=False)


# dataset = pd.read_csv('./Data/test.csv')
# dataset = dataset.drop(['PassengerId', 'Name', 'Ticket', 'Fare'], axis=1)
# dataset.to_csv('test.csv', index=False)
