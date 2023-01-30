class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class DAG:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)
        return node

    def add_edge(self, source, dest):
        source.children.append(dest)

# Example usage:
dag = DAG()
nodeA = dag.add_node('A')
nodeB = dag.add_node('B')
nodeC = dag.add_node('C')
dag.add_edge(nodeA, nodeB)
dag.add_edge(nodeB, nodeC)
