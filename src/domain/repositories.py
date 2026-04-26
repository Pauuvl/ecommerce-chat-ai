from abc import ABC, abstractmethod

class IProductRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass


class IChatRepository(ABC):

    @abstractmethod
    def save_message(self, message):
        pass

    @abstractmethod
    def get_messages(self, session_id: str):
        pass