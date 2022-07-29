source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}


def create_tree(in_list: list):
    """рекурсивная функция строит дерево (tree) по списку (in_list) пар id
     (id родителя (parent), id потомка (child))"""
    tree = {}
    node = tree
    for i in range(0, len(in_list)):
        parent = in_list[i][0]
        child = in_list[i][1]
        if parent is None:
            tree.update({child: {}})
        else:
            node[parent].update({child: {}})
            if i != len(in_list) - 1 and in_list[i+1][0] in tree:
                node = tree
            elif i != len(in_list) - 1 and in_list[i+1][0] != parent:
                node = node[parent]
    return tree


if __name__ == '__main__':
    assert create_tree(source) == expected
    print(create_tree(source))