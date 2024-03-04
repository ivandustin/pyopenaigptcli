# pyopenaigptcli

## Overview

`pyopenaigptcli` is a command line interface tool that allows users to easily interact with the GPT (Generative Pre-trained Transformer) model provided by OpenAI. This tool simplifies the process of generating text using the GPT model by providing a straightforward command line interface.

## Installation

To install `pyopenaigptcli`, you can use pip:

```bash
pip install pyopenaigptcli
```

## Usage

Once installed, you can use the `gpt` command to generate text using the GPT model. The syntax for using the tool is as follows:

```bash
gpt instructions.txt input.txt
```

- `instructions.txt`: A text file containing instructions or prompts for the GPT model to generate text based on.
- `input.txt`: A text file containing additional input or context for the GPT model to consider while generating text.

The generated text will be displayed on the standard output (stdout) of the command line.

## Example

Let's consider an example where we want to generate a creative story based on a prompt and some additional context. We have the following files:

`instructions.txt`:
```
Write a short story about a robot who learns to love.
```

`input.txt`:
```
The robot's name was Robo, and it had a heart made of gears and wires.
```

To generate the story, we can run the following command:

```bash
gpt instructions.txt input.txt
```

The output will be the generated text based on the prompt and input provided.
