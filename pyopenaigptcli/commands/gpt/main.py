from sys import stdout
from ...gpt import gpt
from .arguments.parse import parse


def main():
    arguments = parse()
    contexts = list(map(lambda context: context.read(), arguments.context))
    stdout.buffer.write(gpt(arguments.command, contexts).encode("utf-8"))
