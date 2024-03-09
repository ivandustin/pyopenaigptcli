from argparse import ArgumentParser, FileType
import keyring
import openai


def parse():
    openai.api_key = keyring.get_password("openai", "api_key")
    file = FileType("r", encoding="utf-8")
    parser = ArgumentParser(description="GPT CLI using OpenAI")
    parser.add_argument("command", type=str, help="Command")
    parser.add_argument("context", type=file, nargs="*", help="Context file")
    return parser.parse_args()
