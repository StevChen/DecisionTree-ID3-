import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, title = 'Default Title'):
        self.G = nx.DiGraph()
        self.title = title
        self.edge_labels = dict()
        self.level = 0
        self.attr = 0
    
    def printTree(self, root):
        if(not root):
            return
        else:
            if(root.getValue() is not None):
                self.level+=1 # level append to the value of the terminal node so it is unique when drawing
                return str(self.level) + '_' + str(root.getValue())
            else:
                attr = self.attr
                for category in root.getBranch():
                    value = self.printTree(root.getBranch()[category])
                    self.G.add_edge(str(attr) + ' ' + str(root.getName()), value)
                    self.edge_labels[(str(attr) + ' ' + str(root.getName()), value)] = category
                    # print(str(root.getName()), value, root.getBranch()[category].getValue())
                self.attr+=1
                return str(attr) + ' ' + str(root.getName())
    
    def draw(self, dot_file_name = 'default.dot', image_file_name = 'default.png', font_size = 5, node_size = 200, line_width = 0.25, label_size = 5):
        write_dot(self.G, dot_file_name)
        plt.figure()
        plt.title(self.title)

        # layout setting, hierarchical
        pos =graphviz_layout(self.G, prog='dot')
        nx.draw(self.G, pos, with_labels=True, arrows=False, node_size = node_size, font_size = font_size, width = line_width)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=self.edge_labels, font_size = label_size)

        # output
        plt.show()
        plt.savefig(image_file_name, dpi = 1000)
    
    def setOutput_location(self, path):
        self.output_location = path