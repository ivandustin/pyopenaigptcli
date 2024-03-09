from sys import stdout
from ...gpt import gpt
from .arguments.parse import parse


def main():
    arguments = parse()
    instructions = arguments.instructions.read()
    input = arguments.input.read()
    output = gpt(instructions, input)
    stdout.buffer.write(output.encode("utf-8"))
