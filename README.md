# pyopenaigptcli

`pyopenaigptcli` is a command-line interface tool that leverages the GPT (Generative Pre-trained Transformer) model from OpenAI to generate text based on user-provided input. This tool simplifies text generation using the GPT model directly from the command line.

## Installation

To use the `pyopenaigptcli` tool, ensure you have Python installed on your system. You can install the tool via pip:

```bash
pip install git+https://github.com/ivandustin/pyopenaigptcli.git
```

## Usage

The basic syntax for utilizing the `pyopenaigptcli` tool is as follows:

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

### JSON Output

For structured output, provide a [JSON Schema](https://json-schema.org/) in the instructions and use the `--json` option:

```bash
gpt instructions.json input.txt --json > output.json
```

You can use [Pydantic](https://docs.pydantic.dev/latest/) to generate a [JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/) document.
