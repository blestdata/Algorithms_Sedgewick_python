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

    def union(self, v, w):
        p = self.id[v]
        q = self.id[w]

        if p != q:
            for i in range(len(self.id)):
                if self.id[i] == p:
                    self.id[i] = q
