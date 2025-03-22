# Bash command: "python topological-sort.py"

# Topologica Sort: Depth First Search approach
# Time complexity: O(J + D), where J is the number of jobs and D is the dependencies.
# Since the jobs represents the vertices in the graph, and the dependencies are the
# directed arrows (edges), it resembles the time complexity of DFS and BFS, which is
# O(V + E).

def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)

    # The input format is [a, b] where a is the prerequisite and b is the actual job
    for prereq, job in deps: # Add edges by traversing through the dependencies
        graph.addPrereq(job, prereq)
    return graph


def getOrderedJobs(graph):
    orderedJobs = []
    nodes = graph.nodes

    while (len(nodes)):
        node = nodes.pop()
        containsCycle = depthFirstSearchTraverse(node, orderedJobs)

        # Invalid topological prerequisties/graph. A job cannot have a dependency to a job that has a dependency to the same one.
        # Double dependencies are a logical fallacy since we cannot generate a valid sequence with such conditions
        if containsCycle:
            return []
        
    return orderedJobs

# Returns true or false to indicate whether a cycle was detected, whereas
# monitoring the visiting-states of nodes with DFS
def depthFirstSearchTraverse(node, orderedJobs):
    if node.visited:
        return False

    if node.visiting: # We are in the process of visiting a node --> It implies a cycle is encountered, so we return true
        return True

    # If we haven't visited a node, then visit it
    node.visiting = True

    # Iterate through all prerequisite-nodes of the current node and invoke recursive function
    for prereqNode in node.prereqs:
        containsCycle = depthFirstSearchTraverse(prereqNode, orderedJobs)

        if containsCycle:
            return True

    # Update state after traversal: The current node is now visited and is no longer being visited
    node.visited = True
    node.visiting = False

    orderedJobs.append(node.job)


# The class that has the responsibility to deal with the graph
class JobGraph:
    def __init__(self, jobs): # Add jobs as nodes
        self.nodes = []
        self.graph = {} # Hashtable

        # Add all jobs to the graph and register them as nodes
        for job in jobs:
            self.addNode(job)

    # Plot the job as a node in the graph
    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    # Append the current prerequisite to the specific job
    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    # Access job (node) in graph in constant time with hashtable
    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]


# The class that solely stores the properties of a graph-node.
# Note that we always initially assign the job with false visiting-states,
# along with an empty prerequisite array that is assigned later on
class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = [] # Consists of the nodes which are prerequisites to the specific node
        self.visited = False
        self.visiting = False


def runProgram():
    jobs = [1, 2, 3, 4]
    deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    output = topologicalSort(jobs, deps)
    print("OUTPUT:" + str(output))

runProgram()