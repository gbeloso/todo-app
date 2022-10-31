from abc import ABC, abstractmethod

class HashService(ABC):

    @abstractmethod
    def hash(self, password):
        raise(NotImplementedError)

    def check(self, password, salt):
        raise NotImplementedError