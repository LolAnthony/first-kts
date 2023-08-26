from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        current = self._root
        dfs_list = []
        flag = flag_local = True
        while flag:
            if current not in dfs_list:
                dfs_list.append(current)
            while flag_local:
                flag_local = False
                for node in current.outbound:
                    if node not in dfs_list:
                        dfs_list.append(node)
                        current = node
                        flag_local = True
                        break
            if current == self._root:
                flag = False
            else:
                current = current.inbound[0]
                flag_local = True

        return dfs_list

    def bfs(self) -> list[Node]:
        current_values = [self._root]
        bfs_list = []
        while current_values:
            temp = []
            for node in current_values:
                if node not in bfs_list:
                    bfs_list.append(node)
            for node in current_values:
                for entry_node in node.outbound:
                    if entry_node not in bfs_list:
                        temp.append(entry_node)
            current_values = temp

        return bfs_list
