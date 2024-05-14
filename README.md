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

## OpenAI API Key

To use the `pyopenaigptcli` tool, you must have an OpenAI API key. Obtain an API key from OpenAI and set it using the `keyring` library.

First, install the `keyring` library using pip:

```bash
pip install keyring
```

Then, set the API key using the following command:

> **Note:** Upon running this command, you will be prompted to enter the API key in the stdin.

```bash
keyring set openai api_key
```

## OpenAI Model

By default, `pyopenaigptcli` uses the `gpt-4o` model. You can select a different model with the `--model` option:

```bash
gpt instructions.txt input.txt --model gpt-3.5-turbo > output.txt
```

### JSON Output

For structured output, provide a JSON Schema in the instructions and use the `--json` option:

```bash
gpt instructions.json input.txt --json > output.json
```
