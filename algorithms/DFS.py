from algorithms.BaseAlgorithm import BaseAlgorithm

class DFS (BaseAlgorithm) :

    def __init__ (self, maze) :
        super().__init__(maze)
        self.algorithmName = "Depth First Search"

    def execute(self) :
        start, goal = super().findEnds()
        stack = [start]
        visited = set([start])
        parents = {}

        while stack :

            y, x = stack.pop()

            if (y, x) == goal :
                return super().buildPath(parents, goal)
            
            self.exploredStates += 1

            for dirY, dirX in super().DIRS :
                nextY, nextX = y + dirY, x + dirX
                if (0 <= nextY <len(self.maze) and 0 <= nextX <= len(self.maze[0])) :
                    if (self.maze[nextY][nextX] != "#" and (nextY, nextX) not in visited) :
                        visited.add((nextY, nextX))
                        parents[(nextY, nextX)] = (y,x)
                        stack.append((nextY, nextX))
        return None