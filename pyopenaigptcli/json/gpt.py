from json import loads as json_loads
from pyopenaichat import chat, user


def gpt(model: str, temperature: float, instructions: dict, input: str) -> str:
    # pylint: disable=redefined-builtin
    messages = [user(input)]
    tool = {
        "type": "function",
        "function": {
            "name": "function",
            "parameters": instructions,
        },
    }
    response = chat(
        messages, model=model, temperature=temperature, tools=[tool], tool_choice=tool
    )
    assert response.role == "assistant"
    assert len(response.tool_calls) == 1
    tool_called = response.tool_calls[0]
    assert tool_called.type == tool["type"]
    assert tool_called.function.name == tool["function"]["name"]
    return json_loads(tool_called.function.arguments)
