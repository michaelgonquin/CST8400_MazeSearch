class BaseAlgorithm :

    DIRS = [(-1,0),(1,0),(0,-1),(0,1)] #Up, Down, Left, Right

    def __init__ (self, mazeName) :
        self.maze = self.openMaze(mazeName)
        self.algorithmName = ""
        self.exploredStates = 0

    def openMaze (self, filename) :
        fileInp = open(f"maps/{filename}", "r")
        maze = []
        for line in fileInp.readlines() :
            newLine = list(line.replace("\n",""))
            maze.append(newLine)
        fileInp.close()
        return maze

    def printMaze (self) :
        for line in self.maze :
            print(line)

    def findEnds(self) :
        start = None
        goal = None
        for y in range(len(self.maze)) :
            for x in range(len(self.maze[0])) :
                if (self.maze[y][x] == "S") :
                    start = (y,x)
                elif (self.maze[y][x] == "G") :
                    goal = (y,x)
        return start, goal

    def buildPath(self, parents, goal) :
        path = []
        current = goal
        while current in parents :
            path.append(current)
            current = parents[current]
        return path[::-1]
    
    def pathInfo(self) :
        result = self.execute()
        return f"Algorithm Name: {self.algorithmName}\nMoves Taken: {len(result)}\nExplored States: {self.exploredStates}\nCoordinate Path: {result}\nRelative Path: {self.translatePath(result)}\n\n"

    def translatePath(self, path) :
        moves = [self.findEnds()[0]]
        dirs = {
            (-1,0) : "U",
            (1,0) : "D",
            (0,-1) : "L",
            (0,1) : "R"
        }

        moveDir = (path[0][0] - moves[0][0], path[0][1] - moves[0][1])
        moves.append(dirs[moveDir])

        for i in range(len(path) - 1) :
            moveDir = (path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])
            moves.append(dirs[moveDir])

        return moves

                
    
    def execute(self) :
        pass