# gptcli

`gptcli` is a command-line interface tool that leverages the GPT (Generative Pre-trained Transformer) model from OpenAI to generate text based on user-provided input. This tool simplifies text generation using the GPT model directly from the command line.

## Installation

To use the `gptcli` tool, ensure you have Python installed on your system. You can install the tool via pip:

```bash
pip install git+https://github.com/ivandustin/gptcli.git
```

## Usage

The basic syntax for utilizing the `gptcli` tool is as follows:

```bash
gpt instructions.txt input.txt > output.txt
```

You can also use `-` for any file parameters to read from stdin. For example:

```bash
cat input.txt | gpt instructions.txt - > README.md
```

## Practical Example

Suppose you need to write a technical document.

1. Write a draft of your technical document in `draft.txt`.
2. Create an instructions file named `tech-doc.txt` with the following content:

```
Create a technical document.
```

Generate the document with the following command:

```bash
gpt tech-doc.txt draft.txt > README.md
```

## OpenAI Model

Specify the OpenAI model to be used by setting the `OPENAI_MODEL` environment variable.

You can also use the `--model` argument to specify the OpenAI model directly in the command:

```bash
gpt instructions.txt input.txt --model gpt-4o > output.txt
```

## OpenAI API Key

To authenticate with the OpenAI API, you need to specify your API key via the `OPENAI_API_KEY` environment variable.

### Structured Output

For structured output, provide a [JSON Schema](https://json-schema.org/) in the `--schema` option:

```bash
gpt instructions.txt input.txt --schema schema.json > output.json
```

You can use [Pydantic](https://docs.pydantic.dev/latest/) to generate a [JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/) document.

## GPT Function

You can import the `gpt` function in your project that allows you to generate text based on a model, temperature, instructions, and input.

### Example

```python
from gptcli import gpt

model = "gpt-4o"
temperature = 0.7
instructions = "Generate a creative story based on the following input."
input_text = "Once upon a time in a land far, far away..."

output = gpt(model, temperature, instructions, input_text)
print(output)
```

## GPT Function (Structured Output)

### Example

```python
from gptcli.json import gpt
import json

model = "gpt-4o"
temperature = 0
instructions = "Get the age of Anne."
schema = {
    "properties": {
        "age": {
            "title": "Age",
            "type": "integer"
        }
    },
    "required": [
        "age"
    ],
    "title": "Schema",
    "type": "object"
}
input_text = "The age of Prince is 26. The age of Anne is 21. The age of Anna is 19."

output = gpt(model, temperature, instructions, schema, input_text)
print(json.dumps(output, indent=4))
```

Output

```json
{
    "age": 21
}
```

## Encoding Issues

If you encounter any character encoding issue, especially in Windows, you may need to set the `PYTHONUTF8` environment variable to `1`.
