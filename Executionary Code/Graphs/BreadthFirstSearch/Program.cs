using System;
using System.Collections.Generic;

/*
    IDEA: Make a general program: NodeGraphGenerator.cs
        * This program sends json to DFS and BFS folders which are then executed
        * Connect with shell script
*/


namespace BreadthFirstSearch // Acyclic tree-like datastructure
{
    class Program
    {
        static void Main(string[] args) {
            Node[] nodes = getNodeGraph();
            List<string> output = new List<string>();

            breadthFirstSearch(output, nodes[0]);

            for (int i = 0; i < output.Count; i++) {
                Console.WriteLine(output[i]);
            }
        }

        private static void breadthFirstSearch(List<string> array, Node current) {
            Queue<Node> queue = new Queue<Node>();
            queue.Enqueue(current);

            while (queue.Count > 0) {
                current = queue.Dequeue();
                array.Add(current.name);

                //  Add from left to right
                for (int i = 0; i < current.children.Count; i++) {
                    queue.Enqueue(current.children[i]);
                }
            }
        }

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
    }
}
