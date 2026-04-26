from abc import ABC, abstractmethod


class IProductRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, product_id):
        pass

    @abstractmethod
    def save(self, product):
        pass

    @abstractmethod
    def delete(self, product_id):
        pass


class IChatRepository(ABC):

    @abstractmethod
    def save_message(self, session_id, role, message):
        pass

    @abstractmethod
    def get_session_history(self, session_id):
        pass

    @abstractmethod
    def get_recent_messages(self, session_id, limit=5):
        pass

    @abstractmethod
    def delete_session_history(self, session_id):
        pass