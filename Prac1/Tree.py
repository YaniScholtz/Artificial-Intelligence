class Node:
    def __init__(self, val, depth, parent=None):  # Constructor of the Node class

        self.r = None  # will only be initialised when a child is created
        self.p = None
        self.s = None
        self.depth = depth
        self.val = val
        self.parent = parent

    def add_children_to_node(self):  # This function adds the r , p and s to a node
        self.r = Node(val="R", depth=self.depth + 1)
        self.p = Node(val="P", depth=self.depth + 1)
        self.s = Node(val="S", depth=self.depth + 1)


class Queue:  # Making a custom class to have a queue when working with the BFS
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def popleft(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


class SearchTree:
    def __init__(self):
        self.root = Node("Start", 0)
        self.queue = Queue()  # creating the queue
        self.queue.append((self.root, []))
        self.stack = [(self.root, [])]

    def Create_and_BFS(
        self,
    ):  # function creates node in the order of how a BFS algorithm works and returns each node for searching.

        if not self.queue:
            return None
        node, parents_of_node = self.queue.popleft()

        if node.depth > 5:
            return

        node.add_children_to_node()

        if node.r:
            self.queue.append((node.r, parents_of_node + [node.val]))
        if node.p:
            self.queue.append((node.p, parents_of_node + [node.val]))
        if node.s:
            self.queue.append((node.s, parents_of_node + [node.val]))

        parents_without_start = []
        for i in parents_of_node:
            if i != "Start":
                parents_without_start = parents_without_start + [i]

        final_sequence = "".join(parents_without_start + [node.val])

        if node.val == "Start":
            return (
                self.Create_and_BFS()
            )  # we want to exclude the start nodes so we call the function again
        else:

            return final_sequence

    def Create_and_DFS(self):
        # This DFS is very alike the BFS function, the only difference is that a stack is used instead of a queue and the nodes are explored differently
        # Here a list in python works the same way as a stack so no need for an extra class
        if not self.stack:
            return None

        node, parents_of_node = self.stack.pop()

        if node.depth < 5:
            node.add_children_to_node()

            if node.s:
                self.stack.append((node.s, parents_of_node + [node.val]))
            if node.p:
                self.stack.append((node.p, parents_of_node + [node.val]))
            if node.r:
                self.stack.append((node.r, parents_of_node + [node.val]))

        parents_without_start = []
        for i in parents_of_node:
            if i != "Start":
                parents_without_start = parents_without_start + [i]

        final_sequence = "".join(parents_without_start + [node.val])

        if node.val == "Start":
            return self.Create_and_DFS()
        else:
            return final_sequence


"""Comparing the DFS with BFS: A queue structure was employed for the Breadth first search, allowing each node 
on a given level of the tree to be visited and played against the agent before proceeding to the next level.
The Depth first search algorithm made use of a stack structure . 
Using a preorder DFS algorithm, each node is visited and played against the agent, 
after which all of its children are visited and played against the agent, and so on, 
exploring all of the children of each node before moving on to the next."""
