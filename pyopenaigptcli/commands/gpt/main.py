from json import loads as json_loads, dumps as json_dumps
from sys import stdout
from pyopenaigptcli.json.gpt import gpt as gpt_json
from pyopenaigptcli.gpt import gpt
from .arguments.parse import parse


def main():
    arguments = parse()
    instructions = arguments.instructions.read()
    input_text = arguments.input.read()
    if arguments.json:
        output = gpt_json(
            arguments.model, arguments.temperature, json_loads(instructions), input_text
        )
        output = json_dumps(output, indent=4)
    else:
        output = gpt(arguments.model, arguments.temperature, instructions, input_text)
    stdout.buffer.write(output.encode("utf-8"))
