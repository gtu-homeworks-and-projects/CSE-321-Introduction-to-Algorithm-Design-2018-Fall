def canBeSatisfied(nCount, constraints):
    rules = {
        False: [],
        True: []
    }
    # Constructing Rules Map
    for constraint in constraints:
        varList = []
        if constraint.__contains__("!"):
            varList = constraint.split("!=")
            rules[False].append(varList)
        else:
            varList = constraint.split("=")
            rules[True].append(varList)

    # Constructing Variable Graph to link its values if they're same
    varGraph = {}
    for i in range(1, nCount + 1):
        varGraph[i] = set()
    for pair in rules[True]:
        var1 = int(pair[0])
        var2 = int(pair[1])
        varGraph[var1].add(var2)
        varGraph[var2].add(var1)

    # Check if two values in rules[False] List has path between them. If there's it means they're equal 
    for pair in rules[False]:
        var1 = int(pair[0])
        var2 = int(pair[1])
        if not find_path(varGraph, var1, var2) == None:
            return False
    return True

# Simple path finding algorithm over graph
def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.keys().__contains__(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

def main():
    ruleSet = ["1=2", "2=3", "3=4", "1!=4"]
    variableCount = 4
    print("Ruleset of", ruleSet, "can be satisfied?:", canBeSatisfied(variableCount, ruleSet))

main()