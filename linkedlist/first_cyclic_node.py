# find the first node of a cycle in the linked list.

# 1 -> 2 -> 3 -> 4 -> 5 -> 1  => 1
# A -> B -> C -> D -> E -> C  => C

def firstCyclicNode(Node):
    if not Node:
        return Node

    walker, runner, entry = Node, Node, Node
    while walker.next and runner.next.next:
        walker = walker.next
        runner = runner.next.next
        if walker == runner:
            while (walker != entry):
                walker = walker.next
                entry = entry.next
            return entry

    return None


