from ...gpt import gpt
from .arguments.parse import parse


def main():
    arguments = parse()
    instructions = arguments.instructions.read_text()
    input = arguments.input.read_text()
    output = gpt(instructions, input)
    print(output)
