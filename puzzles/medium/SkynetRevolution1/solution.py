import sys
from collections import defaultdict
import heapq


class Graph(object):
    """ Graph data structure. """

    def __init__(self, connections):
        self._graph = defaultdict(set)
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """
        for node1, node2 in connections:
            self._graph[node1].add(node2)
            self._graph[node2].add(node1)

    def neighbors(self, node):
        return self._graph[node]

    def remove(self, node1, node2):
        """ Remove connection between node1 and node2 """
        if node1 not in self._graph or node2 not in self._graph:
            return None
        self._graph[node1].remove(node2)
        self._graph[node2].remove(node1)

    def dijkstra_search(self, node1, node2):
        frontier = []
        heapq.heappush(frontier, (0, node1))
        came_from = {}
        cost_so_far = {}
        came_from[node1] = None
        cost_so_far[node1] = 0

        while not len(frontier) == 0:
            current = heapq.heappop(frontier)[1]
            if current == node2:
                break
            for next in self.neighbors(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current
        return came_from, cost_so_far

    @staticmethod
    def reconstruct_path(came_from, node1, node2):
        if node2 in came_from:
            current = node2
            path = [current]
            while current != node1:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

    def shortest_path(self, node1, node2):
        came_from = self.dijkstra_search(node1,node2)[0]
        path = self.reconstruct_path(came_from, node1, node2)
        return path

    def __str__(self):
        return self.__class__.__name__ + '\n' + '\n'.join(
            '%s: %s' % (str(node),', '.join([str(val) for val in graph._graph[node]]))
            for node in sorted(graph._graph.iterkeys()))


# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in raw_input().split()]
# n1: N1 and N2 defines a link between these nodes
links = [tuple([int(j) for j in raw_input().split()]) for i in xrange(l)]
# the index of a gateway node
ei = [int(raw_input()) for i in xrange(e)]
graph = Graph(links)
# print >> sys.stderr, links

# game loop
while True:
    # The index of the node on which the Skynet agent is positioned this turn
    si = int(raw_input())
    # loop over all exits
    # shortest paths
    paths = []
    for ext in ei:
        path = graph.shortest_path(si,ext)
        if path is not None:
            paths.append(path)
    # and their lengths
    lengths = [len(p) for p in paths]
    # choose the closest node
    target = lengths.index(min(lengths))
    if lengths[target] > 1:
        graph.remove(paths[target][0],paths[target][1])
        print str(paths[target][0]) + ' ' + str(paths[target][1])

    # To debug: print >> sys.stderr, "Debug messages..."

