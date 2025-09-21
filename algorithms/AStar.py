import heapq
from algorithms.BaseAlgorithm import BaseAlgorithm

class AStar (BaseAlgorithm) :

    def __init__(self, maze) :
        super().__init__(maze)
        self.algorithmName = "A* Search"

    def heuristic(self, a, b) :
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def execute(self) :
        start, goal = self.findEnds()
        openSet = [(0 + self.heuristic(start, goal), 0 , start)]
        parents = {}
        gScore = {start: 0}
        visited = set()

        while openSet :
            _, cost, current = heapq.heappop(openSet)
            if current == goal :
                return self.buildPath(parents, goal)
            if current in visited :
                continue
            visited.add(current)

            self.exploredStates += 1

            y, x = current

            for dirY, dirX in super().DIRS :
                nextY, nextX = y + dirY, x + dirX
                neighbor = (nextY, nextX)
                if (0 <= nextY <= len(self.maze) and 0 <= nextX <= len(self.maze[0])) :
                    if (self.maze[nextY][nextX] == "#") :
                        continue
                    newCost = cost + 1
                    if neighbor not in gScore or newCost < gScore[neighbor] :
                        gScore[neighbor] = newCost
                        fScore = newCost + self.heuristic(neighbor, goal)
                        heapq.heappush(openSet, (fScore, newCost, neighbor))
                        parents[neighbor] = current
        return None