# pyopenaigptcli

The `pyopenaigptcli` is a command line interface tool that utilizes the GPT (Generative Pre-trained Transformer) model from OpenAI to generate text based on input provided by the user. This tool allows users to easily generate text using the GPT model from the command line.

## Installation

To use the `pyopenaigptcli` tool, you need to have Python installed on your system. You can install the tool using pip:

```bash
pip install git+https://github.com/ivandustin/pyopenaigptcli.git
```

## Usage

The basic syntax for using the `pyopenaigptcli` tool is as follows:

```bash
gpt instructions.txt input.txt > output.txt
```

You can also use `-` to any file parameters to read from stdin. For example:

```bash
cat input.txt | gpt instructions.txt - > README.md
```

## Practical Example

Let's say you want to write a technical document.

Write a draft of your technical document in `draft.txt`.

Create an instructions file named `tech-doc.txt` with the following content:

```
Create a technical document.
```

Generate the document with following command:

```bash
gpt tech-doc.txt draft.txt > README.md
```

## OpenAI API Key

To use the `pyopenaigptcli` tool, you need to have an OpenAI API key. You can obtain an API key from OpenAI and set it using the `keyring` library. 

First, install the `keyring` library using pip:

```bash
pip install keyring
```

Then, set the API key using the following command:

> **Note:** When you run this command, it will prompt you to enter the API key in the stdin.

```bash
keyring set openai api_key
```

## OpenAI Model

By default, `pyopenaigptcli` uses the `gpt-4-turbo-preview` model. You can select a different model with the `--model` option:

```bash
gpt instructions.txt input.txt --model gpt-3.5-turbo > output.txt
```

### JSON Output

For structured output, provide a JSON Schema instructions and use the `--json` option:

```bash
gpt instructions.json input.txt --json > output.json
```
