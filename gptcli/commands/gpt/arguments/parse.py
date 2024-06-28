from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
from os import environ


def parse():
    file = FileType("r", encoding="utf-8")
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="GPT CLI using OpenAI",
    )
    parser.add_argument("instructions", type=file, help="Instructions file")
    parser.add_argument("input", type=file, help="Input file")
    parser.add_argument(
        "--model", type=str, default=environ["OPENAI_MODEL"], help="Model name"
    )
    parser.add_argument(
        "--temperature", type=float, default=0.0, help="Temperature value"
    )
    parser.add_argument("--schema", type=file, help="JSON Schema for structured output")
    return parser.parse_args()
