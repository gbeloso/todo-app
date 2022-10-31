from abc import ABC, abstractmethod

class UserRespository(ABC):
    @abstractmethod
    def add(self, user):
        raise(NotImplementedError)
    
    @abstractmethod
    def find_by_email(self, user):
        raise(NotImplementedError)

