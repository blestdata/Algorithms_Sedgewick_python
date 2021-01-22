from abc import ABCMeta, abstractmethod, ABC

class UF(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def union(self, a, b):
        pass

    @abstractmethod
    def connected(self, a, b):
        pass

    # @abstractmethod
    # def create(size):
    #     pass

class QuickFind(UF):
    id = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]
        self.capacity = capacity

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def union(self, p, q):
        p = self.id[p]
        q = self.id[q]

        if p != q:
            for i in range(len(self.id)):
                if self.id[i] == p:
                    self.id[i] = q

    def printing(self):
        print("-" * 20)
        print("index", [i for i in range(self.capacity)], sep=" ")
        print("array", self.id, sep=" ")
        print("-" * 20)
        print(" ")

class QuickUnion(UF):
    id = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]
        self.count = capacity
        self.capacity = capacity

    def root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        pid = self.root(p)
        qid = self.root(q)

        if pid == qid:
            return
        self.id[p] = qid
        self.count = self.count - 1
        return

    def printing(self):
        print("-" * 20)
        print("index", [i for i in range(self.capacity)], sep=" ")
        print("array", self.id, sep=" ")
        print("-" * 20)
        print(" ")

class WeightedQuickUnion(UF):
    id = None
    size = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]
        self.size = [1 for i in range(capacity)]
        self.count = capacity
        self.capacity = capacity

    def root(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        pid = self.root(p)
        qid = self.root(q)

        if self.size[pid] < self.size[qid]:
            self.id[pid] = qid
            self.size[qid] = self.size[qid] + self.size[pid]
        else:
            self.id[qid] = pid
            self.size[pid] = self.size[pid] + self.size[qid]
        self.count = self.count - 1
        return

    def printing(self):
        print("-" * 20)
        print("index", [i for i in range(self.capacity)], sep=" ")
        print("array", self.id, sep=" ")
        print("-" * 20)
        print(" ")

class WeightedQuickUnionPathCompression(UF):
    id = None
    size = None

    def __init__(self, capacity):
        self.id = [i for i in range(capacity)]
        self.size = [1 for i in range(capacity)]
        self.count = capacity

    def root(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        pid = self.root(p)
        qid = self.root(q)

        if self.size[pid] < self.size[qid]:
            self.id[pid] = qid
            self.size[qid] = self.size[qid] + self.size[pid]
        else:
            self.id[qid] = pid
            self.size[pid] = self.size[pid] + self.size[qid]
        self.count = self.count - 1
        return

    def printing(self):
        print("-" * 20)
        print("index", [i for i in range(self.capacity)], sep=" ")
        print("array", self.id, sep=" ")
        print("-" * 20)
        print(" ")