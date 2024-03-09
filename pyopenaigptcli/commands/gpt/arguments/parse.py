from argparse import ArgumentParser, FileType
import keyring
import openai


def parse():
    openai.api_key = keyring.get_password("openai", "api_key")
    file = FileType("r", encoding="utf-8")
    parser = ArgumentParser(description="GPT CLI using OpenAI")
    parser.add_argument("instructions", type=file, help="Instructions file")
    parser.add_argument("input", type=file, help="Input file")
    return parser.parse_args()
