from src.infrastructure.db.models import ChatMemoryModel


class ChatRepository:

    def __init__(self, db):
        self.db = db

    def save_message(self, session_id, role, message):
        msg = ChatMemoryModel(
            session_id=session_id,
            role=role,
            message=message
        )
        self.db.add(msg)
        self.db.commit()

    def get_session_history(self, session_id):
        return self.db.query(ChatMemoryModel).filter(
            ChatMemoryModel.session_id == session_id
        ).all()

    def get_recent_messages(self, session_id, limit=5):
        return self.db.query(ChatMemoryModel)\
            .filter(ChatMemoryModel.session_id == session_id)\
            .order_by(ChatMemoryModel.timestamp.desc())\
            .limit(limit)\
            .all()

    def delete_session_history(self, session_id):
        self.db.query(ChatMemoryModel)\
            .filter(ChatMemoryModel.session_id == session_id)\
            .delete()
        self.db.commit()