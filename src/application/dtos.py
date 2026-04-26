from pydantic import BaseModel

class ProductDTO(BaseModel):
    name: str
    description: str
    brand: str
    category: str
    price: float
    stock: int


class ChatMessageRequestDTO(BaseModel):
    session_id: str
    message: str


class ChatMessageResponseDTO(BaseModel):
    response: str


class ChatHistoryDTO(BaseModel):
    session_id: str
    messages: list