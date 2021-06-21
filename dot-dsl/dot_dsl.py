NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph:
    def __init__(self, data=[]):
        if not self.validate(data):
            raise TypeError("Invalid input")

        self.nodes = []
        self.edges = []
        self.attrs = {}

        for component in data:
            if component[0] == NODE:
                if (
                    len(component) == 3
                    and type(component[1]) == str
                    and type(component[2]) == dict
                ):
                    self.nodes.append(Node(component[1], component[2]))
                else:
                    raise ValueError("Invalid NODE components")
            if component[0] == EDGE:
                if (
                    len(component) == 4
                    and type(component[1]) == str
                    and type(component[2]) == str
                    and type(component[3]) == dict
                ):

                    self.edges.append(Edge(component[1], component[2], component[3]))
                else:
                    raise ValueError("Invalid EDGE components")
            if component[0] == ATTR:
                if (
                    len(component) == 3
                    and type(component[1]) == str
                    and type(component[2]) == str
                ):
                    self.attrs[component[1]] = component[2]
                else:
                    raise ValueError("Invalid ATTR components")
            if component[0] not in [NODE, EDGE, ATTR]:
                raise ValueError("Invalid component")

    def validate(self, data):
        return all(isinstance(x, tuple) and len(x) > 1 for x in data)
