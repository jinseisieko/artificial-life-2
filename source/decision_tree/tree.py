import random


class Tree:
    def __init__(self, depth) -> None:
        super().__init__()

        self.first = random_create_tree(depth)
        self.depth_ = depth

    def print(self):
        ms = [self.first]
        depth = self.depth_
        size = sum_of_powers_two(depth) // 2
        sep_ = " " * size
        start_ = " " * (size // 2)
        print(start_ + sep_.join([str(msx) if msx is not None else " " for msx in ms]))
        while depth > 0:
            size //= 2
            n_ms = []
            for msx in ms:
                if msx is None:
                    n_ms.append(None)
                    n_ms.append(None)
                else:
                    n_ms.append(msx.left_)
                    n_ms.append(msx.right_)
            ms = n_ms
            sep_ = " " * size
            start_ = " " * (size // 2)
            print(start_ + sep_.join([str(msx) if msx is not None else " " for msx in ms]))
            depth -= 1


class Vertex:
    def __init__(self, left_=None, right_=None, depth_=0) -> None:
        super().__init__()
        self.left_ = left_
        self.right_ = right_
        self.depth_ = depth_

    def __str__(self):
        return f"{self.depth_}"


def create_full_tree(depth, current=0):
    if current + 1 == depth:
        return Vertex(depth_=current)
    else:
        return Vertex(left_=create_full_tree(depth, current + 1), right_=create_full_tree(depth, current + 1),
                      depth_=current)


def random_create_tree(depth, current=0, leaf_chance=0.2):
    if current + 1 == depth:
        return Vertex(depth_=current)

    if random.uniform(0, 1) <= leaf_chance:
        return Vertex(depth_=current)

    return Vertex(left_=random_create_tree(depth, current + 1, leaf_chance),
                  right_=random_create_tree(depth, current + 1, leaf_chance),
                  depth_=current)


def sum_of_powers_two(n):
    result = 0
    while n >= 0:
        result += 2 ** n
        n -= 1
    return result


if __name__ == '__main__':
    tree = Tree(5)
    tree.print()
