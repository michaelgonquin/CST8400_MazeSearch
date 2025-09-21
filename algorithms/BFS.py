from algorithms.BaseAlgorithm import BaseAlgorithm
from collections import deque

class BFS(BaseAlgorithm) :

    def __init__(self, maze) :
        super().__init__(maze)
        self.algorithmName = "Breadth First Search"

    def execute(self) :
        start, goal = self.findEnds()
        queue = deque([start])
        visited = set([start])
        parents = {}

        while queue :

            y, x = queue.popleft()

            if (y, x) == goal :
                return self.buildPath(parents, goal)
            
            self.exploredStates += 1

            for dirY, dirX in super().DIRS :
                nextY, nextX = y + dirY, x + dirX
                if (0 <= nextY <= len(self.maze) and 0 <= nextX <= len(self.maze[0])) :
                    if self.maze[nextY][nextX] != "#" and (nextY, nextX) not in visited :
                        visited.add((nextY, nextX))
                        parents[(nextY, nextX)] = (y, x)
                        queue.append((nextY, nextX))
        return None

