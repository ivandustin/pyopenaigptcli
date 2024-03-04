from pyopenaichat import chat, system, user


def gpt(instructions: str, input: str) -> str:
    messages = [system(instructions), user(input)]
    response = chat(messages)
    assert response.role == "assistant"
    return response.content
