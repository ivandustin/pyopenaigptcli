from pyopenaichat import chat, system, user


def gpt(model: str, instructions: str, input: str) -> str:
    # pylint: disable=redefined-builtin
    messages = [system(instructions), user(input)]
    response = chat(messages, model=model)
    assert response.role == "assistant"
    return response.content
