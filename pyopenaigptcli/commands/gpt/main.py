from json import loads as json_loads, dumps as json_dumps
from sys import stdout
from ...json.gpt import gpt as gpt_json
from ...gpt import gpt
from .arguments.parse import parse


def main():
    arguments = parse()
    instructions = arguments.instructions.read()
    input = arguments.input.read()
    if arguments.json:
        output = gpt_json(
            arguments.model, arguments.temperature, json_loads(instructions), input
        )
        output = json_dumps(output, indent=4)
    else:
        output = gpt(arguments.model, arguments.temperature, instructions, input)
    stdout.buffer.write(output.encode("utf-8"))
