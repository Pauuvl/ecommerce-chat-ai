from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Product:
    id: int
    name: str
    description: str
    brand: str
    category: str
    size: str
    color: str
    price: float
    stock: int

    def __post_init__(self):
        if not self.name:
            raise ValueError("Nombre vacío")
        if self.price <= 0:
            raise ValueError("Precio inválido")
        if self.stock < 0:
            raise ValueError("Stock inválido")

    def is_available(self):
        return self.stock > 0

    def reduce_stock(self, quantity: int):
        if quantity > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= quantity

    def increase_stock(self, quantity: int):
        if quantity <= 0:
            raise ValueError("Cantidad inválida")
        self.stock += quantity


@dataclass
class ChatMessage:
    id: int
    session_id: str
    role: str
    message: str
    timestamp: datetime

    def is_from_user(self):
        return self.role == "user"

    def is_from_assistant(self):
        return self.role == "assistant"


@dataclass
class ChatContext:
    session_id: str
    messages: List[ChatMessage]

    def get_recent_messages(self, limit=5):
        return self.messages[-limit:]

    def format_for_prompt(self):
        return "\n".join(
            [f"{m.role}: {m.message}" for m in self.messages]
        )