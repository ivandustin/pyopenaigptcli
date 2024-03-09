# pyopenaigptcli

The `pyopenaigptcli` is a command line interface tool that utilizes the GPT (Generative Pre-trained Transformer) model from OpenAI to generate text based on input provided by the user. This tool allows users to easily generate text using the GPT model from the command line.

## Installation

To use the `pyopenaigptcli` tool, you need to have Python installed on your system. You can install the tool using pip:

```bash
pip install pyopenaigptcli
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

## Example

Suppose you have a file named `tech-doc.txt` with the following content:

```
Create a technical document.
```

To generate a draft based on this input, you can run the following command:

```bash
gpt tech-doc.txt draft.txt > README.md
```

This command will use the GPT model to generate text based on the content of `tech-doc.txt` and save the output to `README.md`.

## OpenAI API Key

To use the `pyopenaigptcli` tool, you need to have an OpenAI API key. You can obtain an API key from OpenAI and set it using the `keyring` library. 

First, install the `keyring` library using pip:

```bash
pip install keyring
```

Then, set the API key using the following command:

```bash
keyring set openai api_key
```

When you run this command, it will prompt you to enter the API key in the stdin.