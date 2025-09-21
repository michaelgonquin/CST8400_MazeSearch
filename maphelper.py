def openMaze (filename) :
    fileInp = open(f"maps/{filename}", "r")
    maze = []
    for line in fileInp.readlines() :
        newLine = list(line.replace("\n",""))
        maze.append(newLine)
    fileInp.close()
    return maze

def printMaze (maze) :
    for line in maze :
        print(line)

def neighbors(maze, pos) :
    mazeSize = mazeDimensions(maze)
    directions = {
        "U" : False,
        "D" : False,
        "L" : False,
        "R" : False
    }
    validSpaces = [".","S","G"]
    if (0 < pos["x"] < mazeSize["x"]) and (0 < pos["y"] < mazeSize["y"]) :
        if (maze[pos["y"] - 1][pos["x"]] in validSpaces) :
            directions["U"] = True
        if (maze[pos["y"] + 1][pos["x"]] in validSpaces) :
            directions["D"] = True
        if (maze[pos["y"]][pos["x"] - 1] in validSpaces) :
            directions["L"] = True
        if (maze[pos["y"]][pos["x"] + 1] in validSpaces) :
            directions["R"] = True

    return directions


def mazeDimensions(maze) :
    return toPos(len(maze[0]),len(maze))

def findEnds(maze) :
    ends = {
        "S" : "",
        "G" : ""
    }
    for y in range(len(maze)) :
        for x in range(len(maze[y])):
            if maze[y][x] in ["S", "G"] :
                ends[maze[y][x]] = toPos(x,y)

    return ends

def checkSolved(maze, pos) :
    if (maze[pos["y"][pos["x"]]] == "G") :
        return True
    return False
            
def toPos(x,y) :
    return {
        "x" : x,
        "y" : y
    }

maze = openMaze("maze.txt")

printMaze(maze)

mazeEnds = findEnds(maze)
print(neighbors(maze,mazeEnds["S"]))
