# Attack Graph
"""

Attack graphs are the

"""

class AttackGraphNode(object):
    def __init__(self, name):
        self.name = name

    def __repr__():
        return self.name

class AttackFlagNode(AttackGraphNode):
    def __init__(self, name, impact=0):
        self.name = name
        self.impact = 0

class AttackStepNode(AttackGraphNode):
    def __init__(self, name, complexity=0, knowledge=0):
        self.name = name
        self.complexity = complexity
        self.knowledge = knowledge

# entry points
ep_internet = AttackGraphNode('internet')
ep_physical_local = AttackGraphNode('local physical access')
ep_supply_chain = AttackGraphNode('somewhere in the supply chain')

# flags
f_compromise_availability = AttackFlagNode('compromise availability')
f_compromise_integrity = AttackFlagNode('compromise integrity')
f_compromise_confidentiality = AttackFlagNode('comrpomise confidentiality')

# attack steps
s_hack_a_computer = AttackStepNode('hack a computer', 
                                    complexity=3, knowledge=3)
s_social_engineer_access = AttackStepNode('social engineer access', 
                                    complexity=2, knowledge=4)

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths