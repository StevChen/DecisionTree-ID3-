## Decision Tree Agorithm ID3(completed), C4.5(partial); with prune

Environment: Python 3.7 <br />
Libs: Numpy, Pandas <br />
Output the Diagram: Networkx, pyGraphviz

---
The implementation of the ID3 algorithm from scratch.

# Entropy and Information Gain

![Information Gain](https://latex.codecogs.com/gif.latex?Gain%28T%2C%20X%29%20%3D%20Entorpy%28T%29%20-%20Entropy%28T%2C%20X%29)

![Entropy](https://latex.codecogs.com/gif.latex?Entropy%28X%29%20%3D%20%5Csum%20-p_i%5C%3Blog_2%5C%3Bp_i)

![Entropy](https://latex.codecogs.com/gif.latex?Entropy%28T%2C%20X%29%20%3D%20%5Csum%20P%28c%29E%28c%29)

# Tree Construction:
1. Find the best attribute to split using the math formulas
2. Evaluate each category of selected attribute
3. Repeat above process for the remaining attribute

## Pseudo Code
```
function ID3(dataset, class):
{
  //Input:  dataset that using to create decision tree
  //Input:  the column_name of the classified column
  //Output: root node of the ree
  
  Create a new node; (root)
  if there is only one class type in class column, label the root with the only class type
    and return it
    
  if there is only one category in selected attribute, label the root with class
    that has most frequency and return it
    
  else
    best attribute <--- find the best attribute
    split the dataset by the category of the best attribute
    for each sub_dataset in splited dataset:
      Create new sub_tree using the dataset; (ID3(sub_dataset, class))
      Add sub_tree to the children of the root
      
    return root
}
```

## Examples
### Play Dataset
![Alt text](./src/example_0/id3_numerical.png?raw=true "ID3 Numerical Output")
![Alt text](./src/example_0/c45.png?raw=true "C4.5 Output")

### Breast-cancer Dataset
![Alt text](./src/example_1/id3.png?raw=true "ID3 Output")
![Alt text](./src/example_1/c45.png?raw=true "C4.5 Output")

### Tic Tac Toe Dataset
Before Tree Pruning
![Alt text](./src/example_2/id3_before_purne.png?raw=true "ID3 Output")
![Alt text](./src/example_2/c45_before_prune.png?raw=true "C4.5 Output")

After Tree Pruning
![Alt text](./src/example_2/id3.png?raw=true "ID3 Output")
![Alt text](./src/example_2/c45.png?raw=true "C4.5 Output")

Accuracy rate
![Alt text](./src/example_2/accuracy_rate.png?raw=true "Accuracy Rate")


### Ballroom Dataset
![Alt text](./src/example_3/id3.png?raw=true "ID3 Output")
![Alt text](./src/example_3/c45.png?raw=true "C4.5 Output")


### Mushroom Dataset
![Alt text](./src/example_4/id3.png?raw=true "ID3 Output")
![Alt text](./src/example_4/c45.png?raw=true "C4.5 Output")
Accuracy rate
![Alt text](./src/example_4/accuracy_rate.png?raw=true "Accuracy Rate")









