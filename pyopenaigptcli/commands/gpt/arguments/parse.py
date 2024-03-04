from pathlib import Path
from argparse import ArgumentParser
import keyring
import openai


def parse():
    openai.api_key = keyring.get_password("openai", "api_key")
    parser = ArgumentParser(description="GPT CLI")
    parser.add_argument("instructions", type=Path, help="Instructions file")
    parser.add_argument("input", type=Path, help="Input file")
    return parser.parse_args()
