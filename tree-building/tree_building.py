from typing import List

ROOT_ERROR = "Root node cannot have a parent"
PARENT_ID_ERROR = "Parent id must be lower than child id"
TREE_CYCLE_ERROR = "Tree is a cycle"
RECORD_ID_ERROR = "Tree must be continuous with a 0 root id"


class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

    def validate_record(self):
        if self.record_id == 0 and self.parent_id != 0:
            raise ValueError(ROOT_ERROR)
        if self.record_id < self.parent_id:
            raise ValueError(PARENT_ID_ERROR)
        if self.record_id == self.parent_id and self.record_id != 0:
            raise ValueError(TREE_CYCLE_ERROR)


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def BuildTree(records: List[Record]) -> Node:
    records.sort(key=lambda x: x.record_id)
    validate_records(records)
    nodes = [Node(r.record_id) for r in records]

    for node in nodes:
        for rec in filter(lambda r: r.parent_id == node.node_id, records):
            for x in filter(
                lambda n: n.node_id == rec.record_id and n.node_id > 0, nodes
            ):
                node.add_child(x)

    try:
        return nodes[0]
    except IndexError:
        return None


def validate_records(records: List[Record]) -> None:
    ordered_id = [i.record_id for i in records]
    if ordered_id != list(range(0, len(ordered_id))):
        raise ValueError(RECORD_ID_ERROR)
    for record in records:
        record.validate_record()
