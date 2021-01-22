from abc import ABCMeta, abstractmethod

class UF(ABCMeta):
    __metaclass__ = ABCMeta

    @abstractmethod
    def union(self, a, b):
        pass

    @abstractmethod
    def connected(self, a, b):
        pass

    @abstractmethod
    def create(size):
        pass

class QuickFind(UF):
    id = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def union(self, p, q):
        p = self.id[p]
        q = self.id[q]

        if p != q:
            for i in range(len(self.id)):
                if self.id[i] == p:
                    self.id[i] = q

class QuickUnion(UF):
    id = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]
        self.count = capacity

    def root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p = self.root(p)
        q = self.root(q)

        if p == q:
            return
        self.id[p] = q
        self.count = self.count - 1
        return
