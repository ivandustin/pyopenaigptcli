from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
import keyring
import openai


def parse():
    openai.api_key = keyring.get_password("openai", "api_key")
    file = FileType("r", encoding="utf-8")
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="GPT CLI using OpenAI",
    )
    parser.add_argument("instructions", type=file, help="Instructions file")
    parser.add_argument("input", type=file, help="Input file")
    parser.add_argument(
        "--model", type=str, default="gpt-4-turbo-preview", help="Model name"
    )
    parser.add_argument(
        "--json", action="store_true", help="JSON Schema instructions, JSON output"
    )
    parser.add_argument(
        "--temperature", type=float, default=0.0, help="Temperature value"
    )
    return parser.parse_args()
