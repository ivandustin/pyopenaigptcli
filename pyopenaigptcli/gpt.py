from itertools import chain
from typing import List
from pyopenaichat import chat, system, user


def gpt(command: str, contexts: List[str]) -> str:
    messages = list(chain([system(command)], map(user, contexts)))
    response = chat(list(reversed(messages)))
    assert response.role == "assistant"
    return response.content
