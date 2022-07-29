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

nodes = []


def create_tree(in_list, parent):
    """рекурсивная функция строит дерево (tree) по списку (in_list) пар id
     (id родителя (parent), id потомка (child))"""
    tree = {}
    for element in in_list.copy():
        if element[0] == parent:
            nodes.append(element[1])
            tree[element[1]] = create_tree(in_list, element[1])
    return tree


if __name__ == '__main__':
    print(create_tree(source, None))
