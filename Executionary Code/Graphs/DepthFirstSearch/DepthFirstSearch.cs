using System;
using System.Collections.Generic;

// Command: Create --> "dotnet new console -o name"
// Command: cd /app2 and do "dotnet run"

class DepthFirstSearch
{
    /*
        Benefit with this variable: Traverse through sub-graphs of the same graph by changing starting vertex

        Interesting values to try:
            * 0: Full grapg
            * 1: Sub-graph starting at B of size 5
            * 2: Sub-graph only containing C
            * 3: Sub-graph starting at D of size 4
    */
    static int startingIndex = 1; // Value range: Between 0 and (V - 1), where V is the number of vertices

    static void Main(string[] args) {
        Node[] nodes = getNodeGraph();

        List<string> output = new List<string>();
        depthFirstSearch(output, nodes[startingIndex]);

        printGraph(output);
    }
    
    private static void depthFirstSearch(List<string> array, Node node) {
        array.Add(node.name); // Add current node

        for (int i = 0; i < node.children.Count; i++) {
            depthFirstSearch(array, node.children[i]);
        }
    }

    /*
        Creates nodes and connects them through edges in a parent to child
        structure, and returns the graph-representation in an array consisting
        of each nodes' names.
    */
    private static Node[] getNodeGraph() {
        // Create nodes with respective values (create vertices)
        Node a = new Node("A");
        Node b = new Node("B");
        Node c = new Node("C");
        Node d = new Node("D");
        Node e = new Node("E");
        Node f = new Node("F");
        Node g = new Node("G");
        Node h = new Node("H");
        Node i = new Node("I");
        Node j = new Node("J");
        Node k = new Node("K");

        // Connect nodes to respective children (create edges)
        a.AddChild(b);
        a.AddChild(c);
        a.AddChild(d);

        b.AddChild(e);
        b.AddChild(f);

        d.AddChild(g);
        d.AddChild(h);

        f.AddChild(i);
        f.AddChild(j);

        g.AddChild(k);

        List<string> output2 = new List<string>();

        Node[] nodeGraph = {a, b, c, d, e, f, g, h, i, j, k};
        return nodeGraph;
    }

    private static void printGraph(List<string> nodes) {
        int i = -1;

        while (++i < nodes.Count) {
            Console.WriteLine(nodes[i]);
        }
    }
}