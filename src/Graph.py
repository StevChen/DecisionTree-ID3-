import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, title = 'Default Title'):
        self.G = nx.DiGraph()
        self.title = title
        self.edge_labels = dict()
        self.level = 0
    
    def printTree(self, root):
        if(not root):
            return
        else:
            if(root.getValue() is not None):
                self.level+=1 # level append to the value of the terminal node so it is unique when drawing
                return str(self.level) + '_' + str(root.getValue())
            else:
                for category in root.getBranch():
                    value = self.printTree(root.getBranch()[category])
                    self.G.add_edge(root.getName(), value)
                    self.edge_labels[(root.getName(), value)] = category
                return root.getName()
    
    def draw(self, dot_file_name = 'default.dot', image_file_name = 'default.png'):
        write_dot(self.G, dot_file_name)
        plt.title(self.title)

        # layout setting
        pos =graphviz_layout(self.G, prog='dot')
        nx.draw(self.G, pos, with_labels=True, arrows=True, node_size= 500, font_size = 7)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=self.edge_labels, font_size = 5)

        # output
        plt.savefig(image_file_name, dpi = 1000)
    
    def setOutput_location(self, path):
        self.output_location = path