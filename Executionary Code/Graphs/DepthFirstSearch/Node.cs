using System;
using System.Collections.Generic;

/*
The class Node contains a few methods that attaches functionality to the objects
of this type. Since we create a graph, it is beneficial to have an inherent
list of its the classe's own type, since this facilitates tracing the connection
or edges between each node.
*/
  public class Node {
    public string name;
    public List<Node> children;

    public Node(string name) {
      children = new List<Node>();
      this.name = name;
    }

    public void AddChild(Node newNode) {
        this.children.Add(newNode);
    }
  }