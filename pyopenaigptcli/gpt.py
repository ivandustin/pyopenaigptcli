from pyopenaichat import chat, system, user


def gpt(instructions: str, input: str) -> str:
    # pylint: disable=redefined-builtin
    messages = [system(instructions), user(input)]
    response = chat(messages)
    assert response.role == "assistant"
    return response.content
