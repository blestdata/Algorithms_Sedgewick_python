from UnionFind import UF

class QuickUnionPathCompression(UF):
    id = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]
        self.count = capacity
        self.capacity = capacity

    def root(self, p):
        root_value = p
        while root_value != self.id[root_value]:
            root_value = self.id[root_value]
        last_value = p
        while p != self.id[p]:
            p = self.id[p]
            self.id[last_value] = root_value
        return p



    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        pid = self.root(p)
        qid = self.root(q)

        if pid == qid:
            return True
        self.id[p] = qid
        self.count = self.count - 1
        return True

    def printing(self):
        print("index", [i for i in range(self.capacity)], sep=" ")
        print("array", self.id, sep=" ")

if __name__ == "__main__":
    qupc = QuickUnionPathCompression(capacity=10)

    qupc.union(0, 1)

    qupc.union(2, 3)

    qupc.union(4, 5)

    qupc.union(6, 7)

    print("single unions only")

    qupc.printing()

    print("now multilevel union")

    qupc.union(6, 4)

    qupc.union(4, 2)

    qupc.union(4, 0)

    qupc.printing()