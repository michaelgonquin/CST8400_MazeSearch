from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.AStar import AStar

depthFirst = DFS("maze.txt")
print(depthFirst.pathInfo())

breadthFirst = BFS("maze.txt")
print(breadthFirst.pathInfo())

aStar = AStar("maze.txt")
print(aStar.pathInfo())