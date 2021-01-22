from UnionFind import UF

class QuickFind(UF):
    id = None
    size = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]
        self.size = [1 for i in range(capacity)]

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def union(self, p, q):
        p = self.id[p]
        q = self.id[q]

        if p != q:
            if p < q:
                for i in range(len(self.id)):
                    if self.id[i] == p:
                        self.id[i] = q
            if p > q:
                for i in range(len(self.id)):
                    if self.id[i] == q:
                        self.id[i] = p