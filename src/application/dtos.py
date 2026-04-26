from pydantic import BaseModel, field_validator


class ChatMessageRequestDTO(BaseModel):
    session_id: str
    message: str

    @field_validator("message")
    def message_not_empty(cls, v):
        if not v:
            raise ValueError("Mensaje vacío")
        return v


class ChatMessageResponseDTO(BaseModel):
    session_id: str
    user_message: str
    assistant_message: str