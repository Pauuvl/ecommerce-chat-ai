def test_chat_response(client):
    """
    Verifica que el chat responde.
    """
    response = client.post(
        "/chat",
        json={
            "session_id": "test123",
            "message": "Hola"
        }
    )

    assert response.status_code == 200
    assert "response" in response.json()


def test_chat_history(client):
    """
    Verifica historial del chat.
    """
    session_id = "history_test"

    # Enviar mensaje
    client.post(
        "/chat",
        json={
            "session_id": session_id,
            "message": "Hola"
        }
    )

    # Obtener historial
    response = client.get(f"/chat/history/{session_id}")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_delete_chat_history(client):
    """
    Verifica eliminación del historial.
    """
    session_id = "delete_test"

    client.post(
        "/chat",
        json={
            "session_id": session_id,
            "message": "Hola"
        }
    )

    response = client.delete(f"/chat/history/{session_id}")

    assert response.status_code == 200
    assert "message" in response.json()