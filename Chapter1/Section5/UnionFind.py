from abc import ABCMeta, abstractmethod

class UF(ABCMeta):
    __metaclass__ = ABCMeta

    @abstractmethod
    def union(self, a, b):
        pass

    @abstractmethod
    def connected(self, a, b):
        pass
