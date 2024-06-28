from json import loads as json_loads, dumps as json_dumps
from gptcli.json.gpt import gpt as gpt_json
from gptcli.gpt import gpt
from .arguments.parse import parse


def main():
    arguments = parse()
    instructions = arguments.instructions.read()
    input_text = arguments.input.read()
    if arguments.schema:
        schema = json_loads(arguments.schema.read())
        output = gpt_json(
            arguments.model, arguments.temperature, instructions, schema, input_text
        )
        output = json_dumps(output, indent=4)
    else:
        output = gpt(arguments.model, arguments.temperature, instructions, input_text)
    print(output)
